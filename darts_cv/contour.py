import numpy as np
import cv2

img = cv2.imread('dartboard--side.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
edges= cv2.Canny(blur, 50, 200)

# ret , thrash = cv2.threshold(imgGry, 240 , 255, cv2.CHAIN_APPROX_NONE)
ret, thrash = cv2.threshold(edges, 70, 255, cv2.THRESH_BINARY)
cv2.imshow('image', thrash)
contours , hierarchy = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

cv2.waitKey(0)
cv2.destroyAllWindows()