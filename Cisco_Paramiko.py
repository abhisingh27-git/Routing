import paramiko
import time

# Device credentials
ip = "192.168.24.130"
username = "cisco"
password = "cisco123"
#enable_password = "cisco123"

# Create SSH client
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    print(f"Connecting to {ip}...")
    client.connect(ip, username=username, password=password, look_for_keys=False, allow_agent=False)

    remote_conn = client.invoke_shell()
    time.sleep(1)
    remote_conn.recv(1000)

    # Enter enable mode
    remote_conn.send("enable\n")
    time.sleep(1)
    #remote_conn.send(f"{enable_password}\n")
    #time.sleep(1)

    # Run the command
    remote_conn.send("terminal length 0\n")  # Prevent --More-- prompts
    time.sleep(1)
    remote_conn.send("show ip int brief\n")
    time.sleep(2)
    remote_conn.send("show version\n")
    time.sleep(2)
    remote_conn.send("show int desc\n")
    time.sleep(10)
    remote_conn.send("wr\n")
    time.sleep(10)


    output = remote_conn.recv(5000).decode("utf-8")
    print("Command Output:\n")
    print(output)

finally:
    client.close()