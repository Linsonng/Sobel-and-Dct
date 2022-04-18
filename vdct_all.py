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




# #print(v)
# time1 = time.time()
# v_dct = cv2.dct(np.array(v, np.float32))
# time2 = time.time()
# print(time2-time1)
# #print(v_dct)

# v_back = np.array(cv2.idct(v_dct), np.uint8)
# print("vback is ")
# print(v_back)

# # print(img4[75,75])
# #imgs_dct = v_dct.expand(5,75,75).transpose(1,2,0)
# imgs_dct = imgs.astype(np.float32)
# imgs_r = imgs.astype(np.float32)

# print(imgs_dct.shape)
# time1 = time.time()
# for r in range(10):

# time2 = time.time()
# print((time2-time1)/10)
# print(imgs_r[75,75,:])

# print("let's check")
# print(imgs_dct.shape)
# print(imgs_dct[75,75,:])
# print(imgs_dct[80,80,:])
# x = imgs_dct[75,75,:]
# x = x.reshape(5,1)

# #x[0] = 8.497058
# print(x)
# print(v_dct)

# y = cv2.idct(v_dct)
# y = cv2.idct(x)
# z = np.array(y, np.uint8)
# print(z)
#v_75_r= np.array(cv2.idct(imgs_dct[75,75,:].reshape(5,1)), np.uint8).reshape(5)
#cv2.imwrite("vdct_tractor_0001.png",imgs_r[:,:,0])
#cv2.imwrite("vdct_tractor_0002.png",imgs_r[:,:,1])
#cv2.imwrite("vdct_tractor_0003.png",imgs_r[:,:,2])
#cv2.imwrite("vdct_tractor_0004.png",imgs_r[:,:,3])
#cv2.imwrite("vdct_tractor_0005.png",imgs_r[:,:,4])


# img_r1 = np.array(cv2.idct(img_dct1), np.uint8)
# img_r2 = np.array(cv2.idct(img_dct2), np.uint8)

# fig = plt.figure('DCT demo', figsize=(4,2))
# plt.subplot(331)
# plt.imshow(img1, 'gray'), plt.title('Original_1'), plt.axis('off')
# plt.subplot(332)
# plt.imshow(np.array(img_dct1, np.uint8), cmap='hot'), plt.title('DCT mod of Original_1'), plt.axis('off')


# plt.subplot(333)
# plt.imshow(img2, 'gray'), plt.title('Original_2'), plt.axis('off')
# plt.subplot(334)
# plt.imshow(np.array(img_dct2, np.uint8), cmap='hot'), plt.title('DCT mod of Original_2'), plt.axis('off')


# # img_d = abs(img1-img2)
# # img_dct_d = abs(img_dct2-img_dct1)
# # img_dct_d2o = np.array(cv2.idct(img_dct_d), np.uint8)

# plt.subplot(335)
# plt.imshow(imgs_r[:,:,0], 'gray'), plt.title('IDCT results of original_1'), plt.axis('off')
# plt.subplot(336)
# plt.imshow(imgs_r[:,:,1], 'gray'), plt.title('IDCT results of original_2'), plt.axis('off')
# plt.subplot(337)
# plt.imshow(imgs_r[:,:,2], 'gray'), plt.title('IDCT results of original_3'), plt.axis('off')
# plt.subplot(338)
# plt.imshow(imgs_r[:,:,3], 'gray'), plt.title('IDCT results of original_4'), plt.axis('off')
# plt.subplot(339)
# plt.imshow(imgs_r[:,:,4], 'gray'), plt.title('IDCT results of original_5'), plt.axis('off')



# plt.tight_layout()
# plt.show()


