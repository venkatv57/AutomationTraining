import os
import json
from netmiko import ConnectHandler

with open("inventory.json") as file:
    inventory = json.load(file)

for router in inventory["routers"]:

    try:

        router["username"] = os.getenv("NET_USERNAME")
        router["password"] = os.getenv("NET_PASSWORD")

        print(f"\nConnecting to {router['host']}")

        conn = ConnectHandler(**router)

        output = conn.send_command("show ip interface brief")

        print(output)

        conn.disconnect()

    except Exception as e:
        print(f"Failed to connect: {router['host']}")
        print(e)