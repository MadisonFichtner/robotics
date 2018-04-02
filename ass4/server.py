# https://pymotw.com/3/socket/tcp.html

import socket
import sys
from threading import Thread

class Server:

	def __init__(self):
		# Create a TCP/IP socket
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		
		# Bind the socket to the port
		server_address = ('10.200.10.163', 1000)
		print('starting up on {} port {}'.format(*server_address))
		self.sock.bind(server_address)

		# Listen for incoming connections
		self.sock.listen(1)

	def write(self):
		try:
			while True:
				if self.message != "":
					self.connection.send((self.message + '\n').encode())
					self.message = ""
		finally:
			self.connection.close
			
	def read(self):
		try:
			while True:
				data = self.connection.recv(256).decode()
				print('received {}'.format(data))
		finally:
			self.connection.close
			
	def input(self):
		while True:
			self.message = input()

	def run(self):
		# Wait for a connection
		print('waiting for a connection')
		self.connection, self.client_address = self.sock.accept()
		self.message = 'goodbye'
		try:
			print('connection from', self.client_address)
			readThread = Thread(target=self.read)
			writeThread = Thread(target=self.write)
			inputThread = Thread(target=self.input)
			
			readThread.start()
			writeThread.start()
			inputThread.start()
			
			readThread.join()
			writeThread.join()
			inputThread.join()
		finally:
			# Clean up the connection
			self.connection.close()

server = Server();
server.run();
