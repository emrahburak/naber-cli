
from setuptools import setup, find_packages



setup(
    name='naber',
    version = '1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'dataset'
        ],

    entry_points='''
    [console_scripts]
    naber=naber.scripts.naber:cli
    ''',

    )
