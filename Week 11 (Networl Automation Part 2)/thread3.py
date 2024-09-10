import paramiko
import time

HOST = "10.4.15.60"
user = "cisco"
password = "cisco"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=HOST, username=user, password=password, allow_agent=False, look_for_keys=False, look_for_keys=False)

print("Successful connected to: " +HOST)

remote_connection = ssh_client.invoke_shell()
remote_connection.send("en\n")
remote_connection.send("sh ip int b\n")
time.sleep(1)

output = remote_connection.recv(65535)
print(output.decode('ascii'))

ssh_client.close()