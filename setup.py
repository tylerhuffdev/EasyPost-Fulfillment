from setuptools import setup, find_packages

setup(
    name='fulfillment',
    version='1.0',
    packages=find_packages(exclude=[
        'tests',
        'examples'
    ]),
    url='',
    license='MIT License',
    author='Tyler Huff',
    author_email='support@easypost.com',
    description='EasyPost Fulfillment Python Client Library',
    install_requires=['requests']
)
