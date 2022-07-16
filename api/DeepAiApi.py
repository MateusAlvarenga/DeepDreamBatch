import requests
from adapters.ApiAdapter import ApiAdapter


class DeepAiApi:
    def __init__(self, api_adapter):
        self.api_key = api_adapter.getApiKey()
        self.url = api_adapter.getUrl()
