import json
import yaml

json_data = '''
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
    }
  ]
}
'''

data = json.loads(json_data)

yaml_output = yaml.dump(data, sort_keys=False)

print(yaml_output)
