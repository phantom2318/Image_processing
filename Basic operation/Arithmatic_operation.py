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

def Substraction(img1: np.ndarray,img2: np.ndarray):
  ipr.subplot(img1,img2,title1="image 1",title2="image 2")
  substraction12=cv.subtract(img1,img2)
  substraction21=cv.subtract(img2,img1)

  substraction12=cv.cvtColor(substraction12,cv.COLOR_BGR2RGB)
  substraction21=cv.cvtColor(substraction21,cv.COLOR_BGR2RGB)

  ipr.subplot(substraction12,substraction21,title1="img`1`-img`2`",title2="img`2`-img`1`")

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
Substraction(img1,img2)
img_and_12=cv.bitwise_and(img1,img2)
img_or_12=cv.bitwise_or(img1,img2)
img_xor_12=cv.bitwise_xor(img1,img2)
img_not_1=cv.bitwise_not(img1)

img_and_12=cv.cvtColor(img_and_12,cv.COLOR_BGR2RGB)
img_or_12=cv.cvtColor(img_or_12,cv.COLOR_BGR2RGB)
img_xor_12=cv.cvtColor(img_xor_12,cv.COLOR_BGR2RGB)
img_not_1=cv.cvtColor(img_not_1,cv.COLOR_BGR2RGB)

plt.subplot(2,2,1)
plt.imshow(img_and_12)
plt.title("AND operation")

plt.subplot(2,2,3)
plt.imshow(img_or_12)
plt.title("OR operation")

plt.subplot(2,2,2)
plt.imshow(img_xor_12)
plt.title("XOR operation")

plt.subplot(2,2,4)
plt.imshow(img_not_1)
plt.title("NOT operation")

plt.show()