import requests
from adapters.ApiAdapter import ApiAdapter
from . import DeepAiApi


class NeuralStyleApi(DeepAiApi.DeepAiApi):
    def __init__(self, api_adapter):
        super().__init__(api_adapter)

    def post(self, image_path, style_path):
        headers = {'api-key': self.api_key}
        response = requests.post(
            self.url,
            files={
                'style': open(style_path, 'rb'),
                'content': open(image_path, 'rb'),
            },
            headers=headers
        )
        return response.json()
