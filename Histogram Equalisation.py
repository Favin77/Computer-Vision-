#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
def start():
            print("Lab 6")
            print("-------------")
            char=input("Enter Input path address: ")
            img=cv2.imread(char,0)
            cv2.imshow("InputImage",img)
            cv2.waitKey(0)
            while(True):
                print("\nFunction List\n------------\n1.Image Histogram\n2.Linear Stretching\n3.Histogram Equalisation\n4.Quit")
                a=int(input("\nEnter your preference number:"))
                if (a==1):
                    img = cv2.imread(char,0)
                    print("Original Image Histogram")
                    hist,bins = np.histogram(img.flatten(),256,[0,256])
                    plt.hist(img.flatten(),256,[0,256], color = 'r')
                    plt.xlim([0,256])
                    plt.legend(('histogram'), loc = 'upper left')
                    plt.show()
                    continue
                elif(a==2):
                    #expands the range of intensity levels, 
                    #decreasing the intensity of the dark pixels and increasing the intensity of the light pixels
                    def pixelVal(pix, r1, s1, r2, s2): 
                        if (0 <= pix and pix <= r1): 
                            return (s1 / r1)*pix 
                        elif (r1 < pix and pix <= r2): 
                            return ((s2 - s1)/(r2 - r1)) * (pix - r1) + s1 
                        else: 
                            return ((255 - s2)/(255 - r2)) * (pix - r2) + s2 
                    r1 =int(input("Enter Min grey value of input img:"))#70
                    s1 =int(input("Enter Min grey value of output img:"))#0
                    r2 =int(input("Enter Max grey value of input img:"))#140
                    s2 =int(input("Enter Max grey value of output img:"))#255 
                    pixelVal_vec = np.vectorize(pixelVal)  
                    contrast_stretched = pixelVal_vec(img, r1, s1, r2, s2) 
                    cv2.imshow("contrast_stretched",contrast_stretched)
                    cv2.waitKey(0)
                    continue
                elif(a==3):
                    print("Image after Histogram Equalisation")
                    dst = cv2.equalizeHist(img)#equalize histogram
                    hist,bins = np.histogram(dst.flatten(),256,[0,256])#no of bins 
                    plt.hist(dst.flatten(),256,[0,256], color = 'r')
                    plt.xlim([0,256])
                    plt.legend(('histogram'), loc = 'upper left')
                    plt.show()
                    cv2.imshow('image', dst)
                    cv2.waitKey(0)
                    continue
                elif(a==4):
                    print("Thank You")
                    break

