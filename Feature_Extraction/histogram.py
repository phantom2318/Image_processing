import ipress as ipr
from matplotlib import pyplot as plot
import numpy as np
import cv2 as cv

def GrayHistogram(img:np.ndarray,title:str="Histogram of GRAY scale image"):
    graph=cv.calcHist([img],[0],None,[256],[0,255])
    
    plot.figure()
    plot.title(f"{title}")
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
    GrayHistogram(equalised_img,"Equalised Gray scale image Histogram")
    ipr.subplot(img,equalised_img,title1="Original image",title2="Equalised image",cmap1="gray",cmap2="gray")
   
def RGB_HistogramEqualiser(img:np.ndarray):
    b,g,r = cv.split(img)
    h_b, bin_b = np.histogram(b.flatten(), 256, (0, 256))
    h_g, bin_g = np.histogram(g.flatten(), 256, (0, 256))
    h_r, bin_r = np.histogram(r.flatten(), 256, (0, 256))
# calculate cdf    
    cdf_b = np.cumsum(h_b)  
    cdf_g = np.cumsum(h_g)
    cdf_r = np.cumsum(h_r)
    
# mask all pixels with value=0 and replace it with mean of the pixel values 
    cdf_m_b = np.ma.masked_equal(cdf_b,0)
    cdf_m_b = (cdf_m_b - cdf_m_b.min())*255/(cdf_m_b.max()-cdf_m_b.min())
    cdf_final_b = np.ma.filled(cdf_m_b,0).astype('uint8')
  
    cdf_m_g = np.ma.masked_equal(cdf_g,0)
    cdf_m_g = (cdf_m_g - cdf_m_g.min())*255/(cdf_m_g.max()-cdf_m_g.min())
    cdf_final_g = np.ma.filled(cdf_m_g,0).astype('uint8')
    cdf_m_r = np.ma.masked_equal(cdf_r,0)
    cdf_m_r = (cdf_m_r - cdf_m_r.min())*255/(cdf_m_r.max()-cdf_m_r.min())
    cdf_final_r = np.ma.filled(cdf_m_r,0).astype('uint8')
# merge the images in the three channels
    img_b = cdf_final_b[np.asarray(b, dtype=np.intp)]
    img_g = cdf_final_g[np.asarray(g, dtype=np.intp)]
    img_r = cdf_final_r[np.asarray(r, dtype=np.intp)]
  
    img_out = cv.merge((img_b, img_g, img_r))
# validation
    equ_b = cv.equalizeHist(b)
    equ_g = cv.equalizeHist(g)
    equ_r = cv.equalizeHist(r)
    equ = cv.merge((equ_b, equ_g, equ_r))
    ipr.subplot(img,img_out,title1="Original image",title2="Equalised image")

path=ipr.select_image()
img=cv.imread(f"{path}")

if img is None:
    raise FileNotFoundError

print("Enter the choice"
"\n\tGray Histogram--->1\t" 
"\n\tGray Histogram Equaliser--->2\t"
"\n\tRGB Histogram--->3\t" 
"\n\tRGB Histogram Equaliser--->4\t"
"\n\tExit--->5\t"
)

choice=None
while(choice!=5):
 choice=int(input("Enter the choice --->"))
  
 if choice==1:
  GrayHistogram(img)
 elif choice==2:
  GRAY_HistogramEqualiser(img)
 elif choice==3:
  RGBHistogram(img)
 elif choice==2:
  RGB_HistogramEqualiser(img)
 elif choice==5:
   print("Bye....")
   exit() 
 else:
   print("Enter valid choice.")