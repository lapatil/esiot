# First unable camera module enable in configuration in References

from picamera import PiCamera
from time import sleep

camera=PiCamera()
camera.rotation=270
camera.start_preview(alpha=250)
camera.capture("/home/pi/Desktop/img1.jpg")
sleep(10)
camera.stop_preview()

