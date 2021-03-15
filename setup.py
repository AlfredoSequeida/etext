from setuptools import setup, find_packages
import codecs
import re
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    with codecs.open(os.path.join(here, *parts), "r") as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M
    )
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


dynamic_version = find_version("etext", "__init__.py")

setup(
    name="etext",
    version=dynamic_version,
    author="Alfredo Sequeida",
    description="Send sms and mms text messages for free using email",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AlfredoSequeida/etext",
    download_url="https://github.com/AlfredoSequeida/etext/archive/"
    + dynamic_version
    + ".tar.gz",
    keywords=[
        "sms",
        "mms",
        "text",
        "text message",
        "phone notification",
        "email",
        "short message service",
        "multimedia messaging service",
    ],
    platforms="any",
    classifiers=[
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Operating System :: Microsoft :: Windows :: Windows 8",
        "Operating System :: Microsoft :: Windows :: Windows 8.1",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
    ],
    license="MIT",
    packages=["etext"],
    scripts=[
        "etext/exceptions.py",
        "etext/providers.py",
    ],
    python_requires=">=3.6",
)