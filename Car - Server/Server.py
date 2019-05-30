import socket
import struct

class Server:

	def __init__(self, host, port):
		## Initialize the server and create the socket
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.bind((host, port))

	def Listen(self):
		print("Listening")
		self.s.listen()
		# acceot is a blocking function, it will wait until there client connecting
		self.conn, self.addr = self.s.accept()
		print("connected to", self.addr)

	def Decode(self, message):
		return struct.unpack("bbb", message)

	def Receive(self):
		## Reads data from the socket buffer
		messages = []
		bytes_read = 0
		while bytes_read < 3:
			msg = self.conn.recv(min(3 - bytes_read, 3))
			if msg == "":
				self.close()
				print("Socket Dropped")
			messages.append(msg)
			bytes_read = bytes_read + len(msg)
		return self.Decode(b''.join(messages))

	def close(self):
		self.conn.close()
		self.s.close()
