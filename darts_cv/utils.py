import cv2
import numpy as np

def to_edges(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 1)
    canny = cv2.Canny(blur, 90, 250)
    _ret, mask = cv2.threshold(canny, 200, 255, cv2.THRESH_BINARY)
    return mask

def to_rg(img): # red + green
    image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([0 , 80, 138], dtype="uint8") # red + green
    upper = np.array([180 , 255, 255], dtype="uint8") # red + green
    mask = cv2.inRange(image, lower, upper)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)
    return opening