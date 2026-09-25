import ipress as ipr
from matplotlib import pyplot as plot
import numpy as np
import cv2 as cv

def Define_Kernel()->np.ndarray:
    dim=int(input("Enter the dimension of kernel Array"))
    kernel=np.ones(dim*dim)
    kernel=np.reshape(kernel,(dim,dim),"C")
    return kernel

def Blurring(img:np.ndarray):
    kernel=Define_Kernel()
    kernel.fill(2/3)
    blurred=cv.blur(img,kernel.shape)
    ipr.subplot(img,blurred)
    return blurred
def NoiseFiltering(img:np.ndarray):
    kernel=Define_Kernel()
    Filteredimg=cv.filter2D(img,ddepth=-1,kernel=kernel)
    ipr.subplot(img,Filteredimg)
    
def Sharpening(img:np.ndarray):
    kernel=Define_Kernel()
    kernel.fill(-1)
    x,y=kernel.shape
    origin_point=(x+y)/2
    kernel = kernel.flatten()
    origin_point = kernel.size // 2
    kernel[origin_point]=int(input("Enter the level of Sharpness"))
    np.reshape(kernel,(x,y),"C")
    sharpened=cv.filter2D(img,ddepth=-1,kernel=kernel)
    ipr.subplot(img,sharpened,title1="Original",title2="Sharpened")
    return sharpened

path=ipr.select_image()
img=cv.imread(f"{path}")

if img is None:
    raise FileNotFoundError

print("Enter the choice"
"\n1.Blurring--->1" 
"\n2.Sharpening of image--->2"
"\n5.Exit--->5"
)

choice=None
while(choice!=5):
 choice=int(input("Enter the choice --->"))
  
 if choice==1:
  Blurring(img)
 elif choice==2:
  Sharpening(img)
 elif choice==5:
   print("Bye....")
   exit() 
