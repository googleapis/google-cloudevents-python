import re

from setuptools import find_packages, setup

with open("README.md", "rt") as f:
    readme = f.read()

setup(
    name="google-events",
    version="0.0.1",
    url="https://github.com/googleapis/google-cloudevents",
    project_urls={
        "Source": "https://github.com/googleapis/google-cloudevents",
        "Documentation": "",
        "Issue Tracker": "https://github.com/googleapis/google-cloudevents/issues",
    },
    license="Apache License 2.0",
    author="Google DevRel",
    author_email="",
    maintainer="Google DevRel",
    maintainer_email="",
    description="A collection of first party Google Cloud Platform event objects.",
    long_description=readme,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Internet",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=find_packages("src"),
    package_dir={"": "src"},
    python_requires=">3.4",
    install_requires=["protobuf", "googleapis-common-protos"],
    extras_require={
        "dev": ["pylint", "pytest", "black"],
    },
)
