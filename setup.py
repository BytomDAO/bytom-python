import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pybtm",
    version="0.1.8",
    author="zcc0721",
    author_email="zcc0721@foxmail.com",
    description="Python3 implementation of the Bytom protocol.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Bytom/pybtm",
    packages=setuptools.find_packages(),
    install_requires=[
        "ed25519>=1.4",
        "pbkdf2>=1.3",
        "pybase64>=0.5.0",
        "qrcode>=6.1",
        "sha3>=0.2.1",
        "six>=1.12.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)