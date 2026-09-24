import ipress as ipr
from matplotlib import pyplot as plot
import numpy as np
import cv2 as cv

def GrayHistogram(img:np.ndarray):
    graph=cv.calcHist([img],[0],None,[256],[0,255])
    
    plot.figure()
    plot.title("Color histogram of GRAY SCALE IMAGE")
    plot.xlabel("Pixel values")
    plot.ylabel("Number of pixels")
    plot.plot(graph)
    plot.show()

def RGBHistogram(img:np.ndarray):

    colors=("Blue","Green","Red")
    for i,color in enumerate(colors):
        hist=cv.calcHist([img],[i],None,[32],[0,256])
        plot.plot(hist,color=color)
    plot.title("RGB color histogram")
    plot.xlabel("Bins")
    plot.ylabel("number of pixels")
    plot.show()

def GRAY_HistogramEqualiser(img:np.ndarray):
    img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    GrayHistogram(img)
    equalised_img=cv.equalizeHist(img)
    ipr.subplot(img,equalised_img,title1="Original image",title2="Equalised image",cmap1="gray",cmap2="gray")
    equaliseHist=cv.calcHist([equalised_img],[0],None,[256],[0,255])

    plot.figure()
    plot.xlabel("Pixel values")
    plot.ylabel("Number of pixels")
    plot.title("Equalised Histogram")
    plot.plot(equaliseHist)
    plot.show()

path=ipr.select_image()
img=cv.imread(f"{path}")

if img is None:
    raise FileNotFoundError
GrayHistogram(cv.cvtColor(img,cv.COLOR_BGR2GRAY))
RGBHistogram(img)
ipr.subplot(img,cv.cvtColor(img,cv.COLOR_BGR2GRAY),cmap2="gray")
GRAY_HistogramEqualiser(img)