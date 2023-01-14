
import argparse
import os
import shutil
import tempfile
import zipfile

from grpc_tools import protoc
import requests


#SPEC_URL = "https://github.com/googleapis/google-cloudevents/archive/refs/heads/main.zip"


def protofiles(proto_dir, proto_names=["data.proto"]):
    files = []

    for (dirpath, _, filenames) in os.walk(proto_dir):
        for filename in filenames:
            if filename in proto_names:
                full_name = os.path.join(dirpath, filename)
                relative_name = os.path.relpath(full_name, proto_dir)
                files.append(relative_name)
    return files


def generate(includes, protofile,  out_dir):
    cli_params = []
    for inc in includes:
        cli_params.append(f"-I{inc}")

    cli_params.append(protofile)
    cli_params.append(f"--python_gapic_out={out_dir}")

    protoc.main(cli_params)


def create_module_directory(directory, confirm_deletions):
    path = os.path.abspath(directory)
    if os.path.exists(path):
        if confirm_deletions:
            confirmation = input(f"Delete {path} and all its contents? (y/N) ")
            if confirmation.lower() != 'y':
                return None

        # WARNING: Data deleting operation below!
        shutil.rmtree(path)

    os.mkdir(path)
    return path


def download(url, filename):
    with requests.get(url, stream=True) as req:
        req.raise_for_status()
        with open(filename, "wb") as f:
            for chunk in req.iter_content(chunk_size=8192):
                f.write(chunk)


def fetch_proto_repo(repo_name, branch):
    repo_zip_url = f"https://github.com/{repo_name}/archive/refs/heads/{branch}.zip"
   
    temp_dir = tempfile.TemporaryDirectory()
    temp_dir_name = temp_dir.name

    repo_zip_file = os.path.join(temp_dir_name, "repo.zip")
    download(repo_zip_url, repo_zip_file)

    zipfile.ZipFile(repo_zip_file).extractall(path=temp_dir_name)

    repo_root_path = os.path.join(temp_dir_name, f"{repo_name.split('/')[1]}-{branch}")

    # Don't let the temp_dir object go out of scope until it's okay to remove
    return repo_root_path, temp_dir


def generate_code_for_protos(repo_path, module_path):
    for fname in protofiles(f"{repo_path}/proto"):
        generate(["/usr/include", f"{repo_path}/proto", f"{repo_path}/third_party/googleapis/", "/home/engelke/Git/protobuf/src/"], fname, module_path)
    pass


def generate_code_for_dependencies(repo_path, module_path):
    pass


def generate_module(module_dir, proto_repo, branch, do_not_confirm_actions):
    module_path = create_module_directory(module_dir, not do_not_confirm_actions)
    if module_path is None:
        print("Operation aborted by user.")
        return False

    repo_root_path, temp_dir = fetch_proto_repo(proto_repo, branch)
    generate_code_for_protos(repo_root_path, module_path)
    generate_code_for_dependencies(repo_root_path, module_path)

    temp_dir.cleanup()
    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Generate Google Cloudevents Python library",
        description="Creates a new Python module for Google Cloudevents",
    )

    parser.add_argument(
        "-o", "--output", required=True,
        help="Directory to write the module source. "
        "Will be created if necessary. "
        "WARNING - preexisting contents will be deleted!",
    )

    parser.add_argument(
        "-r", "--repo",
        help="GitHub repo containing protofiles for Cloud events",
        default="googleapis/google-cloudevents",
    )

    parser.add_argument(
        "-b", "--branch",
        help="Repo branch to fetch",
        default="main",
    )

    parser.add_argument(
        "-q", "--quiet", action='store_true',
        help="do not confirm any steps (even data destructive ones)",
    )

    args = parser.parse_args()

    if generate_module(args.output, args.repo, args.branch, args.quiet):
        print(f"Module generation complete. Source is at {args.output}")
    else:
        print(f"Module generation failed. See error output for details.")
