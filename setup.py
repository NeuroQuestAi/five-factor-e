"""The package settings."""

import codecs
import os

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = "0.0.1"
DESCRIPTION = "Big 5 Personality Traits"
LONG_DESCRIPTION = "Library with a self-administered questionnaire that assesses a person's personality according to the Big Five model, using the IPIP-NEO."

setup(
    name="five-factor-e",
    version=VERSION,
    author="Ederson Corbari and Marcos Ferretti, Neural-7",
    author_email="<e@neural7.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=[
        "python",
        "IPIP-NEO",
        "IPIP-NEO-PI",
        "NEO-PI-R",
        "IPIP",
        "big5",
        "big five",
        "five factor",
        "personality",
        "traits",
        "facet",
        "assessment",
        "psychometrics",
        "personality quiz",
        "inventory",
        "HR tests",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
