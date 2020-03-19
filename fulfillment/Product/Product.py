import fulfillment.core

base_url = 'products/'

# product functions to send to core
def create(**data):
    url = fulfillment.core.base_url + base_url
    fulfillment.core.Resource.create(url, data)

def retrieve(id):
    prod_url = fulfillment.core.base_url + base_url + str(id)
    fulfillment.core.Resource.retrieve(prod_url)

def retrieveAll(options):
    url = fulfillment.core.base_url + base_url
    fulfillment.core.Resource.retrieve(url, options)

def update(id, **data):
    prod_url = fulfillment.core.base_url + base_url + str(id)
    fulfillment.core.Resource.update(prod_url, data)

def delete(id):
    prod_url = fulfillment.core.base_url + base_url + str(id)
    fulfillment.core.Resource.delete(prod_url)
