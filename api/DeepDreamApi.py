import requests
from adapters.ApiAdapter import ApiAdapter
from . import DeepAiApi


class DeepDreamApi(DeepAiApi.DeepAiApi):
    def __init__(self, api_adapter):
        super().__init__(api_adapter)

    def post(self, image_path):
        files = {'image': open(image_path, 'rb')}
        headers = {'api-key': self.api_key}
        r = requests.post(self.url, files=files, headers=headers)
        return r.json()
