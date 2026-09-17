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

## Resizing the image.
def Resize(image):
  if image is None:
    path=SelectImage()
    image=cv.imread(path)

  if image is None:
    raise FileNotFoundError("Could not read the selected image.")

  fx=int(input("Enter the horizontal resizing factor:"))
  fy=int(input("Enter the vertical resizing factor:"))

  resized_image=cv.resize(image,None,fx=fx,fy=fy,interpolation=cv.INTER_AREA)
  Subplot(image,resized_image)

## Translation of image
def Translation(image):
  if image is None:
    path=SelectImage()
    image=cv.imread(path)

  if image is None:
    raise FileNotFoundError("Could not read the selected image.")

  x=int(input("Enter the horizontal translation factor:"))
  y=int(input("Enter the vertical translation factor:"))
  Translation_matrix=np.array([[1,0,x],[0,1,y]],dtype=np.float32)

  height, width = image.shape[:2]
  Translated_image=cv.warpAffine(image,Translation_matrix,(width,height))
  Subplot(image,Translated_image)

#Main Execution
path=SelectImage()
image=cv.imread(path)
Resize(image)
Translation(image)
