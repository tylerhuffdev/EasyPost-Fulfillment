import fulfillment

fulfillment.core.api_key = 'YOUR_API_KEY_GOES_HERE'
# set debug to true to get print json
fulfillment.core.Debug = True

fulfillment.OrderReturn.create(
    'order_123456789abcdefghijklmnopqrstuvwxyz',
    line_items=[
        {
            'product_id': 'prod_123456789abcdefghijklmnopqrstuvwxyz',
            'units': 20,
            'reason_type': 'wrong_size'
        }
    ]
)

fulfillment.OrderReturn.retrieve('return_123456789abcdefghijklmnopqrstuvwxyz')

fulfillment.Product.retrieveAll(
    options={
        'limit': 3,
        'offset': 0,
        'page': 0,
        'per_page': 2
    }
)

fulfillment.OrderReturn.delete('return_123456789abcdefghijklmnopqrstuvwxyz')
