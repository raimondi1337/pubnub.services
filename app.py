import RPi.GPIO as io
import time

LEDPIN =12 

def setup():
	io.setmode(io.BOARD)
	io.setup(LEDPIN, io.OUT)
	io.output(LEDPIN, io.HIGH)

def blink():
	while True:
		io.output(LEDPIN, io.HIGH)
		time.sleep(1)
		io.output(LEDPIN, io.LOW)
		time.sleep(1)

def destroy():
	io.output(LEDPIN, io.LOW)
	io.cleanup()

if __name__=="__main__":
	setup()
	try:
		blink()
	except KeyboardInterrupt:
		destroy()

