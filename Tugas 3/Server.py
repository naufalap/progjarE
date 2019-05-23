import sys
import socket
import os
from threading import Thread

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 9001)
print >> sys.stderr, 'starting up on %s port %s' %server_address
sock.bind(server_address)

sock.listen(1)
def fungsi(connection):
    #connection = connectiondata[0]
    while True:
        req = connection.recv(32)
        if(req == '1'):
            connection.send("READY")
            while True:
                data = connection.recv(1024)
                if(data[0:5]=="START"):
                    print data[6:]
                    namanya = "Image/" + data[6:]
                    fp = open(namanya,'wb+')
                    ditulis=0
                elif(data=="FINISH"):
                    fp.close()
                elif(data=="ENDING"):
                    break
                else:
                    print "blok ", len(data), data[0:10]
                    fp.write(data)
            namafile.append(namanya)

while True:
    print "waiting for a connection"
    connection, client_address = sock.accept()
    print >> sys.stderr, 'connection from', client_address
    thread = Thread(target=fungsi, args=(connection, ))
    thread.start()

