from setuptools import setup, find_packages

setup(
    name='thesaurus',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'requests',
        'inquirer',
        'textual'
    ],
    entry_points={
        'console_scripts': [
            'thesaurus = thesaurus.scripts.thesaurus:cli',
            'th = thesaurus.scripts.thesaurus:cli'
        ],
    },
)