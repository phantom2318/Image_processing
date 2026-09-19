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
   if cmap1!="gray":
    image1=cv.cvtColor(image1,cv.COLOR_BGR2RGB)
   if image2 is None:
     f_image2=SelectImage()
     image2=cv.imread(f"{f_image2}")

     if image2 is None:
       raise FileNotFoundError(f"Could not read image: {f_image2}")
   if cmap1!="gray":
    image2=cv.cvtColor(image2,cv.COLOR_BGR2RGB)
   
   plt.subplot(1,2,1)
   plt.imshow(image1,cmap=cmap1)
   plt.title(title1)

   plt.subplot(1,2,2)
   plt.imshow(image2,cmap=cmap2)
   plt.title(title2)

   plt.show()

## Resizing the image.
def Resize(image: np.ndarray):
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
def Translation(image: np.ndarray):
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

## Rotation of image

def Rotation(image: np.ndarray):
  dcn=float(input("Enter the angle of rotation"))
  w,h=image.shape[0:2]
  center=(h/2,w/2)
  rotated_matrix=cv.getRotationMatrix2D(center,dcn,1)
  rotated_image=cv.warpAffine(image,rotated_matrix,(w,h))
  Subplot(image,rotated_image)

## Flipping of image
def Fliping(image: np.ndarray):
  dcn=int(input("Enter the direction"))
  flipped_image=cv.flip(image,dcn)
  Subplot(image,flipped_image,title1="Original image",title2="Flipped image")
#Main Execution
path=SelectImage()
image=cv.imread(path)
if image is None:
  raise FileNotFoundError(f"Could not read image: {path}")
print("Enter the choice"
"\n1.Resize--->1" 
"\n2.translation of image--->2" 
"\n3.Rotation--->3" 
"\n4.Flipping--->4"
"\n5.Exit--->5"
)

choice=None
while(choice!=5):
 choice=int(input("Enter the choice --->"))
  
 if choice==1:
  Resize(image)
 elif choice==2:
  Translation(image)
 elif choice==3:
  Rotation(image) 
 elif choice==4:
  Fliping(image)
 elif choice==5:
   print("Bye....")
   exit() 