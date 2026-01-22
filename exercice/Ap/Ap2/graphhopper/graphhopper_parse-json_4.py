import requests
import urllib.parse

route_url = "https://graphhopper.com/api/1/route?"
key = "0cce328d-a06f-480e-ac1b-43427b350fb3"

def geocoding(location, key):
    while location == "":
        location = input("Enter the location again: ")

    geocode_url = "https://graphhopper.com/api/1/geocode?"
    url = geocode_url + urllib.parse.urlencode({
        "q": location,
        "limit": "1",
        "key": key
    })

    response = requests.get(url)
    json_data = response.json()
    status = response.status_code

    # ❌ GEEN RESULTAAT
    if status != 200 or len(json_data["hits"]) == 0:
        print(f"❌ Geen resultaat gevonden voor: {location}")
        return None

    # ✅ RESULTAAT GEVONDEN
    hit = json_data["hits"][0]
    lat = hit["point"]["lat"]
    lng = hit["point"]["lng"]
    name = hit.get("name", location)
    state = hit.get("state", "")
    country = hit.get("country", "")
    value = hit.get("osm_value", "")

    new_loc = name
    if state:
        new_loc += ", " + state
    if country:
        new_loc += ", " + country

    print(f"Geocoding API URL for {new_loc} (Type: {value})")
    print(url, "\n")

    return lat, lng, new_loc


# ================= MAIN =================
while True:
    loc1 = input("Starting location: ")
    if loc1.lower() in ["q", "quit"]:
        break

    orig = geocoding(loc1, key)
    if orig is None:
        continue
    print("Origin:", orig)

    loc2 = input("Destination: ")
    if loc2.lower() in ["q", "quit"]:
        break

    dest = geocoding(loc2, key)
    if dest is None:
        continue
    print("Destination:", dest)
