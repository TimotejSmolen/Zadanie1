import pysip
import time
import logging
import SocketServer


ipaddress = '10.83.177.23'
PORT = 60000
pysip.recordroute = "Record-Route: <sip:%s:%d;lr>" % (ipaddress, PORT)
pysip.topvia = "Via: SIP/2.0/UDP %s:%d" % (ipaddress, PORT)
server = SocketServer.UDPServer((ipaddress, PORT), pysip.UDPHandler)
server.serve_forever()



