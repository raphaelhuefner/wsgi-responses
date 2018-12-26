# -*- coding: utf-8 -*-
"""Define the setup configuration of the wsgi_responses adapter library."""
from codecs import open
from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='wsgi_responses',
    version='0.0.1',
    description='The wsgi_responses adapter library',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/raphaelhuefner/wsgi-responses',
    author='Raphael Huefner',
    author_email='raphaelhuefner@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
        'Natural Language :: English',
    ],
    keywords='wsgi responses adapter requests',
    packages=find_packages(exclude=['docs', 'tests']),
    python_requires='~=3.6',
    install_requires=[
        # 'requests',
        'responses',
    ],
    # setup_requires=['pytest-runner'],
    tests_require=[
        'pytest', 'pytest-isort', 'pytest-cov', 'coverage', 'isort', 'yapf',
        'flake8', 'pycodestyle',
    ],
    extras_require={
        'deploy': ['twine', 'wheel'],
    },
    project_urls={
        'Bug Reports': 'https://github.com/raphaelhuefner/wsgi-responses/issues',
        'Source': 'https://github.com/raphaelhuefner/wsgi-responses',
    },
)
