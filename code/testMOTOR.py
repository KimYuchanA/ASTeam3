try:
	import RPi.GPIO as GPIO
	import time

	GPIO.setmode(GPIO.BCM)
	GPIO.setup(23, GPIO.OUT) #right motor
	GPIO.setup(24, GPIO.OUT)
	GPIO.setup(27, GPIO.OUT)
	GPIO.setup(22, GPIO.OUT)
	GPIO.setup(4, GPIO.OUT) #left motor
	GPIO.setup(17, GPIO.OUT)
	GPIO.setup(18, GPIO.OUT)
	GPIO.setup(25, GPIO.OUT)

	GPIO.output(23, True)
	GPIO.output(24, True)
	GPIO.output(4, True)
	GPIO.output(17, True)

	print('Test Start')

	while True:
	# 2016/05/04
	# (1) going back about both motor
	GPIO.output(27, False)
	GPIO.output(22, True)

	GPIO.output(18, True)
	GPIO.output(25, False)
	
	# go ahead (R)
	#GPIO.output(27, True)
	#GPIO.output(22, False)

	# go back (R)
	#GPIO.output(27, False)
	#GPIO.output(22, True)

	# stop (R)
	#GPIO.output(27, False)
	#GPIO.output(22, False)

	# go back (L)
	#GPIO.output(18, True)
	#GPIO.output(25, False)

	# go ahead (L) --> not working
	#GPIO.output(18, False)
	#GPIO.output(25, True)	

	# stop (L)
	#GPIO.output(18, False)
	#GPIO.output(25, False)

	#time.sleep(2)

except KeyboardInterrupt:
	GPIO.cleanup()
