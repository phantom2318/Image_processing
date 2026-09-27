import ipress as ipr
import numpy as np
import cv2 as cv

def BilateralBluring(img:np.ndarray):
    
    s=int(input("Enter an odd scale number of Blurring"))
    bilateral=cv.bilateralFilter(img,s,150,50)
    bilateral=cv.cvtColor(bilateral,cv.COLOR_BGR2RGB)
    img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
    ipr.subplot(img,bilateral,title1="Original image",title2="Bilateral Filtering")
    return bilateral

def SobelDetection(img:np.ndarray):
    #dir=input("Enter the direction of gradient")
    img=BilateralBluring(img)
    sobelX=cv.Sobel(img,cv.CV_64F,1,0,ksize=3)
    sobelY=cv.Sobel(img,cv.CV_64F,0,1,ksize=3)
    detectedImage=cv.max(sobelX,sobelY)
    detectedImage=cv.convertScaleAbs(detectedImage)
    detectedImage=cv.cvtColor(detectedImage,cv.COLOR_BGR2RGB)
    img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
    ipr.subplot(img,detectedImage,title1="Original image",title2="Sobel Detection")

def LaplaceDetection(img:np.ndarray):
    img=BilateralBluring(img)
    laplace=cv.Laplacian(img,cv.CV_64F)
    laplace=np.uint8(np.absolute(laplace))
    ipr.subplot(img,laplace,title1="Original image",title2="Laplace Detection")

def CannyDetection(img:np.ndarray):
    img=BilateralBluring(img)
    cannyD=cv.Canny(img,50,100) ## can set different Threshold values as well.
    ipr.subplot(img,cannyD,title1="Original image",title2="Canny Detection")
    
path=ipr.select_image()
img=cv.imread(f"{path}")

if img is None:
    raise FileNotFoundError
img=cv.cvtColor(img,cv.COLOR_BGR2RGB)

print("Enter the choice"
"\n1.Sobel detection--->1" 
"\n2.Laplace Detection--->2" 
"\n3.Canny Detection--->3"
"\n4.Exit--->4"
)

choice=None
while(choice!=5):
 choice=int(input("Enter the choice --->"))
  
 if choice==1:
  SobelDetection(img)
 elif choice==2:
  LaplaceDetection(img)
 elif choice==3:
  CannyDetection(img) 
 elif choice==4:
   print("\n\n\t\tBye....\n\n\t\t")
   exit() 
 else:
    print("\n\n\t\tEnter valid choice\t\t\n\n")