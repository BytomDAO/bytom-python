import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pybytom",
    version="0.0.1",
    author="zcc0721",
    author_email="zcc0721@foxmail.com",
    description="Python3 implementation of the Bytom protocol.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Bytom/pybytom",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
    ],
)