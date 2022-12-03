import cv2
import numpy as np
from imutils.video import VideoStream
from yolodetect import YoloDetect

video = VideoStream(src=0).start()
# new model Yolo
model = YoloDetect()
detect = False

while True:
    frame = video.read()
    frame = cv2.flip(frame, 1)
    if detect:
        frame = model.detect(frame=frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    detect = True
    # Hien anh ra man hinh
    cv2.imshow("Intrusion Warning Application", frame)
video.stop()
cv2.destroyAllWindows()

