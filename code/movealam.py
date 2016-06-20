#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import datetime
import os

GPIO.setmode(GPIO.BCM)

btn = 19
pir = 21
motor1 = 4
motor2 = 17
motor3 = 18
motor4 = 25

GPIO.setup(btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pir, GPIO.IN)
GPIO.setup(motor1, GPIO.OUT)
GPIO.setup(motor2, GPIO.OUT)
GPIO.setup(motor3, GPIO.OUT)
GPIO.setup(motor4, GPIO.OUT)

GPIO.output(motor1, True)
GPIO.output(motor2, True)

now = datetime.datetime.now()
nowDate = now.strftime('%H:%M')
wakeup = "7:00"

GPIO.output(motor3, False)
GPIO.output(motor4, True)

print "timesleep"
time.sleep(4)

try:
    print "PIR+MOTER+TIME test ctrl_c to exit"
    time.sleep(2)
    print "Ready"

    while True:
        input_state = GPIO.input(btn)
        if input_state == False: 
            print('Button Pressed')
            GPIO.cleanup()

            
        now = datetime.datetime.now()
        nowDate = now.strftime('%H:%M')
        os.system("omxplayer -o local /home/pi/call.wav")
        if input_state == False:
            print('Button Pressed')
            GPIO.cleanup()
        print nowDate

        if GPIO.input(pir):
            print "gogogogogogo"
            GPIO.output(motor3, True)
            GPIO.output(motor4, False)
            if input_state == False:
                print('Button Pressed')
                GPIO.cleanup()
    
        else:
            print "no"
            GPIO.output(motor3, False)
            GPIO.output(motor4, True)
            if input_state == False:
                print('Button Pressed')
                GPIO.cleanup()


except KeyboardInterrupt:
    print "Quit"
    GPIO.cleanup()

    
