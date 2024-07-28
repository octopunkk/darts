import numpy as np
import cv2

def mouseClickHandler( event, x, y, flags, pointList ):
	global H
	if event == cv2.EVENT_LBUTTONDOWN:
		if len( pointList ) >= 4:
			del pointList[:]
		pointList.append( ( x, y ) )
		if len( pointList ) == 4:
			H = None

cv2.namedWindow( 'src' )
cv2.namedWindow( 'dst' )
H = None # the resulting homography matrix.
im = cv2.imread( 'capture/raw/cam1.jpg' ) # a picture of Notre Dame cathedral; substitute your own image as needed.
h, w, channels = im.shape # get image attributes.
pinchLeft = int( w * 0.10 )
pinchRight = w - 1 - pinchLeft
pSrc = [( 0, 0 ), ( w - 1, 0 ), ( w - 1, h - 1 ), ( 0, h - 1 )]
# pDst = [( pinchLeft, 0 ), ( pinchRight, 0 ), ( w - 1, h - 1 ), ( 0, h - 1 )]

centerX = int(w / 2)
centerY = int(h / 2)
dstSize = 150
pDst = [( centerX - dstSize, centerY - dstSize ), ( centerX + dstSize, centerY - dstSize ), ( centerX + dstSize, centerY + dstSize ), ( centerX - dstSize, centerY + dstSize )]
dst = np.zeros( im.shape, dtype = np.uint8 )
dstD = dst.copy()
print( '\nPress ESC to quit.\n')
cv2.setMouseCallback( 'src', mouseClickHandler, pSrc )
cv2.setMouseCallback( 'dst', mouseClickHandler, pDst )
while( 1 ):
	imD = im.copy()
	for p in pSrc:
		cv2.circle( imD, p, 2, ( 255, 0, 0 ), -1 )
	for p in pDst:
		cv2.circle( dstD, p, 2, ( 255, 0, 0 ), -1 )
	if len( pSrc ) == 4 and len( pDst ) == 4 and H == None:
		H = cv2.findHomography( np.array( pSrc, dtype = np.float32 ), np.array( pDst, dtype = np.float32 ), cv2.LMEDS )
		dstD = cv2.warpPerspective( imD, H[0], ( dstD.shape[1], dstD.shape[0] ) )
		msg = 'src:\n' + str( np.array( pSrc, dtype = np.float32 ) )
		msg += '\ndst:\n' + str( np.array( pDst, dtype = np.float32 ) )
		msg += '\nH:\n' + ''.join( map( str, H ) ) + '\n'
		print(msg)
	cv2.imshow( 'src', imD )
	cv2.imshow( 'dst', dstD )
	key = cv2.waitKey( 1 )
	if key == 27:
		exit( 0 )