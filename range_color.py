import numpy as np
import cv2

cap = cv2.VideoCapture(0)
background=0

while (cap.isOpened()):
    # for i in range(30):
    #     ret,background = cap.read()
    #     background = np.flip(background,axis=1)

    ret, img = cap.read()
    # img  = np.flip(imgaxis=1)

    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

# Range for lower red
    lower_red = np.array([39,116,195])
    upper_red = np.array([51,124,204])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)

    # Range for upper range
    lower_red = np.array([47,103,168])
    upper_red = np.array([63,112,174])
    mask2 = cv2.inRange(hsv,lower_red,upper_red)

# Generating the final mask to detect red color
    mask1 = mask1+mask2
    output = cv2.bitwise_and(img, img, mask = mask1)
	
    cv2.imshow('video',np.hstack([img, output]))
    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break
cap.release()
cv2.destroyAllWindows()
