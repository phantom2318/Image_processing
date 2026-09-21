import ipress as ipr
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def MeanFiltering(img:np.ndarray):
    s=int(input("Enter an odd scale number of Blurring"))
    kernel=(s,s)
    filtered=cv.blur(img,kernel)
    ipr.subplot(img,filtered)

def GaussianFiltering(img:np.ndarray):
    img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
    s=int(input("Enter an odd scale number of Blurring"))
    kernel=(s,s)

    gaussian=cv.GaussianBlur(img,kernel,sigmaX=5,sigmaY=5)
    img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
    gaussian=cv.cvtColor(gaussian,cv.COLOR_BGR2RGB)
    ipr.subplot(img,gaussian)
def MedianBlurring(img:np.ndarray):
     img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
     s=int(input("Enter an odd scale number of Blurring"))

     median=cv.medianBlur(img,s)
     median=cv.cvtColor(median,cv.COLOR_BGR2RGB)
     ipr.subplot(img,median,title1="original image",title2="Median Blurred")

def BilateralBluring(img:np.ndarray):
    
    s=int(input("Enter an odd scale number of Blurring"))
    bilateral=cv.bilateralFilter(img,s,150,50)
    bilateral=cv.cvtColor(bilateral,cv.COLOR_BGR2RGB)
    img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
    ipr.subplot(img,bilateral,title1="Original image",title2="Bilateral Filtering")

""" MAIN EXECUTION"""
path=ipr.select_image()
img=cv.imread(f"{path}")
if img is None:
    raise FileNotFoundError("Image not found")
print("Enter the choice"
"\n1.Mean Filtering--->1" 
"\n2.Gaussian Filtering--->2" 
"\n3.Median Filtering--->3" 
"\n4.Bilateral Filtering--->4"
"\n5.Exit--->5"
)

choice=None
while(choice!=5):
 choice=int(input("Enter the choice --->"))
  
 if choice==1:
    MeanFiltering(img)  
 elif choice==2:
  GaussianFiltering(img)
 elif choice==3:
  MedianBlurring(img) 
 elif choice==4:
  BilateralBluring(img)
 elif choice==5:
   print("Bye....")
   exit()
 else:
    print("\n \t \t Enter Valid choice\n") 