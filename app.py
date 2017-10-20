import RPi.GPIO as GPIO 
import time

LEDPIN    = 12
SWITCHPIN = 10 
OPEN      = True 

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LEDPIN, GPIO.OUT)
GPIO.setup(SWITCHPIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.output(LEDPIN, GPIO.HIGH)
	
while True:
	if (GPIO.input(SWITCHPIN) == GPIO.LOW and OPEN is False):
		OPEN = True
		GPIO.output(LEDPIN, GPIO.HIGH)
		print OPEN
	
	if (GPIO.input(SWITCHPIN) == GPIO.HIGH and OPEN is True):
		OPEN = False
		GPIO.output(LEDPIN, GPIO.LOW)
		print OPEN

