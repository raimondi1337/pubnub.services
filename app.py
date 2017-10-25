import RPi.GPIO as GPIO 

import time
from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration

pnconfig = PNConfiguration()
pnconfig.subscribe_key = 'sub-c-0d172eac-b5da-11e7-bf1e-62e28d924c11'
pnconfig.publish_key   = 'pub-c-92d545b8-5884-456c-9546-2fd40697fdb8'
pnconfig.uuid = 'device'
pnconfig.set_presence_timeout_with_custom_interval(60,10)
pubnub = PubNub(pnconfig)

pubnub.subscribe().channels('status').execute()

LEDPIN    = 12
SWITCHPIN = 10 
STALL_STATUS      = True 

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LEDPIN, GPIO.OUT)
GPIO.setup(SWITCHPIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.output(LEDPIN, GPIO.HIGH)

def publish_callback(result, status):
	print result 
	
try:
	while True:
		if (GPIO.input(SWITCHPIN) == GPIO.LOW and STALL_STATUS is False):
			STALL_STATUS = True
			GPIO.output(LEDPIN, GPIO.HIGH)
			print STALL_STATUS
			pubnub.publish().channel('status').message({'stall': 'Occupied'}).async(publish_callback)
		
		if (GPIO.input(SWITCHPIN) == GPIO.HIGH and STALL_STATUS is True):
			STALL_STATUS = False
			GPIO.output(LEDPIN, GPIO.LOW)
			print STALL_STATUS
			pubnub.publish().channel('status').message({'stall': 'Vacant'}).async(publish_callback)
except KeyboardInterrupt:
	GPIO.cleanup()
