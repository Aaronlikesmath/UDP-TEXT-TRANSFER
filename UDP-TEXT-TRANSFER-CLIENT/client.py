from clientlib import UDPTEXTPARSE
from socketUtils import UdpSocket
from myutils import JsonWrap
from datetime import datetime
import rsa

# Setting up parsing lib
UTEXT = UDPTEXTPARSE()

def setup(conf_file):
    JS = JsonWrap(conf_file)
    HostIP = JS.openjsvar("HostIP")
    HostPort = JS.openjsvar("HostPort")
    IP = JS.openjsvar("IP")
    port = JS.openjsvar("Port")
    US = UdpSocket([HostIP, port])
    US.init()
    US.sendpacket("CONNECTED: 1000", IP, port)
    return HostIP, HostPort, IP, port, US

def encrypgen():
    public_key, private_key = rsa.newkeys(2048)
    return public_key, private_key

# Getiing vars
HostIP, HostPort, IP, port, US = setup("clientconf.js")

# Setting up socket
US = UdpSocket([HostIP, HostPort])

while True:
    select = input("What do you want to do? M(Send MSG)/S(Scan for MSG)/E(Encryption tools)")
    if select.lower() == "m":
        msg = input("\nWhat should the msg be?: ")
        US.sendpacket(msg, IP, port)
        data, address = US.s.recvfrom(4096)
        print (UTEXT.messagehandler(data, address))
    
    elif select.lower() == "e":
        select = input("What do you want to do? [G(Generate new keys)/I(Import keys)/EX(Export keys)/D(Decrypt message using current key)/E(Send Encrypted msg)]")
        if select.lower() == "g":
            public_key, private_key = encrypgen()
        elif select.lower() == "i":
            data, address = US.s.recvfrom(4096)
            e_public_key = data.decode("utf-8")
        elif select.lower() == "ex":
            US.sendpacket(str(public_key), IP, port)
        elif select.lower() == "d":
            data, address = US.s.recvfrom(4096)
            msg = rsa.decrypt(data.decode("utf-8"), private_key)
            print (f"\nMessage: {msg}\nFrom: {list(address)[0]}\nTime: {datetime.now()}")
        elif select.lower() == "e":
            msg = input("\nWhat should the MSG be: ")
            emsg = rsa.encrypt(msg, e_public_key)

    elif select.lower() == "s":
        data, address = US.s.recvfrom(4096)
        print ("got packets")
        print (UTEXT.messagehandler(data, address))
    