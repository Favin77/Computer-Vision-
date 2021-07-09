#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2 
import numpy as np
import pandas as pd
def start():
    print("Image Editing")
    print("-------------")
    char=input("Enter Input path address: ")
    img=cv2.imread(char)
    print(img.shape)
    cv2.imshow("InputImage",img)
    cv2.waitKey(0)

    while(True):
        print("\nFunction List\n------------\n1.Translation\n2.Cropping\n3.Flipping\n4.Scaling\n5.Rotation\n6.Shearing\n7.Quit")
        a=int(input("\nEnter your preference number:"))
        if(a==1):

            print("Translation\n------------")
            x=int(input("\nEnter the coordinates for x: "))
            y=int(input("\nEnter the coordinates for y: "))
            M=np.float32([[1,0,x],[0,1,y]])
            shifted=cv2.warpAffine(img,M,(img.shape[1],img.shape[0]))
            cv2.imshow("Shifted",shifted)
            cv2.waitKey(0)
        
        elif(a==2):
            print("Cropping\n------------")
            img=cv2.imread(char)
            x1=int(input("Enter x1 to be cropped: "))
            x2=int(input("Enter x2 to be cropped: "))
            y1=int(input("Enter y1 to be cropped: "))
            y2=int(input("Enter y2 to be cropped: "))
            crop=img[x1:x2,y1:y2]
            cv2.imshow("Cropping",crop)
            cv2.waitKey(0)
      
        elif(a==3):
            print("Flipping\n--------------")
            print("\n1.Horizontal\n2.Vertical\n3.HV")
            w=int(input("Enter your preference number: "))
            if (w==1):
                flipH=cv2.flip(img,1)
                cv2.imshow("Flipping",flipH)
            if (w==2):
                flipV=cv2.flip(img,0)
                cv2.imshow("Flipping",flipV)
            if (w==3):
                flipHV=cv2.flip(img,-1)
                cv2.imshow("Flipping",flipHV)
            cv2.waitKey(0)
     
        elif(a==4):
            print("Scaling\n-------------")
            s=float(input("Enter your scaling parameter:"))

            Width = int(img.shape[1] * s/100 )
            Height = int(img.shape[0] * s/100)
            dim = (Width, Height)
            scale=cv2.resize(img,dim,interpolation=cv2.INTER_AREA)

            cv2.imshow("Scaling",scale)
            cv2.waitKey(0)
    
        elif(a==5):
            print("Rotation\n---------------")
            angle=int(input("Enter your angle :"))
            reduction=0.5
            img=cv2.imread(char)

            (h,w)=img.shape[:2]
            center=(w/2,h/2)

            M=cv2.getRotationMatrix2D(center,angle,reduction)
            rotate=cv2.warpAffine(img,M,(w,h))
            cv2.imshow("Rotation",rotate)
            cv2.waitKey(0)
       
        elif(a==6):
            print("Sheared\n---------------")
            rows, cols, dim = img.shape
            print("\n1.X-axis\n2.Y-axis")
            v=int(input("\nEnter your preference number: "))
            if(v==1):
                M = np.float32([[1, 0.5, 0],
                    [0, 1  , 0],
                    [0, 0  , 1]])
                sheared_img = cv2.warpPerspective(img,M,(int(cols*1.5),int(rows*1.5))) 
                cv2.imshow("Sheared",sheared_img)
                cv2.waitKey(0)
            if(v==2):
                M = np.float32([[1,   0, 0],
                              [0.5, 1, 0],
                              [0,   0, 1]])
                sheared_img = cv2.warpPerspective(img,M,(int(cols*1.5),int(rows*1.5))) 
                cv2.imshow("Sheared",sheared_img)
                cv2.waitKey(0)
            
        elif(a==7):
            print("Thank you")
            break

