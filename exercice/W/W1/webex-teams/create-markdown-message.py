import requests

access_token = 'ZjczMDE4NTMtODU1Ni00NDA2LTg2M2EtYWYzNzAwZWIwNDgxYmRlMDUzZjctMzYw_P0A1_cce0a1f3-bf77-42c7-a45d-46ec83d996ea'
room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL1JPT00vZDg4NTc5MTAtZWIxMi0xMWYwLWIxYWMtM2RhN2VmNGMzNzBm'
message = 'Hello **DevNet Associates**!!'
url = 'https://webexapis.com/v1/messages'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {'roomId': room_id, 'markdown': message}
res = requests.post(url, headers=headers, json=params)
print(res.json())


