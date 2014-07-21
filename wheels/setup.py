import os

from setuptools import setup

setup(
    name='mypackage',
    version='0.0.1',
    description='Sample Python package.',
    long_description=('Long description of mypackage'),
    url='http://github.com/obulpathi/python/',
    license='MIT',
    author='Obulapathi N Challa',
    author_email='obulpathi@gmail.com',
    py_modules=['mypackage'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
