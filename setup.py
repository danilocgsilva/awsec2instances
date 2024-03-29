from setuptools import setup, find_packages

VERSION = '1.12.3'

def readme():
    with open("README.md") as f:
        return f.read()

setup(
    name="awsec2instances",
    version=VERSION,
    description="Wrapper around the aws command line",
    long_description_content_type="text/markdown",
    long_description=readme(),
    keywords="aws ec2 list command line",
    url="https://github.com/danilocgsilva/awsec2instances",
    author="Danilo Silva",
    author_email="contact@danilocgsilva.me",
    packages=[
        "awsec2instances_includes",
        "awsec2instances_includes.OsScriptService"
    ],
    entry_points={"console_scripts": ["awsec2=awsec2instances_includes.__main__:main"],},
    include_package_data=True
)
