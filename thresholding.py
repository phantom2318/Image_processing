import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from tkinter import Tk,filedialog

#Select an image from Device
def SelectImage()->str:
 root=Tk()
 root.withdraw()
 file_path = filedialog.askopenfilename(
    title="Select an image",
    filetypes=[
        ("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff"),
        ("All files", "*.*")
    ]
    )
 #if image is not selected by the user
 if not file_path:
    print("No image selected.")
    exit()
 return file_path

#plotting an image
def Subplot(image1=None,image2=None):

   if image1 is None:
    f_image1=SelectImage()
    image1=cv.imread(f"{f_image1}")
    if image1 is None:
       raise FileNotFoundError(f"Could not read image: {f_image1}")
    image1=cv.cvtColor(image1,cv.COLOR_BGR2RGBA)
   if image2 is None:
     f_image2=SelectImage()
     image2=cv.imread(f"{f_image2}")
     if image2 is None:
       raise FileNotFoundError(f"Could not read image: {f_image2}")
     image2=cv.cvtColor(image2,cv.COLOR_BGR2RGBA)

   plt.subplot(1,2,1)
   plt.imshow(image1)
   plt.title("Image 1")

   plt.subplot(1,2,2)
   plt.imshow(image2)
   plt.title("Image 2")

   plt.show()

file_path = SelectImage()
image = cv.imread(file_path,cv.IMREAD_GRAYSCALE)


if image is None:
    raise FileNotFoundError(f"Could not read image: {file_path}")
##image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
ret, thresh1 = cv.threshold(image, 127, 255, cv.THRESH_BINARY)
ret, thresh2 = cv.threshold(image, 127, 255, cv.THRESH_BINARY_INV)
ret, thresh3 = cv.threshold(image, 127, 255, cv.THRESH_TRUNC)
ret, thresh4 = cv.threshold(image, 127, 255, cv.THRESH_TOZERO)
ret, thresh5 = cv.threshold(image, 127, 255, cv.THRESH_TOZERO_INV)
#ret, thresh6 = cv.threshold(image, 127, 255, cv.THRESH_TRIANGLE)

title=["Image","Binary","Trunc","TOzero","TozerINV","Triangle"]
img=[image,thresh1,thresh2,thresh3,thresh4,thresh5]

for i in range(6):
  plt.subplot(2,3,i+1)
  plt.imshow(img[i],'gray',vmin=0,vmax=255)
  plt.title(f"{title[i]}")

plt.show()

##Adaptive thresholding

th1=cv.adaptiveThreshold(image,255,cv.ADAPTIVE_THRESH_MEAN_C,
                         cv.THRESH_BINARY,11,2)
th2=cv.adaptiveThreshold(image,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                         cv.THRESH_BINARY,11,2)
title=["Image","Global Binary","Mean C","Gaussian C"]
img=[image,thresh1,th1,th2]

for i in range(4):
  plt.subplot(2,2,i+1)
  plt.imshow(img[i],'gray')
  plt.title(f"{title[i]}")
plt.show()