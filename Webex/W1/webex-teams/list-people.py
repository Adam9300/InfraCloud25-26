import requests
import json

access_token = 'MjVlYzc2OTktYTc4NS00YWI4LTg4ZmItNGM0MWMxMTA0Y2JiZjkzMGNjMGUtMDUy_PE93_c1d5175a-94c8-42b4-8597-8085a0c21335'
person_id = 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS9jNTI4NTZmYi00NTBhLTQxMzEtODBjOS02YjE0YzVhYTRiODg'
url = 'https://webexapis.com/v1/people/{}'.format(person_id)
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))