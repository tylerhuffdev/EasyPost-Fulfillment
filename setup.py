from setuptools import setup

setup(
    name='EasyPost-Fulfillment',
    version='1.0',
    packages=[
        'fulfillment',
        'fulfillment.ASN',
        'fulfillment.core',
        'fulfillment.Order',
        'fulfillment.Product',
        'fulfillment.Inventory',
        'fulfillment.Warehouse',
        'fulfillment.OrderReturn',
        'fulfillment.SerialNumber',
        'fulfillment.InboundPackage'
              ],
    url='',
    license='MIT License',
    author='Tyler Huff',
    author_email='support@easypost.com',
    description='EasyPost Fulfillment Client Library',
    install_requires=['requests']
)
