import numpy as np
import cv2

# Load image and HSV color threshold
image = cv2.imread('capture/raw/cam1.jpg')
original = image.copy()
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower = np.array([0 , 80, 138], dtype="uint8") # red + green
upper = np.array([180 , 255, 255], dtype="uint8") # red + green

# lower = np.array([0 , 0, 180], dtype="uint8") # white
# upper = np.array([128 , 70, 255], dtype="uint8") # white

mask = cv2.inRange(image, lower, upper)
detected = cv2.bitwise_and(original, original, mask=mask)

# Remove noise
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)

# Find contours 
cnts = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
for c in cnts:
    area = cv2.contourArea(c)
    (x,y),radius = cv2.minEnclosingCircle(c)
    center = (int(x),int(y))
    radius = int(radius)
    cv2.circle(original,center,radius,(0,255,0),2)
    cv2.drawContours(original,[c], 0, (0,0,0), 2)


# cv2.imshow('mask', mask)
cv2.imshow('original', original)
# cv2.imshow('opening', opening)
# cv2.imshow('detected', detected)
cv2.waitKey()