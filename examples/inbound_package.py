import fulfillment

fulfillment.core.api_key = 'YOUR_API_KEY_GOES_HERE'
# set debug to true to get print json
fulfillment.core.Debug = True

fulfillment.InboundPackage.create(
    'asn_123456789abcdefghijklmnopqrstuvwxyz',
    tracking_code='123456789ABCDEF',
    name='A1A',
    line_items={
        'product': {'id': 'prod_123456789abcdefghijklmnopqrstuvwxyz'},
        'units': 20
    }
)

fulfillment.InboundPackage.retrieve(
    'asn_123456789abcdefghijklmnopqrstuvwxyz',
    'inb_123456789abcdefghijklmnopqrstuvwxyz'
)

fulfillment.Product.retrieveAll(
    options={
        'limit': 3,
        'offset': 0,
        'page': 0,
        'per_page': 2
    }
)

fulfillment.InboundPackage.update(
    comment='fragile',
    tracking_code='987654321ABCDEF'
)

fulfillment.InboundPackage.delete(
    'asn_123456789abcdefghijklmnopqrstuvwxyz',
    'inb_123456789abcdefghijklmnopqrstuvwxyz'
)
