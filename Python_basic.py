from netmiko import ConnectHandler

# Device details
vEOS3 = {
    "device_type": "arista_eos",
    "host": "192.168.24.131",   # vEOS3 IP
    "username": "admin",        # your vEOS username
    "password": "admin",        # your vEOS password
}

# Connect to device
connection = ConnectHandler(**vEOS3)

# Run a command
output = connection.send_command("show ip interface brief")
print(output)

# Close connection
connection.disconnect()
