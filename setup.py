from setuptools import find_packages, setup

setup(
    name='reshape',
    packages=find_packages(include=['src']),
    version='0.1.0',
    description='A Python helper library for applications using Reshape',
    author='Fabian Lindfors',
    license='MIT',
    install_requires=["natsort", "toml"],
)