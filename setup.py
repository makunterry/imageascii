from setuptools import setup, find_packages

setup(
    name="imageascii",
    version="1.0dev",
    description="A simple tool to generate ASCII images",
    author="Kun Ma",
    author_email=', '.join([
        "makunterry@163.com"]),
    url="http://unspecified.yet",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
	    'imageascii = src.cmd.imageascii:main'
        ]
    },
)
