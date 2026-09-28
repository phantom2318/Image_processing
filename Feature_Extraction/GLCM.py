import cv2 as cv
import numpy as np
import ipress as ipr
from skimage import feature as sk


def CalculateGLCM(img:np.ndarray):
    img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    x=int(input("Enter The number of angle"))
    angle=np.zeros(x)
    dst=int(input("Enter the distance from thr origin pixel"))
    for i in range(x):
        angle[i]=int(input("Enter the value of angle"))
        angle[i]=np.radians(angle[i])
    glcm=sk.graycomatrix(img,[dst],angle)
    return glcm


path = ipr.select_image()
image=cv.imread(f"{path}")

if image is None:
    raise FileNotFoundError
#image=cv.cvtColor(image,cv.COLOR_BGR2GRAY)

GLCM=CalculateGLCM(image)

print("GLCM Properties of the image  are given below")

contrast=sk.graycoprops(GLCM,"contrast")
correlation=sk.graycoprops(GLCM,"correlation")
homogeneity=sk.graycoprops(GLCM,"homogeneity")
ASM=sk.graycoprops(GLCM,"ASM")
dissimilarity=sk.graycoprops(GLCM,"dissimilarity")
energy=sk.graycoprops(GLCM,"energy")

print(f"Contrast : {contrast}\n\n"
      f"correlation: {correlation}\n\n"
      f"homogeneity: {homogeneity}\n\n"
      f"ASM: {ASM}\n\n"
      f"dissimilarity: {dissimilarity}\n\n"
      f"energy: {energy}\n\n")