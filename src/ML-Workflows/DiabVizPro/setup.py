from setuptools import setup, find_packages

setup(
    name="diabvizpro",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "matplotlib",
        "seaborn",
    ],
    author="Ihr Name",
    author_email="ihre.email@domain.com",
    description="DiabVizPro - Diabetes Data Visualization Tool",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
