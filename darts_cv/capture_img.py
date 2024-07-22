# Capture image from all 3 camera and save it
import to_edges
import cv2

cap = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)
cap3 = cv2.VideoCapture(2)

ret, img = cap.read()
ret2, img2 = cap2.read()
ret3, img3 = cap3.read()

mask = to_edges.to_edges(img)
mask2 = to_edges.to_edges(img2)
mask3 = to_edges.to_edges(img3)

cv2.imwrite('cam1.jpg', img)
cv2.imwrite('cam2.jpg', img2)
cv2.imwrite('cam3.jpg', img3)

cv2.imwrite('cam1_edges.jpg', mask)
cv2.imwrite('cam2_edges.jpg', mask2)
cv2.imwrite('cam3_edges.jpg', mask3)

cap.release()
cap2.release()
cap3.release()
