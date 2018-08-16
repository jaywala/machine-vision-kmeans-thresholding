import sys
import cv2
import numpy as np
from k_means_thresholding import k_means_thresholding


def filtered_k_means_thresholding(im1):
    mask = k_means_thresholding(im1)
    # kernel = np.ones((5,5),np.uint8)
    # mask_open = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
    kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(10,10))
    mask_open2 = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel2)
    kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(2,2))
    mask_open2_close = cv2.morphologyEx(mask_open2,cv2.MORPH_CLOSE,kernel2)
    
    # Display for test purposes
    # cv2.imshow('Original',im1)
    # cv2.imshow('Mask',mask)
    # cv2.imshow('Mask Open',mask_open)
    cv2.imshow('Mask Open2',mask_open2)
    cv2.imshow('Mask Open2 Close',mask_open2_close)
    cv2.waitKey(0)
    return mask_open2_close




if __name__ == '__main__':
    # Map command line arguments to function arguments.
    im1 = cv2.imread(sys.argv[1],0)
    outputfile = sys.argv[2]
    mask = filtered_k_means_thresholding(im1)
    cv2.imwrite(outputfile,mask)

