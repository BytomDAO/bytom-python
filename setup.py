import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pybtm",
    version="0.0.3",
    author="zcc0721",
    author_email="zcc0721@foxmail.com",
    description="Python3 implementation of the Bytom protocol.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Bytom/pybtm",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)