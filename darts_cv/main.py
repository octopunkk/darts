import cv2
import utils   
import numpy as np 

cap = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)
cap3 = cv2.VideoCapture(2)

while True:
    ret, img = cap.read()
    ret2, img2 = cap2.read()
    ret3, img3 = cap3.read()

    wrapped = utils.wrap_perspective(img, 1)
    wrapped2 = utils.wrap_perspective(img2, 2)
    wrapped3 = utils.wrap_perspective(img3, 3)

    dartboard = utils.dartboard_only(wrapped)
    dartboard2 = utils.dartboard_only(wrapped2)
    dartboard3 = utils.dartboard_only(wrapped3)

    dartboard = cv2.resize(dartboard, (400, 400))
    dartboard2 = cv2.resize(dartboard2, (400, 400))
    dartboard3 = cv2.resize(dartboard3, (400, 400))

    dartboards = np.hstack((dartboard, dartboard2, dartboard3))
    cv2.imshow('Dartboards', dartboards)

    if cv2.waitKey(1) == 13:
        break

cap.release()
cap2.release()
cap3.release()




