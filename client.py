# Doing imports
import socket
from datetime import datetime
from myutils import JsonWrap

# Getting Ip and Port
hostport = JsonWrap("clientconf.js").openjsvar("HostPort")
hostip = JsonWrap("clientconf.js").openjsvar("HostIP")

# Setting up UDP Socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

# Starting client
while True:
    send_data = input("Type data to send here: ")
    encode_data = send_data.encode("utf-8")
    s.sendto(encode_data, (hostip, hostport))
    print (f"\n\nSend data: {send_data} \n Time: {datetime.now()}")
