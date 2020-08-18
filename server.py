# Importing stuff
from datetime import datetime
import socket
from myutils import JsonWrap

# Setting port
servport = JsonWrap("serveconf.js").openjsvar("Port")

# Getting computer IP
#hostIP = socket.gethostbyname(socket.gethostname())
hostIP = JsonWrap("serveconf.js").openjsvar("Ip")

# Creating a UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Binding socket to IP and Port
Bindaddr = (hostIP, servport)
s.bind(Bindaddr)

# Starting server Loop
while True:
    print ("###### Server is listening on UDP 10000 ######")
    data, address = s.recvfrom(4096)
    decoded_data = data.decode("utf-8")
    # Printing data of received packet
    print (f"\n \n Received: {decoded_data} \n From: {address} \n Time: {datetime.now()} \n \n")
