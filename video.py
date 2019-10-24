from picamera.array import PiRGBArray
from picamera import PiCamera
from PIL import Image
from matplotlib import pyplot

import time
import io

RESOLUTION = (512,512)
camera = PiCamera()
camera.resolution = RESOLUTION 
#camera.framerate = 30

stream = io.BytesIO()
rawCapture = PiRGBArray(camera, size=RESOLUTION)
print("STARTING")

for _ in camera.capture_continuous(stream, format='jpeg'):
#for frame in camera.capture_continuous(rawCapture, format='bgr', use_video_port = True):
    
    image = Image.open(stream)
     
    pyplot.imshow(image)
    pyplot.pause(0.001)
    pyplot.draw()
    print("showing")
    
    #rawCapture.truncate(0)
    stream.seek(0)
    stream.truncate()
