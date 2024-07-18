import numpy as np 
import cv2
cap = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)
cap3 = cv2.VideoCapture(2)

while True:
    ret, img = cap.read()
    ret2, img2 = cap2.read()
    ret3, img3 = cap3.read()
    
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # blur = cv2.GaussianBlur(gray, (5, 5), 0)
    # canny = cv2.Canny(blur, 10, 70)
    # ret, mask = cv2.threshold(canny, 70, 255, cv2.THRESH_BINARY)
    # cv2.imshow('image', mask)

    # gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    # blur2 = cv2.GaussianBlur(gray2, (5, 5), 0)
    # canny2 = cv2.Canny(blur2, 10, 70)
    # ret2, mask2 = cv2.threshold(canny2, 70, 255, cv2.THRESH_BINARY)
    # cv2.imshow('image2', mask2)

    # gray3 = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
    # blur3 = cv2.GaussianBlur(gray3, (5, 5), 0)
    # canny3 = cv2.Canny(blur3, 10, 70)
    # ret3, mask3 = cv2.threshold(canny3, 70, 255, cv2.THRESH_BINARY)
    # cv2.imshow('image3', mask3)

    cv2.imshow('Video feed', img)
    cv2.imshow('Video feed2', img2)
    cv2.imshow('Video feed3', img3)
    
    if cv2.waitKey(1) == 13:
        break
cap.release()
cap2.release()
cap3.release()

cv2.destroyAllWindows()

# Save a picture every 1 second
# import cv2
# import time
# cap = cv2.VideoCapture(0)
# i = 0
# while True:
#     ret, img = cap.read()
#     cv2.imshow('Video feed', img)
#     if cv2.waitKey(1) == 13:
#         break
#     time.sleep(1)
#     cv2.imwrite('image'+str(i)+'.jpg', img)
#     i += 1
# cap.release()
# cv2.destroyAllWindows()

# import cv2
# import matplotlib.pyplot as plt


# image= cv2.imread('Dartboard.jpg')
# original_image= image

# gray= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# blur = cv2.GaussianBlur(gray, (5, 5), 0)
# edges= cv2.Canny(blur, 10, 70)

# ret, mask = cv2.threshold(edges, 70, 255, cv2.THRESH_BINARY)
# cv2.imshow('image', mask)

# contours, hierarchy= cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# cnt = contours[0]
# epsilon = 0.1*cv2.arcLength(cnt,True)
# approx = cv2.approxPolyDP(cnt,epsilon,True)

# sorted_contours= sorted(contours, key=cv2.contourArea, reverse= True)



# for (i,c) in enumerate(sorted_contours):
#     M= cv2.moments(c)
#     cx= int(M['m10']/M['m00'])
#     cy= int(M['m01']/M['m00'])
#     cv2.putText(image, text= str(i+1), org=(cx,cy),
#             fontFace= cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,0,0),
#             thickness=2, lineType=cv2.LINE_AA)

    
# plt.imshow(image)
# plt.show()





# for contour in contours:
#     approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
#     cv2.drawContours(img, [approx], 0, (0, 0, 0), 5)
#     x = approx.ravel()[0]
#     y = approx.ravel()[1] - 5
#     if len(approx) == 3:
#         cv2.putText( img, "Triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0) )
#     elif len(approx) == 4 :
#         x, y , w, h = cv2.boundingRect(approx)
#         aspectRatio = float(w)/h
#         print(aspectRatio)
#         if aspectRatio >= 0.95 and aspectRatio < 1.05:
#             cv2.putText(img, "square", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

#         else:
#             cv2.putText(img, "rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

#     elif len(approx) == 5 :
#         cv2.putText(img, "pentagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
#     elif len(approx) == 10 :
#         cv2.putText(img, "star", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
#     else:
#         cv2.putText(img, "circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

# cv2.imshow('shapes', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()