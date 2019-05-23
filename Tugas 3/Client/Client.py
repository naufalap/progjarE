import sys
import socket
import os

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 9001)
print >> sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

try:
    print "input: 1. kirim gambar 2. tutup"
    while True:
        req = raw_input('>')
        sock.send(req)
        if(req=='1'):
            nama = raw_input('Masukan nama file > ')
            sock.send("START {}" . format(nama))
            ukuran = os.stat(nama).st_size
            fp = open(nama,'rb')
            k = fp.read()
            terkirim=0
            for x in k:
                sock.send(x)
                terkirim = terkirim + 1
                print "\r terkirim {} of {} " . format(terkirim,ukuran)
            fp.close()
            sock.send("FINISH")
            sock.send("ENDING")
        elif(req=='2'):
            break
finally:
    print >> sys.stderr, 'closing socket'
    sock.close()