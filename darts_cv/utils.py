import cv2
import numpy as np
import math


def capture_raw():
    cap = cv2.VideoCapture(0)
    cap2 = cv2.VideoCapture(1)
    cap3 = cv2.VideoCapture(2)
    
    ret, img = cap.read()
    ret2, img2 = cap2.read()
    ret3, img3 = cap3.read()
    
    cv2.imwrite('capture/raw/cam1.jpg', img)
    cv2.imwrite('capture/raw/cam2.jpg', img2)
    cv2.imwrite('capture/raw/cam3.jpg', img3)
    
    cap.release()
    cap2.release()
    cap3.release()

def wrap_perspective(img):
    # H = [[ 7.93460644e-01,  7.70655959e-02,  1.10357301e+00],[ 3.67477474e-02,  1.28620048e+00, -2.57744997e+02],[ 1.41080721e-04,  6.28638386e-04,  1.00000000e+00]]
    H = [[ 7.81730855e-01, -4.03096871e-02,  6.29875261e+02],
        [ 7.39937190e-01,  1.80790366e+00, -3.89430187e+02],
        [ 1.25142133e-04,  1.61242442e-03,  1.00000000e+00]]
    H = np.array(H)
    dst = cv2.warpPerspective(img, H, (img.shape[1] * 2, img.shape[0] * 2))
    return dst

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

def get_center(img):
    src = cv2.imread(img)
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    ed = cv2.ximgproc.createEdgeDrawing()
    EDParams = cv2.ximgproc_EdgeDrawing_Params()
    ed.setParams(EDParams)
    ed.detectEdges(gray)
    ellipses = ed.detectEllipses()
    centers = []
    if ellipses is not None: 
        for i in range(len(ellipses)):
            center = (int(ellipses[i][0][0]), int(ellipses[i][0][1]))
            centers.append(center)
    center_avg = np.mean(centers, axis=0)
    print(centers)
    print(center_avg)
    return center_avg
            
def draw_point(img, point):
    cv2.circle(img, (int(point[0]), int(point[1])), 5, (0, 0, 255), -1)
    return img

def dartboard_only(img): 
    # applies a a mask to the image to only show the dartboard
    # Bounding circle around green areas
    image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([52 , 67, 111], dtype="uint8") # green
    upper = np.array([86 , 160, 255], dtype="uint8") # green
    green_mask = cv2.inRange(image, lower, upper)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    opening = cv2.morphologyEx(green_mask, cv2.MORPH_OPEN, kernel, iterations=1)
    contours = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = contours[0] if len(contours) == 2 else contours[1]
    all_points = np.vstack(contours).squeeze()
    left = np.min(all_points[:, 0])
    right = np.max(all_points[:, 0])
    top = np.min(all_points[:, 1])
    bottom = np.max(all_points[:, 1])
    circle = cv2.minEnclosingCircle(all_points)
    # draw circle
    mask = cv2.circle(green_mask, (int(circle[0][0]), int(circle[0][1])), int(circle[1]), (255, 255, 255), -1)

    masked = cv2.bitwise_and(img, img, mask=mask)
    # crop around circle
    masked = masked[int(top):int(bottom), int(left) :int(right)]




    return masked