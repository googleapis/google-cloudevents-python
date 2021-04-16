import os
import setuptools

# Disable version normalization performed by setuptools.setup()
try:
    # Try the approach of using sic(), added in setuptools 46.1.0
    from setuptools import sic
except ImportError:
    # Try the approach of replacing packaging.version.Version
    sic = lambda v: v
    try:
        # setuptools >=39.0.0 uses packaging from setuptools.extern
        from setuptools.extern import packaging
    except ImportError:
        # setuptools <39.0.0 uses packaging from pkg_resources.extern
        from pkg_resources.extern import packaging
    packaging.version.Version = packaging.version.LegacyVersion

release_status = "Development Status :: 3 - Alpha"

package_root = os.path.abspath(os.path.dirname(__file__))
readme_filename = os.path.join(package_root, "README.md")
with open(readme_filename, encoding="utf-8") as readme_file:
    readme = readme_file.read()

version = "0.1.3"

setuptools.setup(
    name="google-events",
    version = sic(version),
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
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    python_requires=">=3.7",
    install_requires=['python-dateutil==2.8.1'],
    extras_require={"dev": ["pylint", "pytest", "black", "stringcase"]}
)
