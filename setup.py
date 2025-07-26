# File: setup.py
from setuptools import setup, find_packages

setup(
    name="cognize",
    version="0.1.0",
    description="Epistemic rupture detection and control system powered by RCC",
    author="Pulikanti Sashi Bharadwaj",
    author_email="bharadwajpulikanti11@gmail.com",
    url="https://github.com/heraclitus0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "requests",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
