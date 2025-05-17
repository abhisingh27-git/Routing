
# Define your VM and Router details
#linux_vm_ip = "192.168.56.107"  # Replace with your Linux VM's IP
#linux_vm_user = "vboxuser"
#linux_vm_pass = "Ubuntu@2025"

import paramiko
from netmiko import ConnectHandler

# Define your VM and Router details
linux_vm_ip = "192.168.56.114"  # Replace with your Linux VM's IP
linux_vm_user = "vboxuser"  # Replace with your Linux VM username
linux_vm_pass = "Ubuntu@2025"  # Replace with your Linux VM password

router_ip = "192.168.56.20"  # Replace with your router's IP
router_user = "cisco"  # Router username
router_pass = "cisco123"  # Router password
router_enable_pass = "ciscoenable"  # Router enable password (if needed)

# SSH into the Linux VM using Paramiko
def ssh_to_linux_vm():
    print("Connecting to Linux VM...")
    ssh_vm = paramiko.SSHClient()
    ssh_vm.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_vm.connect(linux_vm_ip, username=linux_vm_user, password=linux_vm_pass)
    
    # Once logged in, run the Netmiko commands from the Linux VM to SSH into the router
    print("Connected to Linux VM. Now connecting to the router...")
    
    # Use Netmiko to interact with the router on the Linux VM
    router_connection = {
        'device_type': 'cisco_ios',
        'host': router_ip,
        'username': router_user,
        'password': router_pass,
        'secret': router_enable_pass,  # Enter enable mode if required
    }
    
    # Connect to the router via Netmiko
    net_connect = ConnectHandler(**router_connection)
    net_connect.enable()  # Enter enable mode if needed
    
    # Send configuration commands to the router
    config_commands = [
        'interface FastEthernet0/1',
        'ip address 192.168.2.1 255.255.255.0',
        'no shutdown',
        'exit',
        'show ip interface brief'  # Verify interfaces after configuring
    ]
    
    # Send the config commands to the router
    output = net_connect.send_config_set(config_commands)
    print(output)  # Display the output
    
    # Optional: Save the config
    net_connect.save_config()

    # Disconnect from the router
    net_connect.disconnect()
    
    # Close the connection to the Linux VM
    ssh_vm.close()
    print("Commands executed and connection closed.")

# Run the function
ssh_to_linux_vm()