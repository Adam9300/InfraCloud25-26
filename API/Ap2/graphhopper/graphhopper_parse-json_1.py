import requests
import urllib.parse

geocode_url= "https://graphhopper.com/api/1/geocode?"
route_url= "https://graphhopper.com/api/1/route?"
loc1= "Rome, Italy"
loc2= "Baltimore, Maryland"
key= "7b8f5404-2694-4914-b1cb-2689548f0c94"

url= geocode_url + urllib.parse.urlencode({"q":loc1, "limit":"1", "key":key})

replydata= requests.get(url)
json_data= replydata.json()
json_status= replydata.status_code
print(json_data)

