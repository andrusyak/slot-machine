import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="slot-machine",
    version="0.0.5",
    author="Ruslan Andrusyak",
    description="Slot Machine Simulator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/andrusyak/slot-machine.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "matplotlib",
    ],
)
