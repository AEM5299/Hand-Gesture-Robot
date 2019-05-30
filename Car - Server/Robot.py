from gpiozero import Motor
import RPi.GPIO as gpio
from time import sleep

class Robot:
	def __init__(self):
		self.m1 = Motor(27,17)
		self.m2 = Motor(23,24)
		self.m3 = Motor(6,5)
		self.m4 = Motor(16,13)
		self.stop_status = False
		self.data = []
		self.data.append((0, 0, 7))

	def print_data(self):
		while not self.stop_status:
			try:
				d = self.data.pop(0)
			except:
				print(len(self.data))
				continue
			print(d)

	def move(self):
		while not self.stop_status:
			if len(self.data) == 0:
				continue
			_,y,z = self.data.pop(0)
			forward_power = (y / 10)
			# 7 doesn't have any special meaning, it is just the value I get when the accelerometer is on a flat surface
			# [-1, 7) means go *left*, [8, 19] go *right*
			# As you can see, for some reason the acclerometer have more 'levels' for *right* than *left*, so it is somewhat more
			# sensitive to turn right
			if z < 7:
				self.m1.forward(max(min(forward_power, 1), 0) * 0.25)
				self.m2.forward(max(min(forward_power, 1), 0))
				self.m3.forward(max(min(forward_power, 1), 0))
				self.m4.forward(max(min(forward_power, 1), 0) * 0.25)
			elif z > 7:
				self.m1.forward(max(min(forward_power, 1), 0))
				self.m2.forward(max(min(forward_power, 1), 0) * 0.25)
				self.m3.forward(max(min(forward_power, 1), 0) * 0.25)
				self.m4.forward(max(min(forward_power, 1), 0))
			else:
				self.m1.forward(max(min(forward_power, 1), 0))
				self.m2.forward(max(min(forward_power, 1), 0))
				self.m3.forward(max(min(forward_power, 1), 0))
				self.m4.forward(max(min(forward_power, 1), 0))




