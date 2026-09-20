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

path=ipr.select_image()
img=cv.imread(f"{path}")

if img is None:
    raise FileNotFoundError("Image not found")
MeanFiltering(img)
GaussianFiltering(img)
