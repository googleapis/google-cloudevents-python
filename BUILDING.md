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
1. For a test run, run the script, specifying a folder of your choice for the output:  
    `python generate-from-proto.py -o [OUTPUT_DIR]`  
    and examine the contents of *[OUTPUT_DIR]*.
1. Update the library by having the generator script replace the repository src folder:  
    `python generate-from-proto.py -o ../src`

You can install or distribute the updated library with the previous instructions.
