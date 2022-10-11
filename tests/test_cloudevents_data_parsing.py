# Parse and validate text-formatted Cloud Event payload data in a variety of
# google types.

import importlib
import os
import unittest

import google.protobuf.json_format as json_format
import pytest


def make_test_case(filename, pkg, cls):
    """Returns a test function that loads the given file as the supplied proto class."""

    def testfn():
        with open(filename) as f:
            raw_data = f.read()
        mod = importlib.import_module(pkg)
        obj = json_format.Parse(
            raw_data, mod.__dict__.get(cls)(), ignore_unknown_fields=True
        )
        emptyobj = mod.__dict__.get(cls)()
        assert obj != emptyobj

    return testfn


def get_import_for_file(relfile):
    """return the python package and class name for a given testdata file."""
    pkg = os.path.dirname(relfile).replace("/", ".")
    if pkg != "":
        # python proto modules are named after their proto files.
        pkg += ".data_pb2"
    cls = os.path.basename(relfile).split("-")[0]
    return pkg, cls


class TestdataParsing(unittest.TestCase):
    """Load testdata files from $GOOGLE_EVENTS_TESTDATA directory and verify parsing."""

    def test_parsing(self):
        testdata_root = os.getenv("GOOGLE_EVENTS_TESTDATA")
        if testdata_root == None:
            self.skipTest("set GOOGLE_EVENTS_TESTDATA to run these tests")
        for dirpath, _, files in os.walk(testdata_root):
            for file in files:
                loadpath = os.path.join(dirpath, file)
                rfile = os.path.relpath(
                    os.path.join(dirpath, file), start=testdata_root
                )
                (pkg, cls) = get_import_for_file(rfile)
                with self.subTest(f=loadpath):
                    if file[-5:] != ".json":
                        self.skipTest("Skipping non-json file {}".format(loadpath))
                        continue
                    make_test_case(loadpath, pkg, cls)()


if __name__ == "__main__":
    unittest.main()
