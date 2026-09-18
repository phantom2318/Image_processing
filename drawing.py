import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from PIL import Image
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
def Subplot(image1=None,image2=None,cmap1=None,cmap2=None,title1="Image-1",title2="Image-2"):

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
   plt.imshow(image1,cmap=cmap1)
   plt.title(title1)

   plt.subplot(1,2,2)
   plt.imshow(image2,cmap=cmap2)
   plt.title(title2)

   plt.show()

###Drawing a line.
def Line(image:np.ndarray)->np.ndarray:
  thickness=int(input(("Enter the thickness of the line")))
  start=(0,0)
  end=(image.shape[1],image.shape[0])
  image=cv.line(image,start,end,[255,0,0],thickness)
  return image

###Drawing Rectangle
def Rectangle(image: np.ndarray)->np.ndarray:
    thickness=int(input(("Enter the thickness of the line")))
    start=(0,0)
    end=(50,100)
    image=cv.rectangle(image,start,end,[255,0,0],thickness)
    return image
path=SelectImage()
image=cv.imread(path)
image=Line(image)
cv.imshow('Lined',image)
cv.waitKey(0)

image=Rectangle(image)
cv.imshow('Rectangled',image)
cv.waitKey(0)