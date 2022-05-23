import numpy as np
import cv2

cap = cv2.VideoCapture('http://192.168.43.1:4747/video')

while(True):
    ret, frame = cap.read()

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
