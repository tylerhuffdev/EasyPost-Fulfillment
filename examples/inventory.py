import fulfillment

fulfillment.core.api_key = 'YOUR_API_KEY_GOES_HERE'
# set debug to true to get print json
fulfillment.core.Debug = True

fulfillment.Inventory.retrieve(
    'prod_123456789abcdefghijklmnopqrstuvwxyz',
    'prod_123456789abcdefghijklmnopqrstuvwxyz'
)

fulfillment.Product.retrieveAll(
    options={
        'limit': 3,
        'offset': 0,
        'page': 0,
        'per_page': 2
    }
)
