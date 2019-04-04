"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='maestro',
    version='0.1.0',
    description="A project that controls Pololu's Maestro servo controller over USB serial",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/m4reko/maestro',
    author='Steven L. Jacobs',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: System :: Hardware',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='polulu servo',
    py_modules=["maestro"],
    python_requires='>=3.4, <4',
    install_requires=['pyserial'],
    project_urls={
        'Forked repo': 'https://github.com/FRC4564/Maestro/',
    },
)
