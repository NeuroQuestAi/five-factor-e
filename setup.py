"""The package settings."""

import codecs
import os

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = "1.1.0"
DESCRIPTION = "Big 5 IPIP-NEO Personality Traits"
LONG_DESCRIPTION = "Library with a self-administered questionnaire that assesses a person's personality according to the Big Five model, using the IPIP-NEO."

setup(
    name="five-factor-e",
    version=VERSION,
    author="Ederson Corbari and Marcos Ferretti, Neural7",
    author_email="<e@neural7.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=[
        "IPIP-NEO",
        "Big-5",
        "Five-Factor",
        "Personality",
        "Assessment",
        "Psychometrics",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
