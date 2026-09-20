import ipress as ipr
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

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


path1=ipr.select_image()
img1=cv.imread(f"{path1}")
if img1 is None:
    raise ValueError(f"Unable to read image: {path1}")
AndMasking(img1)
