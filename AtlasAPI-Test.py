import requests
import json
from requests.structures import CaseInsensitiveDict


#from atlasclient.client import ENTRY_POINTS
'''
Use this for swagger testing
https://atlas.apache.org/api/v2/ui/index.html
'''

'''
 Get the bearer Token
'''
url = "https://login.microsoftonline.com/72f988bf-86f1-41af-91ab-2d7cd011db47/oauth2/token"
client_id = "23443326-7c07-4c96-a34c-0d84bc9aa2b2"
client_secret = "9e.GH~jL5Z1~.dRW8A8M67uPo-0Ps_16u~"

myobj = {'grant_type': 'client_credentials',
         'client_id' : '23443326-7c07-4c96-a34c-0d84bc9aa2b2',
         'client_secret':'9e.GH~jL5Z1~.dRW8A8M67uPo-0Ps_16u~',
         'resource':'73c2949e-da2d-457a-9607-fcc665198967'
        }

#resource = "73c2949e-da2d-457a-9607-fcc665198967"

auth = requests.post(url,myobj)
bearer_token = auth.json()["access_token"]
#print(bearer_token)

'''
 calling the atlas api-using the http calls
'''

atlas_url = "https://e12-purview-e12.catalog.purview.azure.com/api/atlas/v2/types/typedefs"


headers = CaseInsensitiveDict()

#headers["Accept"] = "application/json"
#headers["Authorization"] = "Token "+bearer_token


headers= {"Authorization": "Bearer " + bearer_token,
          "Content-Type": "application/json"
          }

print(headers)
parameters = {}

resp = requests.get(atlas_url,params= parameters,headers= headers)
print(resp)
results = json.loads(resp.text)
#print(results)

'''
 calling the search atlas api-using the http calls
'''

atlas_url = "https://e12-purview-e12.catalog.purview.azure.com/api/atlas/v2/search/advanced"


headers = CaseInsensitiveDict()

#headers["Accept"] = "application/json"
#headers["Authorization"] = "Token "+bearer_token


headers= {"Authorization": "Bearer " + bearer_token,
          "Content-Type": "application/json"
          }

print(headers)

parameters = {'keywords':'sales',
              'limit':2,
              'offset':1
              }

resp = requests.post(atlas_url,json=parameters,headers=headers)
print(resp)
results = json.loads(resp.text)
print(results)