from socketUtils import UdpSocket
from myutils import JsonWrap
import multiprocessing
from datetime import datetime

class UDPTEXTCLIENT(object):
    def __init__(self, conf_file):
        self.JS = JsonWrap(conf_file)
        self.HostIP = self.JS.openjsvar("HostIP")
        self.HostPort = self.JS.openjsvar("HostPort")
        self.IP = self.JS.openjsvar("IP")
        self.port = self.JS.openjsvar("Port")
        self.US = UdpSocket([self.HostIP, self.port])
        self.US.init()
        self.US.sendpacket("CONNECTED: 1000", self.IP, self.port)
        self.msgup = multiprocessing.Process(target=self.msgupdate)

    def msgupdate(self):
        data, address = self.US.s.recvfrom(4096)
        self.packet = [data, address]

    def msgparse(self, packet):
        statuscode = False
        data, address = packet
        # Decode the utf-8 data
        msg = data.decode("utf-8")
        # Parse the address
        templist = list(address)
        sendrIP = templist[0]
        # Look for status codes
        if msg == "RETURNED: 400":
            print (f"Pinged server at {datetime.now()}")
            statuscode = True

        elif msg == "RECEIVED: 1100":
            print (f"Server received MSG at {datetime.now()}")
            statuscode = True

        elif statuscode == False:
            print (f"\nMessage: {msg} \nFrom: {sendrIP} \n")
    
    def messagehandler(self):
        self.msgup.start()
        self.msgup.join(2)
        if self.msgup.is_alive():
            self.msgup.terminate()
            return
        self.msgparse(self.packet)

    def sendmsg(self, msg):
        self.US.sendpacket(msg, self.IP, self.port)