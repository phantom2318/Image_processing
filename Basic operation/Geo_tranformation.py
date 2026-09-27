import numpy as np
import cv2 as cv
import ipress as ip
def Scalling():

      f_image1=ip.select_image()
      image1=cv.imread(f"{f_image1}")
      if image1 is None:
            raise FileNotFoundError
      
      x=float(input("enter the value of Horizontal Scaling::"))
      y=float(input("enter the value of Vertical Scaling::"))
      image2=cv.resize(image1,None,fx=x,fy=y,interpolation=cv.INTER_CUBIC)

      #plotting of the image
      ip.subplot(image1,image2)
      save=str(input("Do you want to save the image? (yes/no)"))
      if save.lower() =="yes":
            ip.save_image(image2,"Scaled image.jpg")
      else:
            pass

def Translation():
   PathOfImage1:str=ip.select_image()
   image1=cv.imread(f"{PathOfImage1}")
   if image1 is None:
         raise FileNotFoundError
   rows,cols,c=image1.shape
   x=int(input("enter the value of Horizontal Translation::"))
   y=int(input("enter the value of Vertical Translation::"))
   if type(x) is not int or type(y) is not int:
      raise TypeError
   M=np.float32([[1,0,x],[0,1,y]])
   T_image1=cv.warpAffine(image1,M,(cols,rows))
   image1=cv.cvtColor(image1,cv.COLOR_BGR2RGB)
   T_image1=cv.cvtColor(T_image1,cv.COLOR_BGR2RGB)
   ip.subplot(image1,T_image1)

def AffineTransformation():                     
   PathOfImage1:str=ip.select_image()
   image1=cv.imread(f"{PathOfImage1}")
   if image1 is None:
         raise FileNotFoundError 
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
   ip.subplot(image1,dst)

"""There are multiple chnages i want to make in the perspective tranformation code.
   currently all the selected points for the tranformation matrix of pts1 are pre-defined.
   unless user knows the matrix of image perfectly[which is 99.99% impossible],output will not be fruitful.
   therefore i want to change it in a way that user is able to decide the four points by clicking on the image for the first time.
   there are many functionality to add for that, and as part of that i wam not going to expand the code here.
"""
def PerspectiveTranformation():
   PathOfImage1:str=ip.select_image()
   image1=cv.imread(f"{PathOfImage1}")
   if image1 is None:
         raise FileNotFoundError 
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
   ip.subplot(image1,dst)
"""
     Now the various geometric tranformation of image.
"""
print("Enter the choice"
"\n\tPlot two images only side by side--->1\t" 
"\n\tScale the image--->2\t" 
"\n\tTranslate the image vertical and horizontal--->3\t" 
"\n\tAffineTransformation--->4\t"
"\n\tChange the Perspective of the image--->5\t"
"\n\tExit--->6\t")

choice=None
while(choice!=6):
 choice=int(input("Enter the choice --->"))

 if choice==1:
  ip.subplot()

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