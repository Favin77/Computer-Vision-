#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
from skimage.util import random_noise
def start():
            print("Lab 7")
            print("-------------")
            char=input("Enter Input path address: ")
            img=cv2.imread(char,0)
            print(img.shape)
            cv2.imshow("InputImage",img)
            cv2.waitKey(0)

            while(True):
                print("\nFunction List\n------------\n1.OriginalWithNoise\n2.Average\n3.Median\n4.High pass\n5.High boost\n6.Quit")
                a=int(input("\nEnter your preference number:"))
                if (a==1):
                    gauss = np.random.normal(0,1,img.size)#adding random noise
                    gauss = gauss.reshape(img.shape[0],img.shape[1]).astype('uint8')
                    img_gauss = cv2.add(img,gauss)
                    cv2.imshow("Noise",img_gauss)
                    cv2.waitKey(0)
                    continue
                elif(a==2):
                    blur = cv2.blur(img_gauss,(5,5))#average filter
                    cv2.imshow("Average",blur)
                    cv2.waitKey(0)
                    continue
                elif(a==3):
                    noise_img = random_noise(img, mode='s&p',amount=0.3)#adding salt&pepper noise
                    noise_img = np.array(255*noise_img, dtype = 'uint8')
                    median = cv2.medianBlur(noise_img,5)#Median filter
                    cv2.imshow("Median",median)
                    cv2.waitKey(0)
                elif(a==4):
                    noise_img = random_noise(img, mode='s&p',amount=0.3)#adding salt&pepper noise
                    noise_img = np.array(255*noise_img, dtype = 'uint8')
                    kernel = np.array([[-1 , -1 , -1] , [-1 , 8 , -1] ,[-1 , -1 , -1]])
                    sharp_img = cv2.filter2D(noise_img , -1 , kernel = kernel)#HIgh pass filter using Sharpen filter 
                    cv2.imshow("High Pass",sharp_img)
                    cv2.waitKey(0)
                elif(a==5):
                    high_boost=3*noise_img+sharp_img#high boost filter
                    cv2.imshow("High Pass",high_boost)
                    cv2.waitKey(0)
                elif(a==6):
                    print("Thank you")
                    break           
    


# In[ ]:




