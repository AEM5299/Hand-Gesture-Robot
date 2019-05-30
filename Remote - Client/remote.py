import RPi.GPIO as GPIO
import threading
from mpu6050_custom import mpu6050
from time import sleep
import client


class Remote:
	STOP = False
	data = []

	def __init__(self, socket):
		self.socket = socket
		self.sensor = mpu6050(0x68)
		self.output_data_thread = threading.Thread(target=self.send_data)
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		#GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		sleep(0.5)
		self.sensor.calibrate()
		GPIO.add_event_detect(17, GPIO.FALLING, self.readData, 200)
		# Again my button is buggy so I couldn't test this out.
		#GPIO.add_event_detect(27, GPIO.FALLING, self.stop, 500)

	def printData(self):
		while not self.STOP:
			try:
				d = self.data.pop(0)
				print("X: %d" % d['x'], ", Y: %d" % d['y'], ", Z: %d" % d['z'])
			except:
				pass
			sleep(0.2)

	def send_data(self):
		while not self.STOP:
			if len(self.data) == 0:
				continue
			try:
				self.socket.send(self.data.pop(0))
			except IndexError:
				print("Index Error %d" % len(self.data))
				pass
			except:
				print("Socket Dropped")
				self.stop()
			sleep(0.15)

	def readData(self, channel):
		self.data.append(self.sensor.get_accel_data())

	def RUN(self):
		self.socket.connect()
		self.sensor.enable_interrupt()
		sleep(0.1)
		self.output_data_thread.start()
		while not self.STOP:
			pass
		else:
			self.stop()

	def stop(self):
		self.STOP = True
		GPIO.remove_event_detect(17)
		#GPIO.remove_event_detect(27)
		self.socket.close()
		GPIO.cleanup()
		del self.socket