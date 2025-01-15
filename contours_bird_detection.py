import cv2
import numpy as np
import os

def detect_birds(image_path):   #function to detect objects
    img = cv2.imread(image_path)

    width, height = int(img.shape[1]*0.9), int(img.shape[0]*0.9)
    if height > 680:    #decreasing the size of the image if it is too big so it fits my screen easily
        img = cv2.resize(img, (width, height))

    #converting to gray scale and using adaptive thresholding on the image
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #setting blocksize dynamically to make sure it is quite large and then applying adaptive threshold
    block_size = int(width/4)
    block_size += block_size%2==0
    thresh =  cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, block_size, 20)
  
    #making objects more pronounced with dilate
    thresh = cv2.dilate(thresh, np.ones((2, 2), dtype=np.int8))

    #finding contours and plotting them on the original image
    contours, heirarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = width*height
        if cv2.contourArea(cnt) > int(area*0.00027):    #making sure only relatively larger objects are detected
            x, y, w, h = cv2.boundingRect(cnt)
            img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 1)
    
    return img  #returning the image

# Set the directory path that contains the bird images
directory_path = '.venv/Contours/Data'

#reading images from the directory, detecting the birds and then displaying the result one image at a time
for file_name in os.listdir(directory_path):
        image_path = directory_path + '/' + file_name
        img = detect_birds(image_path)
        cv2.imshow('Flying Birds', img)
        cv2.waitKey(0)

cv2.destroyAllWindows()