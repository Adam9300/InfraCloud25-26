from netmiko import ConnectHandler

router = {
    "device_type": "cisco_ios",
    "host": "192.168.56.101",
    "username": "cisco",
    "password": "cisco123!",
}

print("🔗 Verbinden met router...")
connection = ConnectHandler(**router)

print("📡 Uitvoeren: show ip interface brief")
output = connection.send_command("show ip interface brief")
print(output)

connection.disconnect()
print("✅ Verbinding gesloten")
