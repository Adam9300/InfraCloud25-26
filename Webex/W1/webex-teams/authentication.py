import requests
import json

access_token = 'MjVlYzc2OTktYTc4NS00YWI4LTg4ZmItNGM0MWMxMTA0Y2JiZjkzMGNjMGUtMDUy_PE93_c1d5175a-94c8-42b4-8597-8085a0c21335'
url = 'https://webexapis.com/v1/people/me'
headers = {'Authorization': 'Bearer {}'.format(access_token)}
res = requests.get(url, headers=headers)

print(json.dumps(res.json(), indent=4))