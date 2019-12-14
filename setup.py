#!/usr/bin/env python
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
from metadata import (
    __name__, __version__, __long_description__, __description__,
    __author__, __author_email__
)


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        # import re
        # if(type(self.pytest_args) == 'str'):
        #     args = filter(lambda x: len(x) > 0, re.split(r'\s+', self.pytest_args))
        # else:
        #     args = self.pytest_args
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(
    name=__name__,
    packages=find_packages(),
    version=__version__,
    description=__description__,
    long_description=__long_description__,
    author=__author__,
    author_email=__author_email__,
    include_package_data=True,
    url="",
    install_requires=[
    ],
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "mock", "PyHamcrest", "pytest-runner"],
    cmdclass={'test': PyTest}
)
