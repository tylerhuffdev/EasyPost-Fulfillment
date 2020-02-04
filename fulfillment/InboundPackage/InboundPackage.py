import fulfillment.core
import fulfillment.ASN

base_url = 'advanced_shipment_notices/'
ip_url = '/inbound_packages/'


# inbound package functions to send to core
def create(asn, **data):
    url = fulfillment.core.base_url + base_url + asn + ip_url
    fulfillment.core.Resource.create(url, data)


def retrieve(asn_url, url):
    url = fulfillment.core.base_url + base_url + asn_url + ip_url + url
    fulfillment.core.Resource.retrieve(url)


def retrieveAll(asn_url, options):
    url = fulfillment.core.base_url + base_url + asn_url + ip_url
    fulfillment.core.Resource.retrieve(url, options)


def update(asn_url, url, **data):
    url = fulfillment.core.base_url + base_url + asn_url + ip_url + url
    fulfillment.core.Resource.update(url, data)


def delete(asn_url, url):
    url = fulfillment.core.base_url + base_url + asn_url + ip_url + url
    fulfillment.core.Resource.delete(url)
