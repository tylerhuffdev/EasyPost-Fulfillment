from setuptools import setup, find_packages

setup(
    name='fulfillment',
    version='1.0',
    packages=find_packages(),
    namespace_packages=['EPFulfillment'],
    url='',
    license='MIT License',
    author='Tyler Huff',
    author_email='support@easypost.com',
    description='EasyPost Fulfillment Client Library',
    install_requires=['requests']
)
