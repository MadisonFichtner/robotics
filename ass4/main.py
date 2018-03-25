# https://pymotw.com/3/socket/tcp.html

import socket
import sys

# create TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind socket to port
server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address))

# listen for connections
sock.listen(1)

while True:
    # wait for connection
    print('waiting for connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)
    finally:
        connection.close()
