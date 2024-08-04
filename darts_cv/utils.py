import cv2
import numpy as np
import math
from time import sleep
import sys


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

def wrap_perspective(img, camIndex):
    if (camIndex == 1):
        H = [[ 7.81730855e-01, -4.03096871e-02,  6.29875261e+02],
            [ 7.39937190e-01,  1.80790366e+00, -3.89430187e+02],
            [ 1.25142133e-04,  1.61242442e-03,  1.00000000e+00]]

    elif (camIndex == 2):
        H = [[-6.50825247e-01,  1.40662289e-01,  1.28993838e+03],
            [ 3.90272856e-01, -5.55831573e-01,  3.26722339e+02],
            [-3.97107150e-05,  1.12643427e-03,  1.00000000e+00]]
    elif (camIndex == 3):
        H = [[-6.88185097e-01,  2.08111168e-01,  1.13402125e+03],
            [ 2.78178572e-01, -7.21333283e-01,  4.59429677e+02],
            [ 2.29027697e-05,  1.09023522e-03,  1.00000000e+00]]
       
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
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
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
    if center_avg.size == 0:
        return None
    else:
        return (int(center_avg[0]), int(center_avg[1]))
            
def draw_point(img, point):
    cv2.circle(img, (int(point[0]), int(point[1])), 5, (0, 0, 255), -1)
    return img

def get_dartboard_mask(img):
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
    circle = cv2.minEnclosingCircle(all_points)
    # draw circle
    mask = cv2.circle(green_mask, (int(circle[0][0]), int(circle[0][1])), int(circle[1]), (255, 255, 255), -1)
    return mask, circle

def crop_dartboard(img, mask, circle):
    x, y, r = int(circle[0][0]), int(circle[0][1]), int(circle[1])
    masked = cv2.bitwise_and(img, img, mask=mask)
    masked = masked[y-r:y+r, x-r:x+r]
    return masked

def get_masks():
    masks = []
    circles = []
    for i in range(3):
        cap = cv2.VideoCapture(i)
        _ret, img = cap.read()
        wrapped = wrap_perspective(img, i+1)
        mask, circle = get_dartboard_mask(wrapped)
        masks.append(mask)
        circles.append(circle)
        sys.stdout.write('\r')
        sys.stdout.write("[%-30s] %d%%" % ('='*(i+1)*10, 33*(i+1)+1))
        sys.stdout.flush()
        cap.release()
    sys.stdout.write('\n')
    return masks, circles

def get_centers(masks, circles):
    centers_avg = [[] for i in range(3)]
    for j in range(10):
        for i in range(3):
            cap = cv2.VideoCapture(i)
            _ret, img = cap.read()
            wrapped = wrap_perspective(img, i+1)
            masked = crop_dartboard(wrapped, masks[i], circles[i])
            dartboard = cv2.resize(masked, (400, 400))
            center = get_center(dartboard)
            # Center should be around the middle of the dartboard, if not, it's not the dartboard
            if center is not None and center[0] > 195 and center[0] < 206 and center[1] > 195 and center[1] < 206: 
                centers_avg[i].append(center)
            cap.release()
            sys.stdout.write('\r')
            sys.stdout.write("[%-30s] %d%%" % ('='*((j)*3 + i+1), (10*(j)) + 3*(i+1)+1))
            sys.stdout.flush()
    
    sys.stdout.write('\n')
    centers = [None, None, None]
    for i in range(3):
        centers[i] = np.round(np.mean(centers_avg[i], axis=0)).astype(int)

    return centers

def draw_rings(img, center):
    outer_ring = int((162*200)/170)
    inner_ring_out = int((108*200)/170)
    inner_ring_int = int((99*200)/170)
    bullseye = int((16*200)/170)
    double_bullseye = int((6*200)/170)
    thickness = 1  
    color = (0, 0, 255)
    cv2.circle(img, center, outer_ring, color, thickness)
    cv2.circle(img, center, inner_ring_out, color, thickness)
    cv2.circle(img, center, inner_ring_int, color, thickness)
    cv2.circle(img, center, bullseye, color, thickness)
    cv2.circle(img, center, double_bullseye, color, thickness)
    return img

def get_line(img, center):
    rg = to_rg(img)
    edges = to_edges(rg)
    
    return img