import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="generic_validation",
    version="0.0.7",
    author="D Reschner",
    author_email="git@simphotonics.com",
    description="Generic validation decorators.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/simphotonics/generic_validation",
    project_urls={
        "Bug Tracker": "https://github.com/simphotonics/generic_validation/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
