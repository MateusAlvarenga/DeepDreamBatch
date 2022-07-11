import requests

class DeepDreamApi:
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = "https://api.deepai.org/api/deepdream"

    def post(self, image_path):
        files = {'image': open(image_path, 'rb')}
        headers = {'api-key': self.api_key}
        r = requests.post(self.url, files=files, headers=headers)
        return r.json()