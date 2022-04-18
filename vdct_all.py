import cv2
import numpy as np
import matplotlib.pyplot as plt
import time
import os

sobels_path = "sobels/" # path to save results
count=0 # count
vdct_path = "vdct/"
frames = 5

def DCT(imgs5,h,w,f):

  # where imgs is the array to be processed, h and w are the shapes, 
  # and f is for the number of used frames.
  imgs_dct=imgs_r = imgs5.astype(np.float32)
  for i in range(height):
    for j in range(width):
      imgs_dct[i,j,:] = (cv2.dct(np.array(imgs5[i,j,:], np.float32))).reshape(f)
      imgs_dct[i,j,0] = 0;#imgs_dct[i,j,1] = 0
      imgs_r[i,j,:] = np.array(cv2.idct(imgs_dct[i,j,:].reshape(f,1)), np.uint8).reshape(f)
  return imgs_r[:,:,f//2]
  


list = sorted(os.listdir(sobels_path))
img0 = cv2.imread(sobels_path+"/"+list[0], cv2.IMREAD_GRAYSCALE) # get one image to get the shape
height, width = img0.shape

imgs = np.zeros((height, width,len(list)))
for m in list: 
  imgs[:,:,count] = cv2.imread(sobels_path+"/"+m, cv2.IMREAD_GRAYSCALE)
  count+=1
print("There are ",count," images.")

imgs_exp = np.zeros((height, width,len(list)+4))
print(imgs_exp.shape)
imgs_exp[:,:,2:-2] = imgs
imgs_exp[:,:,0] = imgs_exp[:,:,1] = imgs[:,:,0]
imgs_exp[:,:,-2] = imgs_exp[:,:,-1] = imgs[:,:,-1]
imgs_back = imgs
time1 = time.time()
for index in range(count):
  print("Processing frame: ", index)
  imgs_back[:,:,index] = DCT(imgs_exp[:,:,index:index+frames],height,width,frames)
time2 = time.time()
print("Process time: ", time2-time1, "s.") 

index = 0
for index in range(count):
  cv2.imwrite(vdct_path+"/"+list[index],imgs_back[:,:,index])

print("Finish! The results is in ", vdct_path)
