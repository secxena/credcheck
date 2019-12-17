import os

rootdir = os.path.abspath(os.path.dirname(__file__))
__name__ = "credcheck"
__version__ = open(os.path.join(rootdir, "VERSION")).read().strip()
__description__ = "Credential check and validation framework"
__long_description__ = open(os.path.join(rootdir, "README.md")).read()
__author__ = "Apoorv Raj Saxena"
__author_email__ = "saxena.apoorvraj@gmail.com"
