
import time
from time import gmtime, strftime
from ws4py.client.threadedclient import WebSocketClient

class RaspiClient(WebSocketClient):
    def opened(self):
        self.send("Hi there!")
        print "Connection opened..."

    def closed(self, code, reason=None):
        print "Connection closed... ", code, reason

    def received_message(self, m):
        print "Received from server: %s" % (str(m))

try:
    ws = RaspiClient('ws://ec2-23-20-219-99.compute-1.amazonaws.com:8080/ws')
    ws.connect()
except KeyboardInterrupt:
    ws.close()

while True:
    time.sleep(4)
    print strftime("%Y-%m-%d %H:%M:%S", gmtime())