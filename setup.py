from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = []

setup(
    name="gpushare",
    version="0.0.1",
    author="Shresth Verma",
    author_email="vermashresth@gmail.com",
    description="A package to declare, manage and analyse shared GPU resources within a team",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/vermashresth/gpu-share",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: MIT",
    ],
)
