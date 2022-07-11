import requests
import os
from dotenv import load_dotenv

from api.DeepDreamApi import DeepDreamApi

load_dotenv()

API_KEY =  os.getenv('API_KEY')
deepDreamApi = DeepDreamApi(API_KEY)


initial = 1
final = 36

for i in range(initial , final +1):
    file = {
        'image': open('./files/foo-' + str(i).zfill(3) + '.jpeg', 'rb'),
    }
    print(file)

# r = requests.post(
#     "https://api.deepai.org/api/deepdream",
#     files={
#         'image': open('./foo-001.jpeg', 'rb'),
#     },
#     headers={'api-key': '529d4b9a-03ff-4430-823a-6b201e6a9ad2'}
# )
# print(r.json())


# #Get the link or url
# url = 'https://www.facebook.com/favicon.ico'
# r = requests.get(url, allow_redirects=True)
# #Save the content with name.
# open('facebook.ico', 'wb').write(r.content)