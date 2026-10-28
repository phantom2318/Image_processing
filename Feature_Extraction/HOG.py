import ipress as ip
import numpy as np
import cv2 as cv
from skimage import feature as sk

img_path=ip.select_image()
img=cv.imread(f"{img_path}")

if img is None:
	raise ValueError(f"Could not load image: {img_path}")

img=cv.resize(img,(int(img.shape[1]/5),int(img.shape[0]/5)))
img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
(HOG,hog_img)=sk.hog(img,orientations=9,pixels_per_cell=(8,8),cells_per_block=(2,2),visualize=True,transform_sqrt=True,block_norm="L2-Hys",feature_vector=True)

print(f"image_dimension {img.shape}")
print(f"HOG_dimension {HOG.shape}")

ip.subplot(img,hog_img,title1="Original Image",title2="hog Image")