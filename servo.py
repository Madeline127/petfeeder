from gpiozero import Servo
from time import sleep
servo = Servo(17)
counter = 0
while counter < 8:
	servo.value = 0.25
	sleep(1)
	counter += 1
	if counter >= 8:
		servo.detach()
		sleep(86392)
		counter = 0
		continue
