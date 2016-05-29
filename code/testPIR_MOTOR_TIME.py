import RPi.GPIO as GPIO
import time
import datetime

GPIO.setmode(GPIO.BCM)

# pin setting
pir = 21
motor_R1 = 23
motor_R2 = 24
motor_R3 = 27
motor_R4 = 22
motor_L1 = 4
motor_L2 = 17
motor_L3 = 18
motor_L4 = 25

GPIO.setup(pir, GPIO.IN)
GPIO.setup(motor_R1, GPIO.OUT)
GPIO.setup(motor_R2, GPIO.OUT)
GPIO.setup(motor_R3, GPIO.OUT)
GPIO.setup(motor_R4, GPIO.OUT)
GPIO.setup(motor_L1, GPIO.OUT)
GPIO.setup(motor_L2, GPIO.OUT)
GPIO.setup(motor_L3, GPIO.OUT)
GPIO.setup(motor_L4, GPIO.OUT)

GPIO.output(motor_R1, True)
GPIO.output(motor_R2, True)
GPIO.output(motor_L1, True)
GPIO.output(motor_L2, True)

now = datetime.datetime.now()
nowDate = now.strftime('%H:%M')
wakeup = "10:00"

try:
    print "PIR + MOTOR module test (ctrl+c to exit)"
    time.sleep(2)
    print "Ready"


    while True:
        
	now = datetime.datetime.now()
	nowDate = now.strftime('%H:%M')
	if nowDate==wakeup:
            if GPIO.input(pir):
                print "motion detexted!, gogogogogo"
                GPIO.ouput(motor_R3, False)
                GPIO.ouput(motor_R4, True)
                GPIO.ouput(motor_L3, True)
                GPIO.ouput(motor_L4, False)
                
            else:
                print "no"

except KeyboardInterrupt:
    print "Quit"
    GPIO.cleanup()