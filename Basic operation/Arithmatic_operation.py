import ipress as ipr
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

def simpleAddition(img1:np.ndarray,img2:np.ndarray):
  ipr.subplot(img1,img2,title1="image 1",title2="image 2")
  addition=cv.add(img1,img2)
  addition=cv.cvtColor(addition,cv.COLOR_BGR2RGB)
  plt.imshow(addition)
  plt.title("Addition os both images")
  plt.show()

def WeightedAddition(img1:np.ndarray,img2:np.ndarray):
 ipr.subplot(img1,img2,title1="image 1",title2="image 2")
 Waddition = cv.addWeighted(img1, 0.5, img2, 0.5, 0)
 Waddition=cv.cvtColor(Waddition,cv.COLOR_BGR2RGB)
 plt.imshow(Waddition)
 plt.show()

path1=ipr.select_image()
path2=ipr.select_image()

img1=cv.imread(f"{path1}")
img2=cv.imread(f"{path2}")

if img1 is None:
	raise ValueError("Failed to load the first image")
if img2 is None:
	raise ValueError("Failed to load the first image")

img1 = cv.resize(img1, (1000, 1000), interpolation=cv.INTER_AREA)
img2 = cv.resize(img2, (1000, 1000), interpolation=cv.INTER_AREA)

simpleAddition(img1,img2)
WeightedAddition(img1,img2)