
from setuptools import setup
import os
import subprocess

def go_prep():
    env = dict(os.environ)
    env['GOPATH'] = os.path.dirname(os.path.abspath(__file__))

setup(
    name='pyagro',
    version='0.1.dev0',
    packages=[
        'pyagro'
    ],
    install_requires=["protobuf==3.0.0b1.post2", "grpcio==0.11.0b1"],
    license='Apache',
    long_description=open('README').read(),
)


