import numpy as np
import cv2 as cv
from tkinter import Tk,filedialog
import matplotlib.pyplot as plt
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

path=SelectImage()
image=cv.imread(path)

if image is None:
   raise FileNotFoundError(f"Could not read image: {path}")
(h,w)=image.shape[0:2]
aspect=w/h

##after resizing height to it's double
h=int(h*2)
w=int((aspect*h))
dimension=(w,h)

r_image=cv.resize(image,dimension,interpolation=cv.INTER_AREA)
Subplot(image,r_image)
