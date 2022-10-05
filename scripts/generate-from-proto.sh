#!/bin/bash
set -e

EVENTS_SPEC_REPO='https://github.com/googleapis/google-cloudevents'
EVENTS_SPEC_DIR=${EVENTS_SPEC_DIR:="./tmp/cloudevents-parent"}

GOOGLEAPIS_REPO='https://github.com/googleapis/googleapis'
GOOGLEAPIS_DIR=${GOOGLEAPIS_DIR:="./tmp/googleapis-protos"}

echo "Cloning the event specification repository from GitHub..."
if [ ! -d $EVENTS_SPEC_DIR ]; then
  git clone $EVENTS_SPEC_REPO $EVENTS_SPEC_DIR
fi
echo "Cloning Google API proto types repository from GitHub..."
if [ ! -d $GOOGLEAPIS_DIR ]; then
  git clone $GOOGLEAPIS_REPO $GOOGLEAPIS_DIR
fi

echo "Generating the Google Events Library for Python..."
export IN=$EVENTS_SPEC_DIR

# Directories to include in protoc search path.
PROTOC_INCLUDES="-I /usr/include -I ${EVENTS_SPEC_DIR}/proto -I ${GOOGLEAPIS_DIR}/"

for protofile in $(find ${IN}/proto -name 'data.proto' -type f); do
  protopath=$(realpath --relative-to ${IN}/proto $protofile)
  echo $protopath
  if [ "$protopath" == "google/events/cloud/iot/v1/data.proto" ]; then
    # pyi files cannot be produced for this proto. For further context see
    # https://github.com/protocolbuffers/protobuf/issues/10246
    protoc $PROTOC_INCLUDES $protofile --python_out=src
  else
    protoc $PROTOC_INCLUDES $protofile --pyi_out=src --python_out=src
  fi
done

echo "Completed!"
echo "To install the generated package, run pip install -e ."
