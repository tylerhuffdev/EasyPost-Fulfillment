import fulfillment.core

base_url = 'orders/'

# order functions to send to core
def create(service, destination, line_items):
    url = fulfillment.core.base_url + base_url
    data = {
        'service': service,
        'destination': destination,
        'line_items': line_items
        }
    fulfillment.core.Resource.create(url, data)

def retrieve(order_id):
    url = fulfillment.core.base_url + base_url + order_id
    fulfillment.core.Resource.retrieve(url)

def retrieveAll(options):
    url = fulfillment.core.base_url + base_url
    fulfillment.core.Resource.retrieve(url, options)

def update(order_id, **data):
    url = fulfillment.core.base_url + base_url + order_id
    fulfillment.core.Resource.update(url, data)

def delete(order_id):
    url = fulfillment.core.base_url + base_url + order_id
    fulfillment.core.Resource.delete(url)
