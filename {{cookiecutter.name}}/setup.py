#!/usr/bin/python
# -*- coding: UTF-8 -*-
from setuptools import setup
from pip.req import parse_requirements
from pip.exceptions import InstallationError

from {{cookiecutter.package}}.version import get_version

try:
    install_reqs = list(parse_requirements("requirements.txt", session={}))
except InstallationError:
    # There are no requirements
    install_reqs = []

setup(name="{{cookiecutter.package}}",
      version=get_version(),
      description="{{cookiecutter.short_desc}}",
      author="{{cookiecutter.author}}",
      author_email="{{cookiecutter.author_email}}",
      packages=["{{cookiecutter.package}}"],
      install_requires=[str(ir.req) for ir in install_reqs],
      test_suite="pytest",
      tests_require=["pytest", "pytest-cov"],
      setup_requires=["pytest-runner"]
      )
