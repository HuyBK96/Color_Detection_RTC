import numpy as np
import cv2

cap = cv2.VideoCapture(0)
background=0

while (cap.isOpened()):
    ret, img = cap.read()

    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

# Range for lower red
    lower_red = np.array([0,120,70])
    upper_red = np.array([10,255,255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)

    # Range for upper range
    lower_red = np.array([170,120,70])
    upper_red = np.array([180,255,255])
    mask2 = cv2.inRange(hsv, lower_red, upper_red)

# # Range for lower yellow
#     lower_yellow = np.array([20,190,20])
#     upper_yellow = np.array([30,255,255])
#     mask1 = cv2.inRange(hsv, lower_yellow, upper_yellow)

#     # Range for upper range
#     lower_yellow = np.array([190,190,20])
#     upper_yellow = np.array([200,255,255])
#     mask2 = cv2.inRange(hsv, lower_yellow, upper_yellow)

# # Range for lower blue
#     lower_blue = np.array([98,109,20])
#     upper_blue = np.array([112,255,255])
#     mask1 = cv2.inRange(hsv, lower_blue, upper_blue)

#     # Range for upper range
#     lower_blue = np.array([170,109,20])
#     upper_blue = np.array([180,255,255])
#     mask2 = cv2.inRange(hsv, lower_blue, upper_blue)

# Generating the final mask to detect red color
    mask1 = mask1+mask2
    output = cv2.bitwise_and(img, img, mask = mask1)
	
    cv2.imshow('video',np.hstack([hsv, output]))
    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break
cap.release()
cv2.destroyAllWindows()
