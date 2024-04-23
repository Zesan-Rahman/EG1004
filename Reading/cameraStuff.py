from picamera2 import Picamera2, Preview
import time

picam2 = Picamera2()
#setup configuration, highres = 1920x1080, minimum res = 640x480
camera_config = picam2.create_still_configuration(main={"size": (1920, 1080)}, lores={"size": (640, 480)}, display="lores")
#configure camera
picam2.configure(camera_config)
picam2.start_preview(Preview.QTGL)
picam2.start()
time.sleep(2)
picam2.capture_file("test.jpg")