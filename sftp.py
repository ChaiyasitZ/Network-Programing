#sftp.get("/home/newz/test.txt","C:/Users/Chaiyasit Mintakorn/Downloads/d.txt")
import paramiko

hostname = "192.168.188.134"
username = "newz"
passwd = "123"
port = 22

try:
    p = paramiko.Transport((hostname, port))
    p.connect(username=username, password=passwd)
    print("Connected to %s" % hostname + " via SSH")
    sftp = paramiko.SFTPClient.from_transport(p)
    print("Starting download")
    sftp.get("/home/newz/test.txt", "C:/Users/Chaiyasit Mintakorn/Downloads/d.txt")
    print("Downloaded")
    print("Starting upload")
    sftp.put("C:/Users/Chaiyasit Mintakorn/Downloads/d.txt", "/home/newz/d.txt")
    print("Uploaded")
    p.close()
    print("Disconnected")

except Exception as err:
    print("[!]", str(err))