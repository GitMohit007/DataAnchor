from setuptools import setup, find_packages

setup(
    name="data-anchor",
    version="1.0.0",
    description="A Python library for shared memory synchronization with dataclasses.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="GitMohit007",
    author_email="your_email@example.com",
    url="https://github.com/GitMohit007/DataAnchor",
    packages=find_packages(),
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Distributed Computing",
    ],
    license="MIT",
    keywords="shared-memory ipc dataclasses python",
    install_requires=[],
    extras_require={
        "dev": ["pytest", "black", "mypy"],  # Optional: development tools
    },
    include_package_data=True,
    zip_safe=False,
)
