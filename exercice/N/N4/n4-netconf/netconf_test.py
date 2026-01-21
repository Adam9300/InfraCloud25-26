
from ncclient import manager

router = {
    "host": "192.168.56.101",
    "port": 830,
    "username": "cisco",
    "password": "cisco123!",
    "hostkey_verify": False
}

with manager.connect(**router) as m:
    print("=== NETCONF CAPABILITIES ===")
    for capability in m.server_capabilities:
        print(capability)
