import requests

access_token = 'ZjczMDE4NTMtODU1Ni00NDA2LTg2M2EtYWYzNzAwZWIwNDgxYmRlMDUzZjctMzYw_P0A1_cce0a1f3-bf77-42c7-a45d-46ec83d996ea'
room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL1JPT00vZDg4NTc5MTAtZWIxMi0xMWYwLWIxYWMtM2RhN2VmNGMzNzBm'
url = 'https://webexapis.com/v1/rooms/{}/meetingInfo'.format(room_id)
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
res = requests.get(url, headers=headers)
print(res.json())
