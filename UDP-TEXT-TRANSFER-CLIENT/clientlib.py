from myutils import JsonWrap
from datetime import datetime

class UDPTEXTPARSE(object):

    def messagehandler(self, data, address):
        statuscode = False
        # Decode the utf-8 data
        msg = data.decode("utf-8")
        # Parse the address
        templist = list(address)
        sendrIP = templist[0]
        # Look for status codes
        if msg == "RETURNED: 400":
            return (f"Pinged server at {datetime.now()}")
            statuscode = True

        elif msg == "RECEIVED: 1100":
            return (f"Server received MSG at {datetime.now()}")
            statuscode = True

        elif statuscode == False:
            return (f"\nMessage: {msg} \nFrom: {sendrIP} \n")