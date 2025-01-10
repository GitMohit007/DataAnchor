from setuptools import setup, find_packages
import os

# Read the contents of your README file
with open(os.path.join(os.path.dirname(__file__), 'README.md')) as f:
    readme = f.read()
setup(
    name="DataAnchor",
    version="0.0.5",
    author="Mohit Krishna Kanojia",
    author_email="mohitkrishna010@gmail.com",
    url="https://github.com/GitMohit007/DataAnchor",
    packages=find_packages(),
    python_requires='>=3.8',
    long_description=readme,
    long_description_content_type='text/markdown',
)