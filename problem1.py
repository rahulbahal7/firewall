import socket
import json
import time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 2002))
with open("a.json") as f:
        while 1:
                readmsg=f.read(13)
                s.send((readmsg))
                if not readmsg:
                        break
                time.sleep(.2)
                readmsg1=f.read()
                s.send((readmsg1))
print json.loads(s.recv(1024))
