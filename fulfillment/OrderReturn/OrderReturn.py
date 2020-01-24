import fulfillment.core

base_url = 'order_returns/'


# order return functions to send to core
def create(order_id, line_items):
    url = fulfillment.core.base_url + base_url
    data = {'order_id': order_id, 'line_items': line_items}
    fulfillment.core.Resource.create(url, data)


def retrieve(return_id):
    url = fulfillment.core.base_url + base_url + return_id
    fulfillment.core.Resource.retrieve(url)


def retrieveAll(options):
    url = fulfillment.core.base_url + base_url
    fulfillment.core.Resource.retrieve(url, options)


def delete(return_id):
    url = fulfillment.core.base_url + base_url + return_id
    fulfillment.core.Resource.delete(url)
