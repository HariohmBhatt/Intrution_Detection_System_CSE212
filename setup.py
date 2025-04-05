from setuptools import setup, find_packages
import os

# Read long description from README.md if it exists
try:
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()
except FileNotFoundError:
    long_description = """
    An IDS script that:
    1. Sniffs IP packets for 3-second intervals.
    2. Processes them as a batch.
    3. Logs how many were malicious vs. benign, and notifies if malicious are found.
    4. Prints/Logs the extracted features for each packet.
    5. Repeats indefinitely.
    """

setup(
    name="ids_core",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.19.0",
        "scapy>=2.4.5",
        "scikit-learn>=0.24.0",
        "pandas>=1.1.0",
    ],
    python_requires=">=3.6",
    author="Hariohm Bhatt",
    author_email="bhatthariohm2004@gmail.com",
    description="A Python-based Intrusion Detection System (IDS)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="cybersecurity, ids, intrusion detection, network security, machine learning, packet analysis",
    url="https://github.com/HariohmBhatt/ids-core",
    project_urls={
        "Source Code": "https://github.com/HariohmBhatt/ids-core",
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "Topic :: Security :: Intrusion Detection",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: POSIX :: Linux",
    ],
    include_package_data=True,
    package_data={
        "ids_core": ["NSL-KDD/*.pkl", "NSL-KDD/*.model"],
    },
    entry_points={
        "console_scripts": [
            "ids-core=ids_core.main:main",
        ],
    },
    zip_safe=False,
    platforms=["Linux"],
)