#https://www.youtube.com/watch?v=nJYp3_X_p6c&ab_channel=codigofacilito

import socket

Socket = socket.socket()
Socket.connect( ('localhost', 8000) )

Socket.send("Hola mundo desde Cliente".encode())
resp = Socket.recv(1024)

print(resp)
Socket.close()