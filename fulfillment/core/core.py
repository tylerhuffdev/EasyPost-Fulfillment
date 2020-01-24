import requests
import json
from requests.auth import HTTPBasicAuth
from dataclasses import dataclass

# easypost api url and headers
base_url = 'https://api.easypost.com/fulfillment/vendor/v2/'
Headers = {'User-Agent': 'EP Fulfillment Python CL',
           'Content-Type': 'application/json'}


@dataclass(frozen=True)
class Debug:
    debug: bool


def debug(response):
    if Debug == True:
        print(response.json())
    else:
        pass


# stores user's api key
@dataclass
class api_key:
    api_key: str


# http methods for api
class Resource(api_key):

    # http post
    @classmethod
    def create(cls, url, data):
        requestor = api_key
        url = url
        result = json.dumps(data)
        response = requests.post(
            url,
            result,
            headers=Headers,
            auth=HTTPBasicAuth(requestor, '')
            )
        debug(response)
        return response

    # http get
    @classmethod
    def retrieve(cls, url, options=None):
        requestor = api_key
        url = url
        response = requests.get(
            url,
            options,
            headers=Headers,
            auth=HTTPBasicAuth(requestor, '')
            )
        debug(response)
        return response

    # http patch
    @classmethod
    def update(cls, url, data):
        requestor = api_key
        url = url
        result = json.dumps(data)
        response = requests.patch(
            url,
            result,
            headers=Headers,
            auth=HTTPBasicAuth(requestor, '')
            )
        debug(response)
        return response

    # http delete
    @classmethod
    def delete(cls, url):
        requestor = api_key
        url = url
        response = requests.delete(
            url,
            headers=Headers,
            auth=HTTPBasicAuth(requestor, '')
            )
        debug(response)
        return response
