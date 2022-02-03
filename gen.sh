#!/bin/bash
set -e

# EVENTS_SPEC_REPO='https://github.com/googleapis/google-cloudevents'

# echo "Cleaning things up..."
# rm -rf workplace/ || true
# mkdir workplace
rm -rf src/ || true
mkdir src
# rm -rf gen/quicktype-wrapper || true

# echo "Cloning the event specification repository from GitHub..."
# git clone $EVENTS_SPEC_REPO workplace/

# echo "Adding the qt package as a dependency..."
# mv workplace/tools/quicktype-wrapper gen/quicktype-wrapper
cd gen/quicktype-wrapper
npm install
cd ../
npm install

echo "Generating the Google Events Library for Python..."
export IN="../workplace/jsonschema"
export OUT="../"
export EXAMPLES="../workplace/testdata"
npm run start

# echo "Cleaning things up..."
# cd ..
# rm -rf workplace/ || true

echo "Completed!"
echo "To install the generated package, run pip install -e ."