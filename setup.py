# /usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='py3-bencode',
    version='0.0.2',
    description="Python 3 bencoding implementation",
    long_description=open('README.md', 'r').read().strip(),
    classifiers=["Programming Language :: Python"],
    keywords='',
    author='D.Bashkirtsevich',
    author_email='bashkirtsevich@gmail.com',
    url='https://github.com/bashkirtsevich/py3bencode',
    license='GPL3 License',
    py_modules=['bencode'],
    include_package_data=True,
    zip_safe=True,
    packages=find_packages('src'),
    package_dir={'': 'src'},
)
