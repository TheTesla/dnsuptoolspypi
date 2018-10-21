#!/usr/bin/env python

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dnsuptools",
    version="0.0.5",
    author="Stefan Helmert",
    author_email="stefan.helmert@t-online.de",
    description="Library interfaces to dns service api for query, update, add, delete comfortably.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TheTesla/dnsuptoolspypi",
    packages=setuptools.find_packages(),
    install_requires=[
        "simpleloggerplus",
        "dnspython",
        "pycurl"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

