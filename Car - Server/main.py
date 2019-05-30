import RPi.GPIO as GPIO
from Robot import Robot
from Server import Server
import threading
from time import sleep

GPIO.setmode(GPIO.BCM)
s = Server("192.168.0.10", 65432)
moving_thread = None
robot = None

STOP_BUTTON_PIN = 26

def setup():
	# My button wasn't working properly so couldn't test this, but should work
	# GPIO.setup(STOP_BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	# GPIO.add_event_detect(STOP_BUTTON_PIN, GPIO.FALLING, callback=stop, bouncetime=1000)
	global robot, moving_thread
	robot = Robot()
	moving_thread = threading.Thread(target=robot.move)


def main():
	s.Listen()
	moving_thread.start()
	while not robot.stop_status:
		robot.data.append(s.Receive())
		sleep(0.05)



def stop(channel):
	robot.stop_status = True
	s.close()


if __name__ == "__main__":
	try:
		setup()
		main()
	except KeyboardInterrupt:
		stop(0)
		pass
	finally:
		GPIO.cleanup()
