import sys
import imutils
import cv2
import numpy as np
import matplotlib.pyplot as plt
from k_means_thresholding import k_means_thresholding


def filtered_k_means_thresholding(im1):
    kernel = np.ones((3,3),np.uint8)
    open = cv2.morphologyEx(im1,cv2.MORPH_OPEN,kernel)

    #Display for test puroses
    cv2.imshow('Original',im1)
    cv2.imshow('Open',open)

    mask_orig = k_means_thresholding(im1)
    mask_open = k_means_thresholding(open)

    cv2.imshow('Original mask',mask_orig)
    cv2.imshow('Ope asjn',mask_open)

    cv2.imshow('morph after',cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel))

    cv2.waitKey(0)





if __name__ == '__main__':
    # Map command line arguments to function arguments.
    im1 = cv2.imread(sys.argv[1],0)
    outputfile = sys.argv[2]
    mask = filtered_k_means_thresholding(im1)
    cv2.imwrite(outputfile,mask)
