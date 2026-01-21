import requests

ACCESS_TOKEN = "ZTU4ODM5YmYtODA2OS00ZDk4LWJkZWYtZmE0NjhiZmQ4MTcxZTY0MDgzYWEtM2Fk_P0A1_cce0a1f3-bf77-42c7-a45d-46ec83d996ea"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

# ------------------------
# SPACE AANMAKEN
# ------------------------
create_url = "https://webexapis.com/v1/rooms"

create_payload = {
    "title": "DevNet Automation Space"
}

create_response = requests.post(
    create_url,
    headers=headers,
    json=create_payload
)

if create_response.status_code == 200:
    room_id = create_response.json()["id"]
    print("Space aangemaakt met ID:", room_id)
else:
    print("Fout bij aanmaken space")
    exit()

# ------------------------
# SPACE VERWIJDEREN
# ------------------------
delete_url = f"https://webexapis.com/v1/rooms/{room_id}"

delete_response = requests.delete(
    delete_url,
    headers=headers
)

if delete_response.status_code == 204:
    print("Space succesvol verwijderd")
else:
    print("Fout bij verwijderen space")

