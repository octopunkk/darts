import cv2
import random

image = cv2.imread('Dartboard--side.jpg')

# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.medianBlur(image, 5)
blur2 = cv2.GaussianBlur(blur, (9, 9), 0)

canny = cv2.Canny(blur2, 200, 200, 3)

ret, tresh = cv2.threshold(blur, 70, 255, cv2.THRESH_BINARY)
cv2.imshow('blur', tresh)

ret, tresh = cv2.threshold(blur, 70, 255, cv2.THRESH_BINARY)
cv2.imshow('blur2', tresh)

ret, treshc = cv2.threshold(canny, 70, 255, cv2.THRESH_BINARY)
cv2.imshow('canny', treshc)

cnts = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print(len(cnts))

cnts = cnts[0] if len(cnts) == 2 else cnts[1]

point1 = (25, 50)
point2 = (200, 250)
point3 = (200, 350)


# Perform check if point is inside contour/shape
for c in cnts:
    area = cv2.contourArea(c)
    if(area > 1000):
        print(area)         

        cv2.drawContours(image, [c], -1, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 2)
        result1 = cv2.pointPolygonTest(c, point1, False)
        result2 = cv2.pointPolygonTest(c, point2, False)
        result3 = cv2.pointPolygonTest(c, point3, False)

# Draw points
cv2.circle(image, point1, 8, (100, 100, 255), -1)
cv2.putText(image, 'point1', (point1[0] -10, point1[1] -20), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 0), lineType=cv2.LINE_AA)
cv2.circle(image, point2, 8, (200, 100, 55), -1)
cv2.putText(image, 'point2', (point2[0] -10, point2[1] -20), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 0), lineType=cv2.LINE_AA)
cv2.circle(image, point3, 8, (150, 50, 155), -1)
cv2.putText(image, 'point3', (point3[0] -10, point3[1] -20), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 0), lineType=cv2.LINE_AA)

print('point1:', result1)
print('point2:', result2)
print('point3:', result3)
cv2.imshow('image2', image)
cv2.waitKey()