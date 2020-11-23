#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from setuptools import setup

exec(compile(open("tchurn/version.py").read(), "tchurn/version.py", "exec"))

readme_path = os.path.join(os.path.dirname(__file__), "README.md")


long_description = open(readme_path).read()

setup(
    name="tchurn",
    version=__version__,
    description="",
    packages=["tchurn", "tchurn.datasets"],
    license="MIT",
    keywords="customer lifetime value, clv, ltv, BG/NBD, pareto/NBD, frequency, recency",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
    ],
    install_requires=["numpy>=1.10.0", "scipy>=1.0.0", "pandas>=0.24.0", "autograd>=1.2.0", "dill>=0.2.6"],
    package_data={
        "tchurn": ["datasets/*", "../README.md", "../README.txt", "../LICENSE", "../MANIFEST.in", "fitters/*"]
    },
)
