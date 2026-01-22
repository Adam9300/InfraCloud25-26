import requests
import json

access_token = 'ZjczMDE4NTMtODU1Ni00NDA2LTg2M2EtYWYzNzAwZWIwNDgxYmRlMDUzZjctMzYw_P0A1_cce0a1f3-bf77-42c7-a45d-46ec83d996ea'
person_id = 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS9jNTI4NTZmYi00NTBhLTQxMzEtODBjOS02YjE0YzVhYTRiODg'
url = 'https://webexapis.com/v1/people/{}'.format(person_id)
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))