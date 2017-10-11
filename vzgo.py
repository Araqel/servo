import RPi.GPIO as GPIO
from time import sleep

pin=3

GPIO.setmode(GPIO.BOARD)

GPIO.setup(pin, GPIO.OUT)

pwm=GPIO.PWM(pin, 50)

pwm.start(11)

def SetAngle(angle):
	duty = angle/18+2
	GPIO.output(pin, True)
	print(duty)
	pwm.ChangeDutyCycle(duty)
	sleep(5)
	GPIO.output(pin, False)
#	pwm.ChangeDutyCycle(0)


SetAngle(180)
#SetAngle(0)
#for angle in range(0,20):
#	SetAngle(angle)


pwm.stop()
GPIO.cleanup() 

