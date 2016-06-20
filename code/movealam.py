#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import datetime
import os

GPIO.setmode(GPIO.BCM)

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
wakeup = "7:00"

GPIO.output(motor_R3, False)
GPIO.output(motor_R4, False)
GPIO.output(motor_L3, False)
GPIO.output(motor_L4, True)

print "timesleep"
time.sleep(4)

try:
    print "PIR+MOTER+TIME test ctrl_c to exit"
    time.sleep(2)
    print "Ready"

    i = 0;
    while True:
        now = datetime.datetime.now()
        nowDate = now.strftime('%H:%M')
        os.system("omxplayer -o local /home/pi/alam.wav")
        print nowDate

        if GPIO.input(pir):
            print "gogogogogogo"
            GPIO.output(motor_R3, False)
            GPIO.output(motor_R4, True)
            GPIO.output(motor_L3, True)
            GPIO.output(motor_L4, False)
            time.sleep(3)
    
        else:
            print "no"
            GPIO.output(motor_R3, False)
            GPIO.output(motor_R4, False)
            GPIO.output(motor_L3, False)
            GPIO.output(motor_L4, True)
            
    #while True:
    #    time.sleep(0.5)
    #    now = datetime.datetime.now()
    #    nowDate = now.strftime('%H:%M')
    #    print nowDate
    #    if nowDate == wakeup:
    #        if GPIO.input(pir):
    #            print "gogogogogogo"
    #            GPIO.output(motor_R3, False)
    #            GPIO.output(motor_R4, True)
    #            GPIO.output(motor_L3, True)
    #            GPIO.output(motor_L4, False)
    #            time.sleep(5)
    #
    #        else:
    #            print "no"
    #            GPIO.output(motor_R3, False)
    #            GPIO.output(motor_R4, False)
    #            GPIO.output(motor_L3, False)
    #            GPIO.output(motor_L4, True)
    #    else:
    #        GPIO.output(motor_R3, False)
    #        GPIO.output(motor_R4, False)
    #        GPIO.output(motor_L3, False)
    #        GPIO.output(motor_L4, True)

except KeyboardInterrupt:
    print "Quit"
    GPIO.cleanup()

    
