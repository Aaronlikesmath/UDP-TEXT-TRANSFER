import socket

class UdpSocket(object):
    def __init__(self, ip_port):
        self.ip, self.port = ip_port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

    def init(self):
        self.s.bind((self.ip, self.port))
    
    def sendpacket(self, send_data, tip, tport):
        encoded = send_data.encode("utf-8")
        self.s.sendto(encoded, (tip, tport))
