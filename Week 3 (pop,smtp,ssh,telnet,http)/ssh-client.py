import paramiko

hostname = "192.168.0.44"
port = 22
user = "newz"
passwd = "password"

try:
    client = paramiko.SSHClient()
    client.load_system_host_keys()  # แก้ไขตรงนี้
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, port=port, username=user, password=passwd)
    
    while True:
        try:
            cmd = input("$> ")
            if cmd == "exit":   
                break
            stdin, stdout, stderr = client.exec_command(cmd)
            print(stdout.read().decode())
        except KeyboardInterrupt:
            break
    
    client.close()
    
except Exception as err:
    print(str(err))
