...
## To use this script we are setting environment variable for Router username & password inside the Linux OS
## Below are the commands used in Linux
## export NET_USERNAME=admin
## export NET_PASSWORD=Password123
...

import os
import json
from netmiko import ConnectHandler

with open("inventory.json") as file:
    inventory = json.load(file)

router = inventory["R1"]

router["username"] = os.getenv("NET_USERNAME")
router["password"] = os.getenv("NET_PASSWORD")

conn = ConnectHandler(**router)

print(conn.send_command("show ip int br "))

conn.disconnect()