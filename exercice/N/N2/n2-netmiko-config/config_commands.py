from netmiko import ConnectHandler
from netmiko.ssh_exception import (
    NetmikoTimeoutException,
    NetmikoAuthenticationException
)

router = {
    "device_type": "cisco_ios",
    "host": "192.168.56.101",
    "username": "cisco",
    "password": "cisco123!",
}

config_commands = [
    "interface Loopback100",
    "description Configured by Netmiko (N2)",
    "ip address 10.100.100.1 255.255.255.255"
]

try:
    print("🔗 Verbinden met router via SSH...")
    connection = ConnectHandler(**router)

    print("⚙️ Configuratie toepassen...")
    output = connection.send_config_set(config_commands)
    print(output)

    connection.disconnect()
    print("✅ Configuratie succesvol toegepast en verbinding gesloten")

except NetmikoAuthenticationException:
    print("❌ Authenticatie mislukt")

except NetmikoTimeoutException:
    print("❌ Router niet bereikbaar via SSH")
