import socket

try:
    print("Fully qualified domain name" + socket.getfqdn("8.8.8.8"))
    print("Host name to IP address:")