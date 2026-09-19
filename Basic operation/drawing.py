import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from PIL import Image
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

## converting the image from BGR to RGB
def show(img)->np.ndarray:
    img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
    return img
## plotting an image
def Subplot(image1=None,image2=None,cmap1=None,cmap2=None,title1="Image-1",title2="Image-2"):

   if image1 is None:
    f_image1=SelectImage()
    image1=cv.imread(f"{f_image1}")

    if image1 is None:
       raise FileNotFoundError(f"Could not read image: {f_image1}")
   if image2 is None:
     f_image2=SelectImage()
     image2=cv.imread(f"{f_image2}")

     if image2 is None:
       raise FileNotFoundError(f"Could not read image: {f_image2}")

   plt.subplot(1,2,1)
   plt.imshow(image1,cmap=cmap1)
   plt.title(title1)

   plt.subplot(1,2,2)
   plt.imshow(image2,cmap=cmap2)
   plt.title(title2)

   plt.show()

###Drawing a line.
def Line(image:np.ndarray)->np.ndarray:
  thickness=int(input(("Enter the thickness of the line")))
  start=(0,0)
  end=(image.shape[1],image.shape[0])
  image=cv.line(image,start,end,[255,0,0],thickness)
  return image

###Drawing Rectangle
def Rectangle(image: np.ndarray)->np.ndarray:
    thickness=int(input(("Enter the thickness of the line")))
    start=(0,0)
    end=(50,100)
    image=cv.rectangle(image,start,end,[255,0,0],thickness)
    return image
    
path=SelectImage()
image=cv.imread(path)
if image is None:
  raise FileNotFoundError(f"Could not read image: {path}")
Lined_image=image.copy()
Lined_image=show(Lined_image)
Lined_image=Line(Lined_image)
Subplot(image,Lined_image,title1="Normal image",title2="Line drawn")

rectangled_image=image.copy()
rectangled_image=cv.cvtColor(rectangled_image,cv.COLOR_BGR2RGB)
rectangled_image=Rectangle(Lined_image)
Subplot(image,rectangled_image,title1="Normal image",title2="Line drawn")
points = []

def onclick(event):
    if event.xdata is not None and event.ydata is not None:
        points.append((int(event.xdata), int(event.ydata)))

        if len(points) == 2:
            x1, y1 = points[0]
            x2, y2 = points[1]

            ax.plot([x1, x2], [y1, y2])
            fig.canvas.draw()

fig, ax = plt.subplots()

image=cv.cvtColor(image,cv.COLOR_BGR2RGB)
ax.imshow(image)
cid = fig.canvas.mpl_connect("button_press_event", onclick)
plt.show()