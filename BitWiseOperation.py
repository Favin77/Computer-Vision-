#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Arithmeticc Transformation
import cv2
import numpy as np
import pandas as pd
def start():
        print("Image Editing")
        print("-------------")
        char=input("Enter Input path address of Image 1: ")
        img1=cv2.imread(char,0)
        char1=input("Enter Input path address of Image 2: ")
        img2=cv2.imread(char1,0)
        print(img1.shape)
        cv2.imshow("InputImage1",img1)
        cv2.waitKey(0)
        print(img2.shape)
        cv2.imshow("InputImage2",img2)
        cv2.waitKey(0)
        while(True):
            print("\nFunction List\n------------\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Quit")
            a=int(input("\nEnter your preference number:"))
            if(a==1):
                dst = cv2.addWeighted(img1, 0.7, img2, 0.6, 0)#Addition of 2 images
                cv2.imshow("Addition",dst)
                cv2.waitKey(0)
            elif(a==2):
                result_image = cv2.subtract(img1, img2)#Subtraction of 2 images
                cv2.imshow("Subtraction",result_image)
                cv2.waitKey(0)
            elif(a==3):
                result_image = cv2.multiply(img1, img2)#Multiplication of 2 images
                cv2.imshow("Multiply",result_image)
                cv2.waitKey(0)
            elif(a==4):
                result_image = cv2.divide(img1, img2)#Division of 2 images
                cv2.imshow("Divide",result_image)
                cv2.waitKey(0)
            elif(a==5):
                print("Thanks")
                break

