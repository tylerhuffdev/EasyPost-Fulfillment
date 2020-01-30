import fulfillment

fulfillment.core.api_key = 'YOUR_API_KEY_GOES_HERE'
# set debug to true to get print json
fulfillment.core.Debug = True

fulfillment.ASN.create(
    warehouse_id='wh_123456789abcdefghijklmnopqrstuvwxyz',
    comments='packed in bubble wrap'
)

fulfillment.ASN.retrieve('asn_123456789abcdefghijklmnopqrstuvwxyz')

fulfillment.Product.retrieveAll(
    options={
        'limit': 3,
        'offset': 0,
        'page': 0,
        'per_page': 2
    }
)

fulfillment.ASN.update(
    'asn_123456789abcdefghijklmnopqrstuvwxyz',
    comments='extra packing included'
)

fulfillment.ASN.delete('asn_123456789abcdefghijklmnopqrstuvwxyz')
