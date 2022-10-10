import cv2
image=cv2.imread('angela.png')
resize_image=cv2.resize(image,(600,600),interpolation=cv2.INTER_AREA)

cv2.imshow('rgb',resize_image)

# errosion of the resize_image

import numpy as np
img=cv2.imread('angela.png')

kernel=np.ones((5,5),np.uint8)

erosion=cv2.erode(img,kernel)
print(kernel)
cv2.imshow('kernel',kernel)

# dilation
img=cv2.imread('angela.png')

kernel=np.ones((5,5),np.uint8)

dilate=cv2.dilate(img,kernel)
