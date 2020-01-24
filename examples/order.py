import fulfillment

fulfillment.core.api_key = 'YOUR_API_KEY_GOES_HERE'
# set debug to true to get print json
fulfillment.core.Debug = True

fulfillment.Order.create(
    service='standard',
    destination={
        'name': 'John Doe',
        'street1': '123 East 456 South',
        'street2': 'apartment 1',
        'city': 'San Francisco',
        'state': 'CA',
        'zip': '94131',
        'country': 'US',
        'residential': True
    },
    line_items=[
        {
            'product': {'id': 'prod_123456789abcdefghijklmnopqrstuvwxyz'},
            'units': 1
        }
    ]
)

fulfillment.Order.retrieve('order_123456789abcdefghijklmnopqrstuvwxyz')

fulfillment.Product.retrieveAll(
    options={
        'limit': 3,
        'offset': 0,
        'page': 0,
        'per_page': 2
    }
)

fulfillment.Order.update(
    'order_123456789abcdefghijklmnopqrstuvwxyz',
    destination={
        'name': 'Jane Doe'
    }
)

fulfillment.Order.delete('order_123456789abcdefghijklmnopqrstuvwxyz')
