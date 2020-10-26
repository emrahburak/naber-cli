
from setuptools import setup, find_packages



setup(
    name='naber',
    version = '1.0',
    author = 'Emrah Burak Gurbuz',
    author_email = 'gemrahburak@gmail.com',
    py_modules=['naber'],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'dataset',
        'stuf'
        ],

    entry_points='''
    [console_scripts]
    naber=naber.scripts.naber:cli
    ''',

    )
