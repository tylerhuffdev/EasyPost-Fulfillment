import fulfillment

fulfillment.core.api_key = 'YOUR_API_KEY_GOES_HERE'
# set debug to true to get print json
fulfillment.core.Debug = True

fulfillment.SerialNumber.create(
    'prod_123456789abcdefghijklmnopqrstuvwxyz',
    {'value': '123456789abcdefghijkl'}
)
