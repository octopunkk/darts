import cv2
import utils   
import numpy as np 

# CAM = 1

# utils.capture_raw()
# img = cv2.imread(f'capture/raw/cam{CAM}.jpg')
# # wrap = utils.wrap(f'capture/raw/cam{CAM}.jpg')
# wrapped = utils.wrap_perspective(img)
# cv2.imwrite(f'capture/wrapped/cam{CAM}.jpg', wrapped)

# rg = utils.to_rg(wrapped)
# cv2.imwrite(f'capture/rg/cam{CAM}.jpg', rg)
# center = utils.get_center(f'capture/rg/cam{CAM}.jpg')

# dartboard = utils.dartboard_only(wrapped)

# wrapped = utils.draw_point(wrapped, center)

# while True:
#     cv2.imshow('dartboard', dartboard)
#     # cv2.imshow('Wrapped', wrapped)
#     if cv2.waitKey(1) == 13:
#         break

cap = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)
cap3 = cv2.VideoCapture(2)

while True:
    ret, img = cap.read()
    ret2, img2 = cap2.read()
    ret3, img3 = cap3.read()

    wrapped = utils.wrap_perspective(img)
    wrapped2 = utils.wrap_perspective(img2)
    wrapped3 = utils.wrap_perspective(img3)

    dartboard = utils.dartboard_only(wrapped)
    dartboard2 = utils.dartboard_only(wrapped2)
    dartboard3 = utils.dartboard_only(wrapped3)

    
    cv2.imshow('Dartboard', dartboard)
    cv2.imshow('Dartboard2', dartboard2)
    cv2.imshow('Dartboard3', dartboard3)
    
    if cv2.waitKey(1) == 13:
        break

cap.release()
cap2.release()
cap3.release()




