import pysip
import time
import logging
import SocketServer

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', filename='proxy.log', level=logging.INFO,
                    datefmt='%H:%M:%S')
logging.info(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime()))



ipaddress = '192.168.0.100'
PORT = 60000
pysip.recordroute = "Record-Route: <sip:%s:%d;lr>" % (ipaddress, PORT)
pysip.topvia = "Via: SIP/2.0/UDP %s:%d" % (ipaddress, PORT)
server = SocketServer.UDPServer((ipaddress, PORT), pysip.UDPHandler)
server.serve_forever()



