

import numpy as np
import cv2 as cv
filename = '3.6conejo.jpg'
img = cv.imread(filename)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# find Harris corners
gray = np.float32(gray)
dst = cv.cornerHarris(gray,2,3,0.04)
dst = cv.dilate(dst,None)
ret, dst = cv.threshold(dst,0.01*dst.max(),255,0)
dst = np.uint8(dst)
# find centroids
ret, labels, stats, centroids = cv.connectedComponentsWithStats(dst)
# define the criteria to stop and refine the corners
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 100, 0.001)
corners = cv.cornerSubPix(gray,np.float32(centroids),(5,5),(-1,-1),criteria)
# Now draw them
minimo=int(corners[:,1].min())

#linea azul BGR
cv.line(img,(200,minimo),(400,minimo),(255,0,0),1)
maximo=int(corners[:,1].max())
cv.line(img,(200,maximo),(400,maximo),(255,0,0),1)
res = np.hstack((centroids,corners))
res = np.int0(res)
img[res[:,1],res[:,0]]=[0,0,255]
img[res[:,3],res[:,2]] = [0,255,0]
print(f'La altura total del conejo es de {maximo-minimo} pixeles')
cv.imshow('Esquinas del conejo', img)
  
# De-allocate any associated memory usage 
if cv.waitKey(0) & 0xff == 27:
    cv.destroyAllWindows()