import json

network_data = '''
{
  "interfaces": [
    {
      "name": "GigabitEthernet0/0",
      "ip": "192.168.1.1",
      "status": "up"
    },
    {
      "name": "GigabitEthernet0/1",
      "ip": "unassigned",
      "status": "down"
    },
    {
      "name": "Loopback0",
      "ip": "10.1.1.1",
      "status": "up"
    }
  ]
}
'''

data = json.loads(network_data)

for interface in data["interfaces"]:
    if interface["status"] == "up":
        print(f"Interface: {interface['name']}, IP: {interface['ip']}")
