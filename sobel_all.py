import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

images_path = "images2" # original datasets
sobels_path = "sobels2/" # path to save results
i=0 # count

list = os.listdir(images_path)
for m in list:
  i+=1
  print(m)# print the name of current image
  img = cv2.imread(images_path+"/"+m)
  #print(img)
  gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  x = cv2.Sobel(gray_img, cv2.CV_16S, 1, 0)
  y = cv2.Sobel(gray_img, cv2.CV_16S, 0, 1)
  Scale_absX = cv2.convertScaleAbs(x) 
  Scale_absY = cv2.convertScaleAbs(y)
  result = cv2.addWeighted(Scale_absX, 0.5, Scale_absY, 0.5, 0)
  cv2.imwrite(sobels_path+'/'+m[:-4]+'_sobel.png',result)
  
print("There are ",i,"images prosessed and the results are saved in", sobels_path)



