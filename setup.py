# -*- coding: utf-8 -*-
import re
from setuptools import setup
from setuptools import find_packages


DESCRIPTION = "Python client for the https://api.radio-browser.info"


def get_version():
    content = open("pyradios/__init__.py").read()
    mo = re.search(r"[0-9]+, [0-9]+, [0-9]+", content)
    if not mo:
        raise RuntimeError(
                'Unable to find version string in pyradios/__init__.py'
            )
    return mo.group(0).replace(', ', '.')


def readme():
    with open("README.md") as f:
        return f.read()


def required():
    with open("requirements.txt") as f:
        return f.read().splitlines()


setup(
    name="pyradios",
    version=get_version(),
    description=DESCRIPTION,
    long_description=readme(),
    long_description_content_type="text/markdown",
    keywords="pyradios wrapper radios api",
    author="André P. Santos",
    author_email="andreztz@gmail.com",
    url="https://github.com/andreztz/pyradios",
    license="MIT",
    packages=find_packages(),
    install_requires=required(),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
    ],
    python_requires=">=3.6",
    project_urls={
        "Source": "https://github.com/andreztz/pyradios/",
        "Upstream": "https://api.radio-browser.info/",
    },
)
