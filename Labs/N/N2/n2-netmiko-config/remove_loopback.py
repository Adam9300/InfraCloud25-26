from netmiko import ConnectHandler

router = {
    "device_type": "cisco_ios",
    "host": "192.168.56.101",
    "username": "cisco",
    "password": "cisco123!",
}

print("🔗 Verbinden met router via Netmiko...")
net_connect = ConnectHandler(**router)

# Te verwijderen loopback
loopback_id = "Loopback100"

print(f"🗑️ Verwijderen van {loopback_id}...")

config_commands = [
    f"no interface {loopback_id}"
]

output = net_connect.send_config_set(config_commands)
print(output)

# Controle
print("🔍 Controle loopbacks:")
check = net_connect.send_command("show ip interface brief | include Loopback")
print(check)

net_connect.disconnect()
print("✅ Netmiko sessie gesloten")
