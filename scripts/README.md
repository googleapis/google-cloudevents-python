# Generating google-events-cloud and google-events-firebase

The program `generate-from-proto.py` will fetch the Google Cloudevents proto
files from a Github repository and generate Python libraries for each type of
event defined there.

Before running the generator, create a virtual Python environment (recommended)
and install the libraries it needs with:

    pip install -r requirements.txt

You will also need an Internet connection as the generator fetches the event
definitions from Github.

## Code generator usage: python generate-from-proto.py *[arguments]*

Arguments are:

<dl>

<dt><code>-h</code> or <code>--help</code></dt>
<dd>
    Print help and then exit without other action.
</dd>

<dt><code>-q</code> or <code>--quiet</code></dt>
<dd>
    If specified, do not prompt for confirmation of any operation, including
    ones that would delete files or directories.
</dd>

<dt><code>-o <em>[dirname]</em></code> or <code>--out <em>[dirname]</em></code></dt>
<dd>
    <strong>Required.</strong> Write generated library source code to
    <em><code>dirname</code></em>. That directory, and all its contents, will be
    deleted first. Program will prompt user for confirmation before deleting
    any contents, unless <code>-q</code> or <code>--quite</code> is specified.
</dd>

<dt><code>-r <em>[repo-name]</em></code> or <code>--repo <em>[repo-name]</em></code></dt>
<dd>
    Optional. Fetch proto definitions from Github repo
    <em><code>repo-name</code></em>. Default, if not specified, is
    <code>googleapis/google-cloudevents</code>.
</dd>

<dt><code>-b <em>[branch-name]</em></code> or <code>--out <em>[branch-name]</em></code></dt>
<dd>
    Optional. Fetch proto definitions from Github branch
    <em><code>branch-name</code></em>. Default, if not specified, is
    <code>main</code>.
</dd>

</dl>

## Installing the generated libraries

The generated code can be packaged and installed using standard Python packaging
tools. Or, the library can be installed directly from source by changing to the
generated code library and running:

    pip install .

## Sample code using the libraries

Print the name of the bucket and object that triggered the event:

    from google.events.cloud import storage

    with open("file-containing-storage-json-example", "r") as f:
        example = f.read()

    event = storage.StorageObjectData.from_json(example)
    print(f"Bucket is {event.bucket}")
    print(f"Name is {event.name}")
