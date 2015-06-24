import time
import picamera

# X is number of photos, t is time interval
def timelapse(x, t):
    with picamera.PiCamera() as camera:

        for i in range(1,x+1):
            camera.start_preview()
            time.sleep(t)
            camera.capture('image' + str(i) +'.jpg')
            camera.stop_preview()

timelapse(10, 1)
