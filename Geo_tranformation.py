import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from tkinter import Tk,filedialog

#Select an image from Device
def SelectImage()->str:
 root=Tk()
 root.withdraw()
 file_path = filedialog.askopenfilename(
    title="Select an image",
    filetypes=[
        ("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff"),
        ("All files", "*.*")
    ]
    )
 #if image is not selected by the user
 if not file_path:
    print("No image selected.")
    exit()
 return file_path

#plotting an image
def Subplot(image1=None,image2=None):

   if image1 is None:
    f_image1=SelectImage()
    image1=cv.imread(f"{f_image1}")
    image1=cv.cvtColor(image1,cv.COLOR_BGR2RGBA)
   if image2 is None:
     f_image2=SelectImage()
     image2=cv.imread(f"{f_image2}")
     image2=cv.cvtColor(image2,cv.COLOR_BGR2RGBA)

   plt.subplot(1,2,1)
   plt.imshow(image1)
   plt.title("Image 1")

   plt.subplot(1,2,2)
   plt.imshow(image2)
   plt.title("Image 2")

   plt.show()
def Scalling():

      f_image1=SelectImage()
      
      image1=cv.imread(f"{f_image1}")
      x=float(input("enter the value of Horizontal scaling::"))
      y=float(input("enter the value of vertical scaling::"))
      image2=cv.resize(image1,None,fx=x,fy=y,interpolation=cv.INTER_CUBIC)
      image2=cv.cvtColor(image2,cv.COLOR_BGR2RGBA)
      image1=cv.cvtColor(image1,cv.COLOR_BGR2RGBA)

      #plotting of the image
      Subplot(image1,image2)

def Translation():
   PathOfImage1:str=SelectImage()
   image1=cv.imread(f"{PathOfImage1}")

   rows,cols,c=image1.shape
   x=int(input("enter the value of Horizontal Translation::"))
   y=int(input("enter the value of vertical translation::"))
   
   M=np.float32([[1,0,x],[0,1,y]])
   T_image1=cv.warpAffine(image1,M,(cols,rows))
   image1=cv.cvtColor(image1,cv.COLOR_BGR2RGB)
   T_image1=cv.cvtColor(T_image1,cv.COLOR_BGR2RGB)
   Subplot(image1,T_image1)

def AffineTransformation():
   PathOfImage1:str=SelectImage()
   image1=cv.imread(f"{PathOfImage1}") 
   rows,cols,c=image1.shape
   pts1 = np.float32([[50,50],
                      [200,50],
                      [50,200]])
   pts2 = np.float32([[10,100],
                      [200,50],
                      [100,250]])

   M = cv.getAffineTransform(pts1,pts2)
   dst = cv.warpAffine(image1,M,(cols,rows))

   image1=cv.cvtColor(image1,cv.COLOR_BGR2RGB)
   dst=cv.cvtColor(dst,cv.COLOR_BGR2RGB)
   Subplot(image1,dst)

"""There are multiple chnages i want to make in the perspective tranformation code.
   currently all the selected points for the tranformation matrix of pts1 are pre-defined.
   unless user knows the matrix of image perfectly[which is 99.99% impossible],output will not be fruitful.
   therefore i want to change it in a way that user is able to decide the four points by clicking on the image for the first time.
   there are many functionality to add for that, and as part of that i wam not going to expand the code here.
"""
def PerspectiveTranformation():
   PathOfImage1:str=SelectImage()
   image1=cv.imread(f"{PathOfImage1}") 
   rows,cols,c=image1.shape

   pts1 = np.float32([[200,65],
                      [400,52],
                      [28,387],
                      [389,390]])
   pts2 = np.float32([[0,0],
                      [300,0],
                      [0,300],
                      [300,300]])
   M = cv.getPerspectiveTransform(pts1,pts2)
   dst = cv.warpPerspective(image1,M,(300,300))
   image1=cv.cvtColor(image1,cv.COLOR_BGR2RGB)
   dst=cv.cvtColor(dst,cv.COLOR_BGR2RGB)
   Subplot(image1,dst)
"""
     Now the various geometric tranformation of image.
"""
print("Enter the choice"
"\n1.Plot two images only side by side--->1" 
"\n2.Scale the image--->2" 
"\n3.Translate the image vertical and horizontal--->3" 
"\n4.AffineTransformation--->4"
"\n5.Change the Perspective of the image--->5"
"\n6.Exit--->6")

choice=None
while(choice!=6):
 choice=int(input("Enter the choice --->"))

 if choice==1:
  Subplot()
 elif choice==2:
  Scalling()
 elif choice==3:
  Translation()
 elif choice==4:
  AffineTransformation()
 elif choice==5:
  PerspectiveTranformation()
 elif choice==6:
  print("\n\tExiting................")
  exit()
 else:
  print("Invalid choice.\t Enter again.")