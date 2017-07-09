import os

from setuptools import find_packages, setup

import interpreters

setup(
    name='interpreters',
    version=interpreters.__version__,
    packages=find_packages(),
    test_suite='tests',
    # long_description=open(join(dirname(__file__), 'README.txt')).read(),
    # entry_points={
    #     'console_scripts':
    #         ['inter = inter.core:print_message']
    #     }
    # )
)
