import imutils
import cv2
import numpy as np
import matplotlib.pyplot as plt


def k_means_thresholding(im1):
    low_mean = 1.0
    high_mean = 254.0
    # change = 0
    # prev_low_mean
    # prev_high_mean
    # for x in range(im1.shape[1]):
    #     for y in range(im1.shape[0]):
    #         if abs(im1[y, x]-low_mean) < abs(im1[y, x]-high_mean):
    #             low_index.append((y, x))
    #             low_vals.append(im1[y, x])
    #         else:
    #             high_index.append((y, x))
    #             high_vals.append(im1[y, x])
    
    low_index = (abs(im1-low_mean) < abs(im1-high_mean))
    im2 = cv2.bitwise_and(im1, im1, mask=low_index)
    print
    cv2.imshow(im2)
    cv2.waitKey(0)
    # print("low_mean {}".format(low_mean))
    # print("highmean {}".format(high_mean))
    # print("no.of low values {}".format(len(low_vals)))
    # print("no.of low values {}".format(len(high_vals)))


im1 = cv2.imread('DataSamples/input_image_1.jpg', 0)
k_means_thresholding(im1)
