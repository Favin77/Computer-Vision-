#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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
                print("\nFunction List\n------------\n1.And\n2.OR\n3.XOR\n4.NOT\n5.Quit")
                a=int(input("\nEnter your preference number:"))
                if(a==1):
                    dest_and = cv2.bitwise_and(img2, img1, mask = None)#And operation
                    cv2.imshow("AND Operation",dest_and)
                    cv2.waitKey(0)
                elif(a==2):
                    dest_or = cv2.bitwise_or(img2, img1, mask = None)#OR operation
                    cv2.imshow("OR Operation",dest_or)
                    cv2.waitKey(0)
                elif(a==3):
                    dest_xor = cv2.bitwise_xor(img1, img2, mask = None)#XOR operation
                    cv2.imshow("XOR Operation",dest_xor)
                    cv2.waitKey(0)
                elif(a==4):
                    dest_not1 = cv2.bitwise_not(img1, mask = None)#Not operation for image 1
                    dest_not2 = cv2.bitwise_not(img2, mask = None)#Not operation for image 2 
                    cv2.imshow("NOT Operation img1",dest_not1)
                    cv2.waitKey(0)
                    cv2.imshow("NOT Operation img2",dest_not2)
                    cv2.waitKey(0)
                elif(a==5):
                    print("Thanks")
                    break
    

