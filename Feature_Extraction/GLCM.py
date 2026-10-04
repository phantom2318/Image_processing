import cv2 as cv
import numpy as np
import ipress as ipr
from skimage import feature as sk


def CalculateGLCM(img:np.ndarray):
    img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    x=int(input("Enter The number of angle::"))
    angle=np.zeros(x)
    dst=int(input("Enter the distance from thr origin pixel::"))
    for i in range(x):
        angle[i]=int(input("Enter the value of angle::"))
        angle[i]=np.radians(angle[i])
    glcm=sk.graycomatrix(img,[dst],angle)
    return glcm

def CompareGLCM(img1:np.ndarray,img2:np.ndarray):

    GLCM_1=CalculateGLCM(img1)
    print("\n\n\n------------------\n\n\n")
    GLCM_2=CalculateGLCM(img2)

    ipr.subplot(cv.cvtColor(img1,cv.COLOR_BGR2GRAY),cv.cvtColor(img2,cv.COLOR_BGR2GRAY),cmap1='gray',cmap2='gray')
    contrast_1,contrast_2=sk.graycoprops(GLCM_1,"contrast"),sk.graycoprops(GLCM_2,"contrast")
    correlation_1,correlation_2=sk.graycoprops(GLCM_1,"correlation"),sk.graycoprops(GLCM_2,"correlation")
    homogeneity_1,homogeneity_2=sk.graycoprops(GLCM_1,"homogeneity"),sk.graycoprops(GLCM_2,"homogeneity")
    energy_1,energy_2=sk.graycoprops(GLCM_1,"energy"),sk.graycoprops(GLCM_2,"energy")
    print(f"Contrast 1: {contrast_1} Contrast 2: {contrast_2} \n\n"
      f"correlation 1: {correlation_1} correlation 2: {correlation_2}\n\n"
      f"homogeneity 1: {homogeneity_1} homogeneity 2 {homogeneity_2}\n\n"
      f"energy 1: {energy_1} energy 2: {energy_2}\n\n")

path1 = ipr.select_image()
path2 = ipr.select_image()
image1=cv.imread(f"{path1}")
image2=cv.imread(f"{path2}")

if image1  is None:
    raise FileNotFoundError
#image=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
if image2  is None:
    raise FileNotFoundError
CompareGLCM(image1,image2)