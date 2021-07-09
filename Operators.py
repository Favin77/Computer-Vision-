#!/usr/bin/env python
# coding: utf-8

# In[3]:


import cv2 
import numpy as np
def start():
    print("Image Editing")
    print("-------------")
    char=input("Enter Input path address: ")
    img=cv2.imread(char,0)
    print(img.shape)
    img2= cv2.GaussianBlur(img,(5,5),0)#gaussian Image
    cv2.imshow("InputImage",img)
    cv2.imshow("GaussianImage",img2)
    cv2.waitKey(0)
    while(True):
        print("\nFunction List\n------------\n1.Prewitts Operator\n2.Sobel Operator\n3.Roberts Operator\n4.Prewitts Compass Operator\n5.Sobel Compass Operator\n6.Quit")
        a=int(input("\nEnter your preference number:"))
        if(a==1):
            kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
            kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
            img_prewittx = cv2.filter2D(img2, -1, kernelx)#Horizontal 
            img_prewitty = cv2.filter2D(img2, -1, kernely)#Vertical
            img_prewitt = img_prewittx + img_prewitty#Horizontal & Vertical
            cv2.imshow("img_prewittx",img_prewittx)
            cv2.imshow("img_prewitty",img_prewitty)
            cv2.imshow("img_prewitt",img_prewitt)
            cv2.waitKey(0)
        elif(a==2):
            img_sobelx = cv2.Sobel(img2,cv2.CV_8U,0,1,ksize=3)
            img_sobely = cv2.Sobel(img2,cv2.CV_8U,1,0,ksize=3)
            img_sobel = img_sobelx + img_sobely
            cv2.imshow("Horizontal",img_sobelx)
            cv2.imshow("Vertical",img_sobely)
            cv2.imshow("All Edges",img_sobel)
            cv2.waitKey(0)
        elif(a==3):
            kernel_Roberts_x = np.array([[1, 0],[0, -1]])
            kernel_Roberts_y = np.array([[0, -1],[1, 0]])
            x = cv2.filter2D(img2, cv2.CV_16S, kernel_Roberts_x)
            y = cv2.filter2D(img2, cv2.CV_16S, kernel_Roberts_y)
            absX = cv2.convertScaleAbs(x)
            absY = cv2.convertScaleAbs(y)
            roberts = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)
            cv2.imshow("roberts",roberts)
            cv2.waitKey(0)
        elif(a==4):
            #Masks
            prewitt1 = np.array ([[-1,-1,-1],[1,-2,1],[1,1,1]])
            prewitt2 = np.array ([[-1,-1,1],[-1,-2,1],[1,1,1]])
            prewitt3 = np.array ([[-1,1,1],[-1,-2,1],[-1,1,1]])
            prewitt4 = np.array ([[1,1,1],[-1,-2,1],[-1,-1,1]])
            prewitt5 = np.array ([[1,1,1],[1,-2,1],[-1,-1,-1]])
            prewitt6 = np.array ([[1,1,1],[1,-2,-1],[1,-1,-1]])
            prewitt7 = np.array ([[1,1,-1],[1,-2,-1],[1,1,-1]])
            prewitt8 = np.array ([[1,-1,-1],[1,-2,-1],[1,1,1]])
            #Applying All Prewitt filter on the image
            img_prewitt1 = cv2.filter2D(img2, -1, prewitt1)
            img_prewitt2 = cv2.filter2D(img2, -1, prewitt2)
            img_prewitt3 = cv2.filter2D(img2, -1, prewitt3)
            img_prewitt4 = cv2.filter2D(img2, -1, prewitt4)
            img_prewitt5 = cv2.filter2D(img2, -1, prewitt5)
            img_prewitt6 = cv2.filter2D(img2, -1, prewitt6)
            img_prewitt7 = cv2.filter2D(img2, -1, prewitt7)
            img_prewitt8 = cv2.filter2D(img2, -1, prewitt8)

            #Adding all the elements together to form an image
            prewitt_compass = img_prewitt1 + img_prewitt2 + img_prewitt3 + img_prewitt4 + img_prewitt5 + img_prewitt6 + img_prewitt7 + img_prewitt8
            cv2.imshow("prewitt_compass",prewitt_compass)
            cv2.waitKey(0)
        
        elif(a==5):
            img_sobel1 = cv2.Sobel(img2,cv2.CV_8U,1,0,ksize=3)
            img_sobel2 = cv2.Sobel(img2,cv2.CV_8U,0,1,ksize=3)
            img_sobel3 = cv2.Sobel(img2,cv2.CV_8U,1,0,ksize=3)
            img_sobel4 = cv2.Sobel(img2,cv2.CV_8U,0,1,ksize=3)
            img_sobel5 = cv2.Sobel(img2,cv2.CV_8U,1,0,ksize=3)
            img_sobel6 = cv2.Sobel(img2,cv2.CV_8U,0,1,ksize=3)
            img_sobel7 = cv2.Sobel(img2,cv2.CV_8U,1,0,ksize=3)
            img_sobel8 = cv2.Sobel(img2,cv2.CV_8U,0,1,ksize=3)
            #Adding all the elements together to form an image
            sobel_compass = img_sobel1 + img_sobel2 + img_sobel3 + img_sobel4 + img_sobel5 + img_sobel6 + img_sobel7 + img_sobel8
            cv2.imshow("sobel_compass",sobel_compass)
            cv2.waitKey(0)
            
        elif(a==6):
            print("Thank you")
            break
            
            
            


# In[ ]:




