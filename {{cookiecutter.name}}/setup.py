#!/usr/bin/python
# -*- coding: UTF-8 -*-
from setuptools import setup

from {{cookiecutter.package}}.version import get_version

setup(name="{{cookiecutter.package}}",
      version=get_version(),
      description="{{cookiecutter.short_desc}}",
      author="{{cookiecutter.author}}",
      author_email="{{cookiecutter.author_email}}",
      packages=["{{cookiecutter.package}}"],
      install_requires=[
          "oshino>=0.1.0"
      ],
      test_suite="pytest",
      tests_require=["pytest", "pytest-cov"],
      setup_requires=["pytest-runner"]
      )
