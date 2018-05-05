# First unable camera module enable in configuration in References

from picamera import PiCamera
from time import sleep

camera=PiCamera()
camera.start_preview()

camera.start_recording('/home/pi/Desktop/video.h264') # Recording Format
sleep(10)
camera.start_recording()
camera.stop_preview()


# format need to change to mp4. so install gpac  " sudo apt-get install gpac"
# now convert the video to mp4 open terminal and type " MP4Box -fps 30 -add video.h264 video.mp4"
