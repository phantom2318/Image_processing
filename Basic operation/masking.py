import ipress as ipr
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def CreateMask(img:np.ndarray)-> np.ndarray:
    s1, s2 = map(int, input("Enter the Starting points (x y): ").split())
    e1, e2 = map(int, input("Enter the Ending points (x y): ").split())
    rectangle = cv.rectangle(np.zeros(img.shape[0:2],dtype="uint8"), (s1, s2), (e1, e2), (255, 255, 255), thickness=-1) 
    return rectangle

def AndMasking(img:np.ndarray):
    img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.show()

    s1, s2 = map(int, input("Enter the Starting points (x y): ").split())
    e1, e2 = map(int, input("Enter the Ending points (x y): ").split())
    rectangle = cv.rectangle(np.zeros(img.shape[0:2],dtype="uint8"), (s1, s2), (e1, e2), (255, 255, 255), thickness=-1)
    masked=cv.bitwise_and(img,img,mask=rectangle)
    img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
    masked=cv.cvtColor(masked,cv.COLOR_BGR2RGB)
    ipr.subplot(img,masked)

def GrayHistogram(img:np.ndarray,mask:np.ndarray):
    graph=cv.calcHist([img],[0],mask,[256],[0,255])
    plt.figure()
    plt.title("Color histogram of GRAY SCALE IMAGE")
    plt.xlabel("Pixel values")
    plt.ylabel("Number of pixels")
    plt.plot(graph)
    plt.show()

def RGBHistogram(img:np.ndarray,mask:np.ndarray):

    colors=("Blue","Green","Red")
    for i,color in enumerate(colors):
        hist=cv.calcHist([img],[i],mask,[32],[0,256])
        plt.plot(hist,color=color)
    plt.title("RGB color histogram")
    plt.xlabel("Bins")
    plt.ylabel("number of pixels")
    plt.show()

path1=ipr.select_image()
img1=cv.imread(f"{path1}")
if img1 is None:
    raise ValueError(f"Unable to read image: {path1}")
AndMasking(img1)
mask=CreateMask(img1)
GrayHistogram(img1,mask=mask)
RGBHistogram(img1,mask=mask)