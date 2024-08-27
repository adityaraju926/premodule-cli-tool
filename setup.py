from setuptools import setup, find_packages

setup(
    name='replace-nulls-cli-tool',
    version='0.1',
    py_modules=['replace_nulls'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'replace-nulls-cli-tool = replace_nulls:main',
        ],
    },
)