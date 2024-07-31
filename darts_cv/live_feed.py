import numpy as np 
import cv2

cap = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)
cap3 = cv2.VideoCapture(2)

while True:
    ret, img = cap.read()
    ret2, img2 = cap2.read()
    ret3, img3 = cap3.read()

    masks = np.hstack((img, img2, img3))
    cv2.imshow('Masks', masks)
    
    if cv2.waitKey(1) == 13:
        break
cap.release()
cap2.release()
cap3.release()

cv2.destroyAllWindows()
