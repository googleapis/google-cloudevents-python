import os
from setuptools import find_packages, setup

release_status = "Development Status :: 3 - Alpha"

package_root = os.path.abspath(os.path.dirname(__file__))
readme_filename = os.path.join(package_root, "README.md")
with open(readme_filename, encoding="utf-8") as readme_file:
    readme = readme_file.read()

setup(
    name="google-events",
    version = "0.1.2",
    description="A collection of first party Google Cloud Platform event objects.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/googleapis/google-cloudevents",
    project_urls={
        "Source": "https://github.com/googleapis/google-cloudevents-python",
        "Documentation": "https://github.com/googleapis/google-cloudevents-python",
        "Issue Tracker": "https://github.com/googleapis/google-cloudevents-python/issues",
    },
    license="Apache License 2.0",
    author="Google LLC",
    author_email="googleapis-packages@google.com",
    classifiers=[
        release_status,
        "Environment :: Web Environment",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Internet",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=find_packages("src"),
    package_dir={"": "src"},
    python_requires=">=3.7",
    install_requires=['python-dateutil==2.8.1'],
    extras_require={"dev": ["pylint", "pytest", "black", "stringcase"]}
)
