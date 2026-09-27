import ipress as ipr
import numpy as np
import cv2 as cv

path=ipr.select_image()
image=cv.imread(f"{path}")

if image is None:
    raise FileNotFoundError

print("Enter the choice"
"\n\tBGR format--->1"
"\n\tGRAY format--->2"
"\n\tYCrCb format--->3"
"\n\tYUV format--->4"
"\n\tHSV and HSV_FULL format--->5"
"\n\tHSL and HSL_FULL format--->6"
"\n\tLAB format format--->7"
"\n\tChoose the image again--->8"
"\n\tExit--->9"
)

flag=False
while(flag is False):

    choice=int(input("Enter the choice for image formate"))

    if choice == 1:
        ipr.subplot(image,cv.cvtColor(image,cv.COLOR_RGB2BGR),title1="RGB Format",title2="BGR Formate")
    
    elif choice == 2:
        ipr.subplot(image,cv.cvtColor(image,cv.COLOR_RGB2GRAY),title1="RGB Format",title2="GRAY Format",cmap2="gray")
    elif choice == 3:
        ipr.subplot(image,cv.cvtColor(image,cv.COLOR_RGB2YCrCb),title1="RGB Format",title2="YCrCb Format")
    elif choice == 4:
            ipr.subplot(image,cv.cvtColor(image,cv.COLOR_RGB2YUV),title1="RGB Format",title2="YUV Format")
    elif choice == 5:
            ipr.subplot(image,cv.cvtColor(image,cv.COLOR_RGB2HSV),title1="RGB Format",title2="HSV Format")
            ipr.subplot(image,cv.cvtColor(image,cv.COLOR_RGB2HSV_FULL),title1="RGB Format",title2="HSV_FULL Format")
    elif choice == 6:
            ipr.subplot(image,cv.cvtColor(image,cv.COLOR_RGB2HLS),title1="RGB Format",title2="HSL Format")
            ipr.subplot(image,cv.cvtColor(image,cv.COLOR_RGB2HLS_FULL),title1="RGB Format",title2="HSL_FULL Format")
    elif choice == 7:
            ipr.subplot(image,cv.cvtColor(image,cv.COLOR_RGB2LAB),title1="RGB Format",title2="LAB Format")
    elif choice == 8:
            path=ipr.select_image()
            image=cv.imread(f"{path}")

            if image is None:
                  raise FileNotFoundError
    elif choice == 9:
          print("\n\n\t\t BYEEEE \t\t\n\n")
          flag=True
    else:
          print("Enter valid choice.")
