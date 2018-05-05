
# Download Adafruit_DHT from github DHT11
#install it using "sudo python setup.py install"




#!/usr/bin/python
import sys
import Adafruit_DHT
while True:
    hum,temp=Adafruit_DHT.read_retry(11,4)
    print(hum,temp)
    
