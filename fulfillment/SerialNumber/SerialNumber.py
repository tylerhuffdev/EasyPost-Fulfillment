import fulfillment.core
import fulfillment.Product

base_url = '/serial_numbers/'


# serial number functions to send to core
def create(product_id, value):
    url = fulfillment.core.base_url + fulfillment.Product.base_url + product_id + base_url
    fulfillment.core.Resource.create(url, value)
