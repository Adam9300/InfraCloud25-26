import json

webex_response = '''
{
  "items": [
    {
      "id": "1",
      "displayName": "Alice",
      "emails": ["alice@example.com"],
      "type": "person"
    },
    {
      "id": "2",
      "displayName": "Bob",
      "emails": ["bob@example.com"],
      "type": "person"
    },
    {
      "id": "3",
      "displayName": "Meeting Room",
      "type": "room"
    }
  ]
}
'''
data = json.loads(webex_response)
for item in data["items"]:
    if item["type"] == "person":
        name = item["displayName"]
        email = item["emails"][0]
        print(f"Naam: {name}, Email: {email}")


