import fulfillment

fulfillment.core.api_key = 'YOUR_API_KEY_GOES_HERE'
# set debug to true to get print json
fulfillment.core.Debug = True

fulfillment.Product.create(
    title='example product',
    barcode='123456789',
    type='merchandise',
    origin_country='US',
    hs_code='1234.56.78',
    requires_serial_tracking=False,
    length={'value': 1},
    width={'value': 2},
    height={'value': 3},
    weight={'value': 4},
    price={'value': 5}
)

fulfillment.Product.retrieve('prod_123456789abcdefghijklmnopqrstuvwxyz')

fulfillment.Product.retrieveAll(
    options={
        'limit': 3,
        'offset': 0,
        'page': 0,
        'per_page': 2
    }
)

fulfillment.Product.update(
    'prod_123456789abcdefghijklmnopqrstuvwxyz',
    title='updated example product'
    )

fulfillment.Product.delete('prod_123456789abcdefghijklmnopqrstuvwxyz')
