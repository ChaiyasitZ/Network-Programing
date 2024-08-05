import poplib
from email.message import EmailMessage

server = "192.168.188.134"
user = "newz"
passwd = "123"

server = poplib.POP3(server)
server.user(user)
server.pass_(passwd)

msgNum = len(server.list()[1])

for i in range(msgNum):
    for msj in server.retr(i+1)[1]:
        print(msj.decode())