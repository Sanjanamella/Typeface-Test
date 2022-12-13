import cv2
import numpy as np
img = cv2.imread("iiit-test-image2.png")
number_of_white_pix = np.sum(img == 255)
print('Number of white pixels:', number_of_white_pix+1)
    
         
