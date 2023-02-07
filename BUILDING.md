# Building the google-events Python library

## Installing the current version

The library source in this repository can be installed and used as is:

1. Clone or download the repository contents
1. Instantiate a virtual Python environment if desired.
1. In a shell, change to the repository root.
1. Install with `pip install -e .`

## Building a distribution

A Python wheel can be created for the current contents of this repository as
follows:

1. Clone or download the repository contents
1. Instantiate a virtual Python environment if desired.
1. In a shell, change to the repository root.
1. Install the standard *build* library:  
    `pip install --upgrade build`
1. Build the distributions(s):  
    `python -m build .`
1. The *dist* folder will contain distributable packages in those formats
available to your installation.

## Updating the library

Whenever the *googleapis/cloudevents* proto definitions change, the matching
Python *google-events* library can be updated to match, as follows:

1. Clone or download the repository contents
1. Instantiate a virtual Python environment if desired.
1. In a shell, change to the repository root, then the *scripts* folder:   
    `cd scripts`
1. Install the required libraries to run the generator script:  
    `pip install -r requirements.txt`
1. Run the script, specifying a folder of your choice for the output:  
    `python generator-from-proto.py -o [OUTPUT_DIR]`

You can use the updated library directly from the generated *[OUTPUT_DIR]/src*
folder by adding it to your `PYTHONPATH`, or you can replace the contents of the
local repository's `/src` folder with the generated *[OUTPUT_DIR]/src* folder
and install or distribute it with the previous instructions.
