from setuptools import setup, find_packages
setup(
    name='Hello_World',
    version='0.1.0',
    packages=find_packages(include=['exampleproject', 'exampleproject.*'])
)
