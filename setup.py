from setuptools import setup, find_packages
import os

# Function to extract the library version
def get_version():
    init_file = os.path.join("azure_pipelines_generator", "__init__.py")
    with open(init_file, "r") as f:
        for line in f:
            if line.startswith("__version__"):
                return line.split("=")[-1].strip().strip('"')

setup(
    name="azure-pipelines-generator",
    version=get_version(),
    description="A Python library to generate Azure Pipelines programmatically",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Emmanuel Osimosu",
    author_email="emmanuel.osimosu@scouth.com",
    url="https://github.com/scouth-com/azure-pipelines-generator",
    packages=find_packages(),
    install_requires=[
        "pyyaml>=6.0",
        "jsonschema>=4.23.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
