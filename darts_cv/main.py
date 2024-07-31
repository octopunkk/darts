import cv2
import utils   
import numpy as np 

masks, circles = utils.get_masks()
caps = [cv2.VideoCapture(i) for i in range(3)]

while True:
    dartboards = []
    for i in range(3):
        _ret, img = caps[i].read()
        wrapped = utils.wrap_perspective(img, i+1)
        masked = utils.crop_dartboard(wrapped, masks[i], circles[i])
        dartboard = cv2.resize(masked, (400, 400))
        dartboards.append(dartboard)

    dartboards = np.hstack(dartboards)
    cv2.imshow('Dartboards', dartboards)

    if cv2.waitKey(1) == 13:
        break

for cap in caps:
    cap.release()



