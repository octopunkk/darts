#!/usr/bin/python

'''
This example illustrates how to use cv.ximgproc.EdgeDrawing class.

Usage:
    ed.py [<image_name>]
    image argument defaults to cam1.jpg
'''

# Python 2/3 compatibility
from __future__ import print_function

import numpy as np
import cv2 as cv
import random as rng
import sys

rng.seed(12345)

def main():
    try:
        fn = sys.argv[1]
    except IndexError:
        fn = 'cam1.jpg'

    src = cv.imread(cv.samples.findFile(fn))
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (5, 5), 3)
    # cv.imshow("source", src)

    ssrc = src.copy()*0
    lsrc = src.copy()
    esrc = src.copy()

    ed = cv.ximgproc.createEdgeDrawing()

    # you can change parameters (refer the documentation to see all parameters)
    EDParams = cv.ximgproc_EdgeDrawing_Params()
    EDParams.MinPathLength = 10     # try changing this value between 5 to 1000
    EDParams.PFmode = False         # defaut value try to swich it to True
    EDParams.MinLineLength = 60     # try changing this value between 5 to 100
    EDParams.NFAValidation = True   # defaut value try to swich it to False
    # EDParams.PFmode = False
    # EDParams.EdgeDetectionOperator = 3
    # EDParams.GradientThresholdValue = 20
    # EDParams.AnchorThresholdValue = 10
    # EDParams.ScanInterval = 10
    # EDParams.MinPathLength = 10
    # EDParams.Sigma = 1.0
    # EDParams.SumFlag = True
    # EDParams.NFAValidation = True
    # EDParams.MinLineLength = -1
    # EDParams.MaxDistanceBetweenTwoLines = 6.0
    # EDParams.LineFitErrorThreshold = 1.0 # 1.0
    # EDParams.MaxErrorThreshold = 4 # 1.3

    ed.setParams(EDParams)

    # Detect edges
    # you should call this before detectLines() and detectEllipses()
    ed.detectEdges(blur)

    segments = ed.getSegments()
    lines = ed.detectLines()
    ellipses = ed.detectEllipses()

    #Draw detected edge segments
    for i in range(len(segments)):
        color = (rng.randint(0,256), rng.randint(0,256), rng.randint(0,256))
        cv.polylines(ssrc, [segments[i]], False, color, 1, cv.LINE_8)

    # cv.imshow("detected edge segments", ssrc)

    #Draw detected lines
    if lines is not None: # Check if the lines have been found and only then iterate over these and add them to the image
        lines = np.uint16(np.around(lines))
        for i in range(len(lines)):
            cv.line(lsrc, (lines[i][0][0], lines[i][0][1]), (lines[i][0][2], lines[i][0][3]), (0, 0, 255), 1, cv.LINE_AA)

    # cv.imshow("detected lines", lsrc)

    #Draw detected circles and ellipses
    if ellipses is not None: # Check if circles and ellipses have been found and only then iterate over these and add them to the image
        for i in range(len(ellipses)):
            center = (int(ellipses[i][0][0]), int(ellipses[i][0][1]))
            axes = (int(ellipses[i][0][2])+int(ellipses[i][0][3]),int(ellipses[i][0][2])+int(ellipses[i][0][4]))
            angle = ellipses[i][0][5]
            color = (0, 0, 255)
            if ellipses[i][0][2] == 0:
                color = (0, 255, 0)
            cv.ellipse(esrc, center, axes, angle,0, 360, color, 2, cv.LINE_AA)
            print(center)

    # cv.imshow("detected circles and ellipses", esrc)
    images = np.hstack((src, ssrc, lsrc, esrc))
    cv.imshow("Edge Drawing", images)

    cv.waitKey(0)
    print('Done')


if __name__ == '__main__':
    print(__doc__)
    main()
    cv.destroyAllWindows()