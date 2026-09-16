import numpy as np
from PIL import Image
import cv2 as cv
import matplotlib.pyplot as plt
from tkinter import filedialog,Tk

#Select an image from Device
def SelectImage()->str:
  root = Tk()
  root.withdraw()
  file_path = filedialog.askopenfilename(
    title="Select an image",
    filetypes=[
      ("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff"),
      ("All files", "*.*")
    ]
  )
  return file_path

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


image=np.array([])
print(image.shape)
z=np.array([[input("Enter the RGB value")]])
image=np.full((300,400),z)
print(image.shape)
print(image)

Subplot(image,None,'gray')