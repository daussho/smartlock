import RPi.GPIO as GPIO
from time import sleep

def SetAngle(angle):
	duty = angle / 18 + 2
	GPIO.output(3, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(3, False)
	pwm.ChangeDutyCycle(0)

def servoStart():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(3, GPIO.OUT)
    pwm=GPIO.PWM(3, 50)
    pwm.start(0)
    SetAngle(90) 
    pwm.stop()
    GPIO.cleanup()

def servoStop():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(3, GPIO.OUT)
    pwm=GPIO.PWM(3, 50)
    pwm.start(0)
    SetAngle(90) 
    pwm.stop()
    GPIO.cleanup()

servoStart()