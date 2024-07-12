from setuptools import setup, find_packages

setup(
    name="cloudns_sdk",
    version="0.1.0",
    description="A Python SDK for the ClouDNS API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Komal Paudyal",
    author_email="komal.paudyal@icloud.com",
    url="https://github.com/lively-ops/cloudns_sdk",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)