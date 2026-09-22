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
    #detectedImage=cv.cvtColor(detectedImage,cv.COLOR_BGR2RGB)
    img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
    ipr.subplot(img,detectedImage,cmap1='gray',cmap2='gray')

def LaplaceDetection(img:np.ndarray):
    img=BilateralBluring(img)
    laplace=cv.Laplacian(img,cv.CV_64F)
    laplace=np.uint8(np.absolute(laplace))

    ipr.subplot(img,laplace,cmap1='gray',cmap2='gray')
def CannyDetection(img:np.ndarray):
    img=BilateralBluring(img)
    cannyD=cv.Canny(img,50,100) ## can set different Threshold values as well.
    ipr.subplot(img,cannyD,cmap1='gray',cmap2='gray')
    
path=ipr.select_image()
img=cv.imread(f"{path}")

if img is None:
    raise FileNotFoundError
img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
SobelDetection(img)
LaplaceDetection(img)
CannyDetection(img)