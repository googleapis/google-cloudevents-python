# Utility functions for writing tests for google-cloudevents

import importlib

def make_test_case(filename, pkg, cls):
    """Returns a test function that loads the given file as the supplied proto class."""

    def testfn():
        with open(filename) as f:
            raw_data = f.read()
        klass = getattr(importlib.import_module(pkg), cls)
        obj = klass.from_json(raw_data, ignore_unknown_fields=True)
        emptyobj = klass()
        assert obj != emptyobj
        return obj

    return testfn