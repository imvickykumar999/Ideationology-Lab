from setuptools import setup

setup(
    name = 'firicks', # while installing pacakge, e.g., matplotlib...
    version = '0.0.1',
    description = 'Firebase Push and Pull Dictionary.',
    long_description = open('Readme.txt').read(),
    url = 'https://pypi.org/user/imvickykumar999/',
    author = 'Vicky Kumar',
    keywords = ['push', 'pull', 'firebase', 'dictionary'],
    packages = ['vicks'], # while importing package, e.g., pyplot...
)

# python setup.py sdist
# pip install twine
# twine upload dist/*
