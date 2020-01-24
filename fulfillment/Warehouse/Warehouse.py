import fulfillment.core

base_url = 'warehouses/'


# warehouse function to send to core
def retrieveALL():
    url = fulfillment.core.base_url + base_url
    fulfillment.core.Resource.retrieve(url)
