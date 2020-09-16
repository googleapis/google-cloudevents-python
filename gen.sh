#!/bin/bash
set -e

EVENTS_SPEC_REPO='https://github.com/michaelawyu/google-cloudevents'

echo "Cleaning things up..."
rm -rf workplace/ || true
mkdir workplace
rm -rf src/ || true
mkdir src
pip uninstall google-events

echo "Cloning the event specification repository from GitHub..."
git clone $EVENTS_SPEC_REPO workplace/

echo "Adding the qt package as a dependency..."
mv workplace/tools/quicktype-wrapper gen/quicktype-wrapper
cd gen/
npm install

echo "Generating the Google Events Library for Python..."
export IN="../workplace/proto"
export OUT="../"
npm run start

echo "Cleaning things up..."
rm -rf workplace/ || true

echo "Completed!"
echo "To install the generated package, run pip install -e ."