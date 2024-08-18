import socket
from IPy import IP
ipaddress = input("[+] enter ip to scan ")
port = 80
try:
    sock=socket.socket()
    sock.connect((ipaddress,port))

    print("[+] port80 is open")
except:
    print("[+] port 80 is close")
    