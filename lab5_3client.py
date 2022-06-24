import socket
import sys
import json

s = socket.socket()

port = 9898

s.connect(('10.0.2.15', port))

data = s.recv(1024)
data = data.decode("utf-8")

s.send(b'Thank you from client!');

dataJ = json.loads(data)

print (type(dataJ))
print(dataJ)

s.close()
