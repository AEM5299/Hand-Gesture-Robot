# Hand Gestures Controlled Car
The idea of this project was to create a car that could be controlled by hand gesture, much like a wii controller if you will. The car will play the role of the server and the controller will be a client. When the car is turned on the program listen for connections over the device's own network. After the remote connects to the car it start sending data using sockets.

# Devices
- Raspberry Pi 3B +
- Raspberry Pi Zero W
- Accelerometer MPU6050
- Chassis and 4 wheels and motors
- 2 Motor Drivers L298

# Manuals
- You need to set up the Raspberry Pi 3B + as an access point. Doesn't have to be bridged internet access is not needed. You can find a toturial on how to do so here: https://www.raspberrypi.org/documentation/configuration/wireless/access-point.md

# Dependencies
- Gpiozero - https://github.com/RPi-Distro/python-gpiozero
- MPU6050 library - https://github.com/Tijndagamer/mpu6050 (Included in the repo, modified to cater project needs)

# Demo
- https://urlzs.com/wXGtk

