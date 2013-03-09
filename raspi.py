
from ws4py.client.threadedclient import WebSocketClient

class EchoClient(WebSocketClient):
     def opened(self):
         print "Connection opened..."

     def closed(self, code, reason=None):
         print code, reason

     def received_message(self, m):
         self.send(m)

try:
    ws = EchoClient('ws://ec2-23-20-219-99.compute-1.amazonaws.com:8080/ws')
    ws.connect()
except KeyboardInterrupt:
    ws.close()