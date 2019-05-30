import socket
import struct

class Client:
	def __init__(self, server, port):
		self.c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server = server
		self.port = port

	def connect(self):
		try:
			self.c.connect((self.server, self.port))
		except socket.timeout:
			print("Socket connection timed-out")

	def _send(self, data):
		buff = struct.pack("bbb", data['x'], data['y'], data['z'])
		self.c.sendall(buff)

	def send(self, data):
		self._send(data)

	def _close(self):
		self.c.close()

	def close(self):
		self._close()