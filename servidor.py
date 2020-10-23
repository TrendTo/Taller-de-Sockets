#https://www.youtube.com/watch?v=nJYp3_X_p6c&ab_channel=codigofacilito

import socket

Socket = socket.socket()
Socket.bind( ('localhost', 8000) )
Socket.listen(5)

while True:
    conec, addr = Socket.accept()
    res = conec.recv(1024)
    print(res, addr)
    conec.send("Hola Mundo desde Servidor".encode())
    conec.close()