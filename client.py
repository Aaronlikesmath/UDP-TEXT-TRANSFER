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
    Statuscode = False
    US.sendpacket("CONNECTED: 1000", IP, PORT)
    SelectDo = input("Do you want to send a message? [Y/N(N will also refresh msges)/T(For serverping)]").lower()
    if SelectDo == "y":
        # SENDING DATA
        Send_data = input("What MSG do you want to send?: ")
        US.sendpacket(Send_data, IP, PORT)
        print (f"Sent: {Send_data} \n Time: {datetime.now()}")
    if SelectDo == "t":
        US.sendpacket("Return: 500", IP, PORT)
    # This code will parse and receive DATA
    data, address = US.s.recvfrom(4096)
    decoded = data.decode("utf-8")
    if decoded == "RECEIVED: 1100":
        print ("\nMessage has been delivered\n")
    if decoded == "RETURNED: 500":
        Statuscode = True
    if Statuscode == False:
        print (decoded)