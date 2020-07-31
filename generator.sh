EVENTS_SPEC_REPO='https://github.com/googleapis/google-cloudevents.git'

echo "Cleaning things up."
rm -rf workplace/ || true
mkdir workplace
rm -rf google/ || true

echo "Cloning the event specification repository from GitHub."
git clone $EVENTS_SPEC_REPO workplace/

echo "Generating Python code using Protocol Buffers Generator."
if [ -n "$PROTOC" ] && [ -n "$PROTOC_INCLUDE" ]; then
    $PROTOC -I workplace/proto/ -I "$PROTOC_INCLUDE" -I workplace/third_party/googleapis/ --python_out=. $(find workplace/proto/ -name '*.proto')
else
    echo "Environment variable PROTOC and/or PROTOC_INCLUDE are not set."
    echo "Set PROTOC to the path of the executable of Protocol Buffers Generator."
    echo "Set PROTOC_INCLUDE to the path of the include directory in the Protocol Buffers package."
    echo "To install the Protocol Buffers Generator, see https://developers.google.com/protocol-buffers/docs/downloads."
    exit 1
fi

echo "Patching the generatoed code and preparing the code into a Python package."
pip install -r requirements.txt
python generator.py

echo "Completed! See gen_package/ for the generators package."
echo "To install the generated package, run pip install -e gen_package/"
