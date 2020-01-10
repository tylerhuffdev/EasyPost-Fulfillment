import requests, json
from requests.auth import HTTPBasicAuth
from dataclasses import dataclass


base_url = 'https://api.easypost.com/fulfillment/vendor/v2/'
Headers = {'User-Agent': 'EP Fulfillment Python CL',
            'Content-Type': 'application/json'}

@dataclass(frozen=True)
class api_key:
    api_key: str

class Resource(api_key):
    @classmethod
    def create(cls, api_key, url, data):
        requestor = api_key
        url = url
        result = json.dumps(data)
        response = requests.post(url, result, headers=Headers, auth=HTTPBasicAuth(requestor, ''))
        return response

    @classmethod
    def retrieve(cls, api_key, url):
        requestor = api_key
        url = url
        response = requests.get(url, headers=Headers, auth=HTTPBasicAuth(requestor, ''))
        product = response.json()
        print(product)
        return response

    @classmethod
    def update(cls, api_key, url, data):
        requestor = api_key
        url = url
        result = json.dumps(data)
        response = requests.patch(url, result, headers=Headers, auth=HTTPBasicAuth(requestor, ''))
        return response

    @classmethod
    def delete(cls, api_key, url):
        requestor = api_key
        url = url
        response = requests.delete(url, headers=Headers, auth=HTTPBasicAuth(requestor, ''))
        print(response)
        return response