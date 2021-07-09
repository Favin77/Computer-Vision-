#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2 
import numpy
import pandas


# In[ ]:


def start():
    print("Image Read & Write")
    print("-------------")
    while(True):
        print("\nFunction List\n------------\n1.Read an Image\n2.Write an Image\n3.Read a Video\n4.Record a Video and save video & frame\n5.Quit")
        a=int(input("\nEnter your preference number:"))
        if (a==1):
            char=input("Enter Image Input path address:")#Input path of image
            img=cv2.imread(char)#reads the image
            cv2.imshow("Image",img)#displays the image on a window
            cv2.waitKey(0)
            
        elif(a==2):
            char=input("Enter Image Input path address:")
            img=cv2.imread(char)
            filename = 'savedImage.jpg'
            cv2.imwrite(filename, img) #writes the image and saves it in the local drive
            cv2.imshow('Saved Image', img)
            cv2.waitKey(0)
            
        elif(a==3):
            
            video=input("Enter Video Input path address:")
            print("Press Q to Exit the Video")
            cap = cv2.VideoCapture(video)
            if (cap.isOpened()== False):  
                print("Error opening video  file") 

            # Read until video is completed 
            while(cap.isOpened()): 

              # Capture frame-by-frame 
                ret, frame = cap.read() 
                if ret == True: 

                # Display the resulting frame 
                    cv2.imshow('Frame', frame) 

                # Press Q on keyboard to  exit 
                    if cv2.waitKey(25) & 0xFF == ord('q'): 
                        break

              # Break the loop 
                else:  
                    break

            # When everything done, release  
            # the video capture object 
            cap.release() 

            # Closes all the frames 
            cv2.destroyAllWindows()
              
        elif(a==4):
                print("Press S to save a frame of the video and to write the video as well")
                # Create an object to read  
                # from camera 
                video = cv2.VideoCapture(0) 

                # We need to check if camera 
                # is opened previously or not 
                if (video.isOpened() == False):  
                    print("Error reading video file") 

                # We need to set resolutions. 
                # so, convert them from float to integer. 
                frame_width = int(video.get(3)) 
                frame_height = int(video.get(4)) 

                size = (frame_width, frame_height) 

                # Below VideoWriter object will create 
                # a frame of above defined The output  
                # is stored in 'SavedVideo.avi' file. 
                result = cv2.VideoWriter('SavedVideo.avi',  
                                         cv2.VideoWriter_fourcc(*'MJPG'), 
                                         10, size) 

                while(True): 
                    ret, frame = video.read() 

                    if ret == True:  

                        # Write the frame into the 
                        # file 'filename.avi' 
                        result.write(frame) 

                        # Display the frame 
                        # saved in the file 
                        cv2.imshow('Frame', frame) 

                        # Press S on keyboard  
                        # to stop the process 
                        if cv2.waitKey(1) & 0xFF == ord('s'): 
                            break

                    # Break the loop 
                    else: 
                        break
                filename = 'SavedFrame.jpg'
                cv2.imwrite(filename,frame)

                # When everything done, release  
                # the video capture and video  
                # write objects 
                video.release() 
                result.release() 

                # Closes all the frames 
                cv2.destroyAllWindows() 

                print("The video & image was successfully saved")
        elif(a==5):
            print("Thank You")
            break
            
            

