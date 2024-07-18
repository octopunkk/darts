# Capture image from all 3 camera and save it

import cv2

cap = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)
cap3 = cv2.VideoCapture(2)

ret, img = cap.read()
ret2, img2 = cap2.read()
ret3, img3 = cap3.read()

cv2.imwrite('cam1.jpg', img)
cv2.imwrite('cam2.jpg', img2)
cv2.imwrite('cam3.jpg', img3)

cap.release()
cap2.release()
cap3.release()
