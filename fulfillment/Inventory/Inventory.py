import fulfillment.core

base_url = 'inventories'
product = '?product_ids[]='
includes = '&includes[]='


# inventory functions to send to core
def retrieve(product_ids):
    url = fulfillment.core.base_url + base_url + product + product_ids + includes + 'product' + includes + 'warehouse'
    fulfillment.core.Resource.retrieve(url)


def retrieveAll(options):
    url = fulfillment.core.base_url + base_url
    fulfillment.core.Resource.retrieve(url, options)
