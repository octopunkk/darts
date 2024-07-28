# Capture image from all 3 camera and save it
import utils
import cv2

cap = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)
cap3 = cv2.VideoCapture(2)

ret, img = cap.read()
ret2, img2 = cap2.read()
ret3, img3 = cap3.read()

# mask = utils.to_edges(img)
# mask2 = utils.to_edges(img2)
# mask3 = utils.to_edges(img3)

# opening = utils.to_rg(img)
# opening2 = utils.to_rg(img2)
# opening3 = utils.to_rg(img3)

cv2.imwrite('capture/raw/cam1.jpg', img)
cv2.imwrite('capture/raw/cam2.jpg', img2)
cv2.imwrite('capture/raw/cam3.jpg', img3)

# cv2.imwrite('capture/cam1_edges.jpg', mask)
# cv2.imwrite('capture/cam2_edges.jpg', mask2)
# cv2.imwrite('capture/cam3_edges.jpg', mask3)

# cv2.imwrite('capture/cam1_rg.jpg', opening)
# cv2.imwrite('capture/cam2_rg.jpg', opening2)
# cv2.imwrite('capture/cam3_rg.jpg', opening3)

cap.release()
cap2.release()
cap3.release()
