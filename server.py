# Importing stuff
from datetime import datetime
import socket
from myutils import JsonWrap
from socketUtils import UdpSocket
import time


# Setting port
servport = JsonWrap("serveconf.js").openjsvar("Port")

# Getting computer IP
hostIP = JsonWrap("serveconf.js").openjsvar("Ip")

# Getting Port to relay text back to clients
RelayPort = JsonWrap("serveconf.js").openjsvar("RelayPort")

# Setting up SocketUtils
US = UdpSocket([hostIP, servport])

# Creating a UDP socket
US.init()

# Adding Ip list so we can forward new messages
IPlist = []

# Starting server Loop
while True:
    data, address = US.s.recvfrom(4096)
    # Converting address tuple to list
    templist = list(address)
    IPadress = templist[0]
    # Decoding data
    decoded_data = data.decode("utf-8")
    # Adding Ip address to list if received connection packet and IP not already in list
    if decoded_data == "CONNECTED: 1000":
        if IPlist.count(IPadress) == 0:
            IPlist.append(IPadress)
    elif decoded_data == "Return: 500":
        US.sendpacket("Returned: 400", IPadress, RelayPort)
    else:
        # Printing data of received packet
        print (f"\n \n Received: {decoded_data} \n From: {IPadress} \n Time: {datetime.now()} \n \n")
        relaymsg = f"\nMessage: {decoded_data} \n From: {IPadress}"
        # Relaying data to other clients
        for Ipadd in IPlist:
            if Ipadd != IPadress:
                US.sendpacket(relaymsg, Ipadd, RelayPort)
        US.sendpacket("RECEIVED: 1100", IPadress, 12000)