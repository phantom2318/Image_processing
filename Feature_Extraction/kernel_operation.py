import ipress as ipr
from matplotlib import pyplot as plot
import numpy as np
import cv2 as cv

def Define_Kernel()->np.ndarray:
    dim=int(input("Enter the dimension of kernel Array"))
    kernel=np.zeros((dim,dim))
    return kernel

def Blurring(img:np.ndarray):
    kernel=Define_Kernel()
    kernel.fill(1/9)
    blurred=cv.blur(img,kernel.shape)
    ipr.subplot(img,blurred)
    save=str(input("Do you want to save the image? (yes/no)"))
    if save.lower() =="yes":
        ipr.save_image(blurred,"Blurred image.jpg")
    else:
        pass
    return blurred
def NoiseFiltering(img:np.ndarray):
    kernel=Define_Kernel()
    kernel.fill(1)
    Filteredimg=cv.filter2D(img,ddepth=-1,kernel=kernel)
    ipr.subplot(img,Filteredimg)
    save=str(input("Do you want to save the image? (yes/no)"))
    if save.lower() =="yes":
        ipr.save_image(Filteredimg,"Noise Filtered image.jpg")
    else:
        pass
    
def Sharpening(img:np.ndarray):
    kernel=Define_Kernel()
    kernel.fill(-1)
    x,y=kernel.shape
    kernel = kernel.flatten()
    origin_point = kernel.size // 2
    kernel[origin_point]=(x*y)+1
    kernel=np.reshape(kernel,(x,y),order="F")
    sharpened=cv.filter2D(img,ddepth=-1,kernel=kernel)
    ipr.subplot(img,sharpened,title1="Original",title2="Sharpened")
    save=str(input("Do you want to save the image? (yes/no)"))
    if save.lower() =="yes":
        ipr.save_image(sharpened,"sharpened image.jpg")
    else:
        pass
    return sharpened

path=ipr.select_image()
img=cv.imread(f"{path}")

if img is None:
    raise FileNotFoundError

print("Enter the choice"
"\nBlurring--->1" 
"\nSharpening of image--->2"
"\nExit--->3"
)

choice=None
while(choice!=5):
 choice=int(input("Enter the choice --->"))
  
 if choice==1:
  Blurring(img)
 elif choice==2:
  Sharpening(img)
 elif choice==3:
   print("Bye....")
   exit() 
else:
   print("Enter valid choice.")

