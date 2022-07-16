class ApiAdapter:
    def __init__(self):
        pass

    def setApiKey(self, api_key):
        self.api_key = api_key

    def setUrl(self, url):
        self.url = url

    def getApiKey(self):
        return self.api_key

    def getUrl(self):
        return self.url
