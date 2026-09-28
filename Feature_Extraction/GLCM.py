import cv2 as cv
import numpy as np
import ipress as ipr
from skimage import feature as sk

path = ipr.select_image()
image=cv.imread(f"{path}")

if image is None:
    raise FileNotFoundError
image=cv.cvtColor(image,cv.COLOR_BGR2GRAY)

glcm=sk.graycomatrix(image,[5],[0,np.pi/2,np.pi,np.pi/3,np.pi/5])

print(glcm)
print(glcm.size)
print(glcm.shape)
print(glcm[255,255,0,1])
print(glcm[255,255,0,0])
print(glcm[255,254,0,0])
print(glcm[255,254,0,1])

