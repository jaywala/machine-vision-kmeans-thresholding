import sys
import imutils
import cv2
import numpy as np
import matplotlib.pyplot as plt
from k_means_thresholding import k_means_thresholding
from filtered_k_means_thresholding import filtered_k_means_thresholding


def count_eggs_4(im1):
    # mask = filtered_k_means_thresholding(im1)
    kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(8,8))
    im2 = cv2.morphologyEx(im1,cv2.MORPH_OPEN,kernel2)
    kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(2,2))
    mask = cv2.morphologyEx(im2,cv2.MORPH_CLOSE,kernel2)
    cv2.imshow('test',mask)
    mask = im1 > 0
    label_mask = np.zeros_like(mask,dtype=np.uint8)
    neighbour = [(-1,0),(1,0),(0,-1),(0,1)]
    label_count = 1
    for x in range(mask.shape[1]):
            for y in range(mask.shape[0]):
                if mask[y,x] != 0:
                    label_low =  label_count
                    found = False
                    for i in range(4):
                        if 0<=y+neighbour[i][0]<mask.shape[0] and 0<=x+neighbour[i][1]<mask.shape[1]:
                            if mask[y+neighbour[i][0],x+neighbour[i][1]] != 0 and label_mask[y+neighbour[i][0],x+neighbour[i][1]] != 0:
                                if label_mask[y+neighbour[i][0],x+neighbour[i][1]] < label_low:
                                    label_low = label_mask[y+neighbour[i][0],x+neighbour[i][1]]
                                    found = True
                    if found == False:
                        label_count += 1
                        # print(label_count)
                    label_mask[y,x] = label_low

    for x in range(label_mask.shape[1]):
        for y in range(label_mask.shape[0]):
            if mask[y,x] != 0:
                label_low = label_mask[y,x]
                for i in range(4):
                    if 0<=y+neighbour[i][0]<mask.shape[0] and 0<=x+neighbour[i][1]<mask.shape[1]:
                        if 0<label_mask[y+neighbour[i][0],x+neighbour[i][1]]<label_low:
                            label_low = label_mask[y+neighbour[i][0],x+neighbour[i][1]]
                label_mask[y,x] = label_low
    
    prev = 0
    count = 0
    for x in range(label_mask.shape[1]):
        for y in range(label_mask.shape[0]):
            if label_mask[y,x]>prev:
                prev = label_mask[y,x]
                count += 1
    print('count is {}'.format(count))
    print('prev is {}'.format(prev))

    


    color_img = cv2.cvtColor(label_mask,cv2.COLOR_GRAY2RGB)
    color_img[:,:,0] = (color_img[:,:,0]+8)*2
    color_img[:,:,1] = color_img[:,:,1]*3
    color_img[:,:,2] = color_img[:,:,2]*2
    cv2.imshow('colour image',color_img)
    cv2.waitKey(0)
    return color_img
    


                            
 


if __name__ == '__main__':
    # Map command line arguments to function arguments.
    im1 = cv2.imread(sys.argv[1],0)
    x = int(sys.argv[2])
    outputfile = sys.argv[3]
    im = count_eggs_4(im1)
    cv2.imwrite(outputfile,im)
