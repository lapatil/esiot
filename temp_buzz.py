
# Download Adafruit_DHT from github DHT11
#install it using "sudo python setup.py install"




#!/usr/bin/python
import sys
import Adafruit_DHT
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23,GPIO.OUT)
while True:
    hum,temp=Adafruit_DHT.read_retry(11,4)
    print(hum,temp)
    if(temp>=25):
        print("buzzer on")
        GPIO.output(21,GPIO.HIGH)
        
