
from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='testpackageschon',
    version='0.0.8',    
    description='A simple Python package.',
    url='',
    author='Kushagra Tiwari',
    author_email='kush0984@gmail.com',
    license='MIT',
    packages=['testpackageschon'],
    install_requires=required,
    package_data={'': ['testpackage/*.json']},
    include_package_data=True,
)