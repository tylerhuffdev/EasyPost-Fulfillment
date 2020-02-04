import fulfillment.core

base_url = 'advanced_shipment_notices/'


# ASN functions to send to core
def create(**data):
    url = fulfillment.core.base_url + base_url
    fulfillment.core.Resource.create(url, data)


def retrieve(id):
    asn_url = fulfillment.core.base_url + base_url + str(id)
    fulfillment.core.Resource.retrieve(asn_url)


def retrieveAll(options):
    url = fulfillment.core.base_url + base_url
    fulfillment.core.Resource.retrieve(url, options)


def update(id, **data):
    asn_url = fulfillment.core.base_url + base_url + str(id)
    fulfillment.core.Resource.update(asn_url, data)


def delete(id):
    asn_url = fulfillment.core.base_url + base_url + str(id)
    fulfillment.core.Resource.delete(asn_url)
