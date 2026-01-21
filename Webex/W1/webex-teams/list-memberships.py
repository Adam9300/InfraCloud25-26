import requests
access_token = 'MjVlYzc2OTktYTc4NS00YWI4LTg4ZmItNGM0MWMxMTA0Y2JiZjkzMGNjMGUtMDUy_PE93_c1d5175a-94c8-42b4-8597-8085a0c21335'
room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL1JPT00vZDg4NTc5MTAtZWIxMi0xMWYwLWIxYWMtM2RhN2VmNGMzNzBm'
url = 'https://webexapis.com/v1/memberships'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {'roomId': room_id}
res = requests.get(url, headers=headers, params=params)
print(res.json())