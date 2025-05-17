from netmiko import ConnectHandler

# Define device parameters
cisco_device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.24.129',            # Replace with your router/switch IP
    'username': 'cisco',            # Replace with your username
    'password': 'cisco123',     # Replace with your password
    'secret': 'cisco123', # Optional: for enable mode
}

# Connect to the device
print(f"connecting to device {['ip']}")

net_connect = ConnectHandler(**cisco_device)

# Enter enable mode (if required)
net_connect.enable()

# Send a show command
output = net_connect.send_command('show ip int brief')
print("Show Command Output:")
print(output)

# Send configuration commands
config_commands = [
    'interface Loopback0',
    'ip address 10.1.1.1 255.255.255.0',
    'description Configured via Netmiko',
]
output = net_connect.send_config_set(config_commands)
print("\nConfiguration Output:")
print(output)

# Save config
save_output = net_connect.save_config()
print("\nSave Config Output:")
print(save_output)

# Disconnect
net_connect.disconnect()