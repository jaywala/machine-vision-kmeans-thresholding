import sys
import imutils
import cv2
import numpy as np
import matplotlib.pyplot as plt


def k_means_thresholding(im1):
    low_mean = 40
    high_mean = 205
    change = True
    prev_low_mean = None
    prev_high_mean = None
    while change:
        low_vals = []
        high_vals = []
        for x in range(im1.shape[1]):
            for y in range(im1.shape[0]):
                if abs(im1[y, x]-low_mean) < abs(im1[y, x]-high_mean):
                    low_vals.append(im1[y, x])
                else:
                    high_vals.append(im1[y, x])
        if (len(low_vals)==0):
            low_mean = 0
        else:
            low_mean = sum(low_vals)/len(low_vals)
        if (len(high_vals)==0):
            high_mean = 0
        else:
            high_mean = sum(high_vals)/len(high_vals)
        change = (low_mean != prev_low_mean or high_mean != prev_high_mean)
        prev_low_mean = low_mean
        prev_high_mean = high_mean

    mask = np.array(abs(im1-low_mean) < abs(im1-high_mean),dtype=np.uint8) * 255

    # im2 = np.empty(im1.size)

    # im2[np.array(low_index)] = 1
        
    # im2[np.array(high_index)] = 0

    
    # print("low_mean {}".format(low_mean))
    # print("highmean {}".format(high_mean))
    # print("no.of low values {}".format(len(low_vals)))
    # print("no.of low values {}".format(len(high_vals)))

    # im6 = im1 * mask
    # cv2.imshow('image 1',mask*255)
    # cv2.imshow('image 2',im6)
    # cv2.waitKey(0)

    return mask

if __name__ == '__main__':
    # Map command line arguments to function arguments.
    im1 = cv2.imread(sys.argv[1],0)
    outputfile = sys.argv[2]
    mask = k_means_thresholding(im1)
    cv2.imwrite(outputfile,mask)
