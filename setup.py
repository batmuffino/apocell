#!/usr/bin/python
# -*- coding: latin-1 -*-

import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__),fname)).read()

setup(
    name = "apocell_project/",
    version = "1.0.0",
    author = u"Jan-Hendrik Trösemeier, Sabine Klawitter, Gerald Schumann",
    author_email = "jan-hendrik.troesemeier@pei.de",
    description= ("Post-processing for apobec collocation data from cellprofiler"),
    packages = ["apocell_project"],
    url = "www.pei.de",
    classifiers=[
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)"]
)
