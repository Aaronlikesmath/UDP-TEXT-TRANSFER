# Doing imports
import socket
from datetime import datetime
from myutils import JsonWrap
from socketUtils import UdpSocket

# Getting Ip and Port
PORT = JsonWrap("clientconf.js").openjsvar("Port")
IP = JsonWrap("clientconf.js").openjsvar("IP")

#Getting your Own hostip and port
HostIP = JsonWrap("clientconf.js").openjsvar("HostIP")
HostPort = JsonWrap("clientconf.js").openjsvar("HostPort")

# Setting up  UdpSocket
US = UdpSocket([HostIP, HostPort])

# Setting up UDP Socket
US.init()

# Starting client
while True:
    US.sendpacket("CONNECTED: 1000", IP, PORT)
    if input("Do you want to send a message? [Y/N(N will also refresh msges)]").lower() == "y":
        # SENDING DATA
        Send_data = input("What MSG do you want to send?: ")
        US.sendpacket(Send_data, IP, PORT)
        print (f"Sent: {Send_data} \n Time: {datetime.now()}")
    # This code will parse and receive DATA
    # Asking for return packet (Just to make sure that the recvfrom doesnt get stuck until there new messages)
    US.sendpacket("Return: 500", IP, PORT)
    data, address = US.s.recvfrom(4096)
    decoded = data.decode("utf-8")
    if decoded == "RECEIVED: 1100":
        print ("\nMessage has been delivered\n")
    elif decoded == "Returned: 400":
        print ("\n Server Pinged \n")
    else:
        print (decoded)