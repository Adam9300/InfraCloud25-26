import requests
access_token = 'ZjczMDE4NTMtODU1Ni00NDA2LTg2M2EtYWYzNzAwZWIwNDgxYmRlMDUzZjctMzYw_P0A1_cce0a1f3-bf77-42c7-a45d-46ec83d996ea'
url = 'https://webexapis.com/v1/rooms'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params={'title': 'DevNet Associate Training!'}
res = requests.post(url, headers=headers, json=params)
print(res.json())