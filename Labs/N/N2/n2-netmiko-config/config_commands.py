from netmiko import ConnectHandler

router = {
    "device_type": "cisco_ios",
    "host": "192.168.56.101",
    "username": "cisco",
    "password": "cisco123!",
}

print("🔗 Verbinden met router via NETMIKO (SSH)...")

net_connect = ConnectHandler(**router)

config_commands = [
    "interface Loopback2222",
    "ip address 10.100.100.1 255.255.255.255",
    "description Configured via Netmiko"
]

output = net_connect.send_config_set(config_commands)

print(output)

net_connect.disconnect()

print("✅ NETMIKO SSH sessie gesloten")
