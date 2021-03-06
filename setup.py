import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="packmol_wrapper",
    version="0.1.0",
    author="Alyssa Travitz",
    author_email="atravitz@umich.edu",
    description="A python Packmol wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/atravitz/PackmolWrapper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)