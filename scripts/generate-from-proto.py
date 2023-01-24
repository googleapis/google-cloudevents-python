import argparse
import fnmatch
import os
import shutil
import tempfile
import zipfile

from grpc_tools import protoc
import requests


def protofiles(proto_dir, proto_names):
    files = []

    for (dirpath, _, filenames) in os.walk(proto_dir):
        for filename in filenames:
            for protoname in proto_names:
                if fnmatch.fnmatch(filename, protoname):
                    full_name = os.path.join(dirpath, filename)
                    relative_name = os.path.relpath(full_name, proto_dir)
                    files.append(relative_name)
    return files


def generate(includes, protofile, other_args):
    cli_params = []
    for inc in includes:
        cli_params.append(f"-I{inc}")

    cli_params.append(protofile)

    for arg in other_args:
        cli_params.append(arg)

    protoc.main(cli_params)


def create_module_directory(directory, confirm_deletions):
    path = os.path.abspath(directory)
    if os.path.exists(path):
        if confirm_deletions:
            confirmation = input(f"Delete {path} and all its contents? (y/N) ")
            if confirmation.lower() != "y":
                return None

        # WARNING: Data deleting operation below!
        shutil.rmtree(path)

    os.mkdir(path)
    return path


def download(url, filename):
    with requests.get(url, stream=True) as req:
        req.raise_for_status()
        with open(filename, "wb") as f:
            f.write(req.raw.read())


def fetch_repo(repo_name, branch, dir_name):
    # Github convention for downloading as zip:
    repo_zip_url = f"https://github.com/{repo_name}/archive/refs/heads/{branch}.zip"

    # Name downloaded zip file for end of repo_name
    repo_zip_name = f"{repo_name.split('/')[1]}.zip"
    repo_zip_path = os.path.join(dir_name, repo_zip_name)

    download(repo_zip_url, repo_zip_path)
    zipfile.ZipFile(repo_zip_path).extractall(path=dir_name)

    repo_root_path = os.path.join(dir_name, f"{repo_name.split('/')[1]}-{branch}")

    return repo_root_path


def generate_code_for_protos(proto_path, std_proto_path, module_path):
    for fname in protofiles(f"{proto_path}/proto", ["data.proto"]):
        generate(
            [
                "/usr/include",
                f"{proto_path}/proto",
                f"{proto_path}/third_party/googleapis/",
                f"{std_proto_path}/src/",
            ],
            fname,
            [
                f"--python_gapic_out={module_path}",
            ],
        )


def generate_code_for_dependencies(proto_path, std_proto_path, module_path):
    for fname in protofiles(f"{proto_path}/third_party/googleapis", ["*.proto"]):
        generate(
            [
                "/usr/include",
                f"{proto_path}/proto",
                f"{proto_path}/third_party/googleapis/",
                f"{std_proto_path}/src/",
            ],
            fname,
            [
                f"--pyi_out={module_path}",
                f"--python_out={module_path}",
            ],
        )


def generate_module(module_dir, proto_repo, branch, do_not_confirm_actions):
    module_path = create_module_directory(module_dir, not do_not_confirm_actions)
    if module_path is None:
        print("Operation aborted by user.")
        return False

    with tempfile.TemporaryDirectory() as tempdir:
        # Fetch repo with cloudevent proto definitions
        proto_path = fetch_repo(proto_repo, branch, tempdir)

        # Fetch repo with referenced common protos (e.g., timestamp)
        std_proto_path = fetch_repo("protocolbuffers/protobuf", "main", tempdir)

        generate_code_for_protos(proto_path, std_proto_path, module_path)
        generate_code_for_dependencies(proto_path, std_proto_path, module_path)

    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Generate Google Cloudevents Python library",
        description="Creates a new Python module for Google Cloudevents",
    )

    parser.add_argument(
        "-o",
        "--output",
        required=True,
        help="Directory to write the module source. "
        "Will be created if necessary. "
        "WARNING - preexisting contents will be deleted!",
    )

    parser.add_argument(
        "-r",
        "--repo",
        help="GitHub repo containing protofiles for Cloud events",
        default="googleapis/google-cloudevents",
    )

    parser.add_argument(
        "-b",
        "--branch",
        help="Repo branch to fetch",
        default="main",
    )

    parser.add_argument(
        "-q",
        "--quiet",
        action="store_true",
        help="do not confirm any steps (even data destructive ones)",
    )

    args = parser.parse_args()

    if generate_module(args.output, args.repo, args.branch, args.quiet):
        print(f"Module generation complete. Source is at {args.output}")
    else:
        print(f"Module generation failed. See error output for details.")
