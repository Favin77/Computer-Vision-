#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Intensity transformation
import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt  
def start():
            import cv2
            import numpy as np
            import pandas as pd
            import matplotlib.pyplot as plt  
            print("Image Editing")
            print("-------------")
            char=input("Enter Input path address: ")
            img=cv2.imread(char,0)
            print(img.shape)
            cv2.imshow("InputImage",img)
            cv2.waitKey(0)
            while(True):
                print("\nFunction List\n------------\n1.Log Transformation\n2.Power Law\n3.Intensity Level Slicing Without Background\n4.Intensity Level Slicing With Background\n5.Thanks")
                a=int(input("\nEnter your preference number:"))
                if (a==1):
                    # log is expressed as s = clog(1+r)
                    # s is output intensity, m is max pixel value, shoud not exceed 255
                    # c scaling constant is given by 255/(log (1 + m))
                    c = 255/(np.log(1 + np.max(img))) 
                    log_transformed = c * np.log(1 + img) 
                    log_transformed = np.array(log_transformed, dtype = np.uint8)
                    cv2.imshow("log_transformed",log_transformed)
                    cv2.waitKey(0)
                elif(a==2):
                    gamma=float(input("Enter the value of gamma"))
                    gamma_corrected = np.array(255*(img / 255) ** gamma, dtype = 'uint8') #Gamma Calculation
                    cv2.imshow("Power Law",gamma_corrected)
                    cv2.waitKey(0)
                elif(a==3):
                    # Find width and height of image
                   
                    row, column = img.shape
                    # Create an zeros array to store the sliced image
                    img1 = np.zeros((row,column),dtype = 'uint8')

                    # Specify the min and max range
                    min_range = int(input("\nEnter your min_range:"))
                    max_range = int(input("\nEnter your max_range:"))

                    # Loop over the input image and if pixel value lies in desired range set it to 255 otherwise set it to 0.
                    for i in range(row):
                        for j in range(column):
                            if img[i,j]>min_range and img[i,j]<max_range:
                                img1[i,j] = 255
                            else:
                                img1[i,j] = 0
                    # Display the image
                    cv2.imshow("Input Image",img)
                    cv2.imshow('Graylevel slicing without background', img1)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
                elif(a==4):
                    # Find width and height of image
                    row, column = img.shape
                    # Create an zeros array to store the sliced image
                    img1 = np.zeros((row,column),dtype = 'uint8')

                    # Specify the min and max range
                    min_range = int(input("\nEnter your min_range:"))
                    max_range = int(input("\nEnter your max_range:"))

                    # Loop over the input image and if pixel value lies in desired range set it to 255 otherwise set it to 0.
                    for i in range(row):
                        for j in range(column):
                            if img[i,j]>min_range and img[i,j]<max_range:
                                img1[i,j] = 255
                            else:
                                img1[i,j] = img[i,j]
                    # Display the image
                    cv2.imshow("Input Image",img)
                    cv2.imshow('Graylevel slicing with background', img1)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
                elif(a==5):
                    print("Thanks")
                    break

