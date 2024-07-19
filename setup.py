"""The package settings."""

import codecs
import os

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = "1.12.0"
DESCRIPTION = "Big 5 IPIP-NEO Personality Traits"
LONG_DESCRIPTION = "Library with a self-administered questionnaire that assesses a person's personality according to the Big Five Model, using the IPIP-NEO."

setup(
    name="five-factor-e",
    version=VERSION,
    author="Ederson Corbari, NeuroQuest AI",
    author_email="<e@NeuroQuest.ai>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(exclude=("test",)),
    python_requires=">=3.10",
    include_package_data=True,
    install_requires=[],
    extras_require={"quiz": ["plotext"]},
    entry_points={
        "console_scripts": [
            "ipipneo-quiz = ipipneo.quiz:main",
        ],
    },
    keywords=[
        "IPIP",
        "IPIP-NEO",
        "Big-5",
        "Big-Five",
        "Five-Factor",
        "Personality",
        "Assessment",
        "Psychometrics",
        "Personality-Insights",
        "People-Analytics",
        "Python",
    ],
    classifiers=[
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
