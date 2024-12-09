
from setuptools import setup, find_packages

setup(
    name='energylink',
    version='4.0',
    description='EnergyLink: Open Source Energy Data Exchange and DERMS',
    author='Your Name',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'boto3',
        'azure-storage-blob',
        'google-cloud-storage',
        'databricks-sql-connector',
        'dbt',
        'snowflake-connector-python',
        'streamlit',
        'fastapi',
        'requests',
        'jira',
        'sklearn',
        'web3'
    ],
)
    