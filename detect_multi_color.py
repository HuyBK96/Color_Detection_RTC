import numpy as np
import cv2

cap = cv2.VideoCapture(0)
background=0

while (cap.isOpened()):
    ret, image = cap.read()

    hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

    boundaries = [
        ([0, 120, 70], [10, 255, 255]), #red
	    ([98,109, 20], [112,255, 255]) #blue
    ]

    for (lower, upper) in boundaries:
        lower = np.array(lower)
        upper = np.array(upper)
        mask = cv2.inRange(hsv, lower, upper)
        output = cv2.bitwise_and(image, image, mask = mask)
       
    
    cv2.imshow('video',np.hstack([image, output]))
    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break
cap.release()
cv2.destroyAllWindows()
