import requests
import json

access_token = 'ZjczMDE4NTMtODU1Ni00NDA2LTg2M2EtYWYzNzAwZWIwNDgxYmRlMDUzZjctMzYw_P0A1_cce0a1f3-bf77-42c7-a45d-46ec83d996ea'
url = 'https://webexapis.com/v1/people/me'
headers = {'Authorization': 'Bearer {}'.format(access_token)}
res = requests.get(url, headers=headers)

print(json.dumps(res.json(), indent=4))