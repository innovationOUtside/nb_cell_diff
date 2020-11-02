from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="nbcelldiff",
    author="Tony Hirst",
    author_email="tony.hirst@open.ac.uk",
    description="Tools for finding the difference between two notebook code cells",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=['nbcelldiff'],
    package_data = {},
    include_package_data=False,
    install_requires=[],
)