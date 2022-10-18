#!/bin/bash
set -e

EVENTS_SPEC_REPO='https://github.com/googleapis/google-cloudevents'
EVENTS_SPEC_DIR=${EVENTS_SPEC_DIR:="./tmp/cloudevents-parent"}

echo "Cloning the event specification repository from GitHub..."
if [ ! -d $EVENTS_SPEC_DIR ]; then
  git clone $EVENTS_SPEC_REPO $EVENTS_SPEC_DIR
fi

echo "Generating the Google Events Library for Python..."
export IN=$EVENTS_SPEC_DIR

# Directories to include in protoc search path.
PROTOC_INCLUDES="-I /usr/include -I ${EVENTS_SPEC_DIR}/proto -I  ${EVENTS_SPEC_DIR}/third_party/googleapis/ "

# Generate code for protos defined in this repo
for protofile in $(find ${IN}/proto -name 'data.proto' -type f); do
  protopath=$(realpath --relative-to ${IN}/proto $protofile)
  echo $protopath
  python -m grpc_tools.protoc $PROTOC_INCLUDES $protofile --python_gapic_out=src
done

# Generate code for dependencies included in this repo.
# Note that we're using the regular python generator here, as the gapic-generator produces
# different import paths, and does not find the generated types.
for protofile in $(find ${IN}/third_party/googleapis -type f -name '*.proto'); do
  protopath=$(realpath --relative-to ${IN}/proto $protofile)
  echo $protopath
  protoc $PROTOC_INCLUDES $protofile --pyi_out=src --python_out=src
done

echo "Completed!"
echo "To install the generated package, run pip install -e ."
