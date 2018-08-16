import sys
import cv2
import numpy as np


def count_eggs_4(im1,min_comp_size):
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

    # First Pass of finding Connected Components
    for x in range(mask.shape[1]):
            for y in range(mask.shape[0]):
                if mask[y,x] != 0:
                    label_low =  label_count
                    found = False
                    for i in range(4):
                        # Check if neighbour is within the 
                        if 0<=y+neighbour[i][0]<mask.shape[0] and 0<=x+neighbour[i][1]<mask.shape[1]:
                            if mask[y+neighbour[i][0],x+neighbour[i][1]] != 0 and label_mask[y+neighbour[i][0],x+neighbour[i][1]] != 0:
                                if label_mask[y+neighbour[i][0],x+neighbour[i][1]] < label_low:
                                    label_low = label_mask[y+neighbour[i][0],x+neighbour[i][1]]
                                    found = True
                    if found == False:
                        label_count += 1
                        # print(label_count)
                    label_mask[y,x] = label_low

    # Second Pass for finding connected components
    for x in range(label_mask.shape[1]):
        for y in range(label_mask.shape[0]):
            if mask[y,x] != 0:
                label_low = label_mask[y,x]
                for i in range(4):
                    if 0<=y+neighbour[i][0]<mask.shape[0] and 0<=x+neighbour[i][1]<mask.shape[1]:
                        if 0<label_mask[y+neighbour[i][0],x+neighbour[i][1]]<label_low:
                            label_low = label_mask[y+neighbour[i][0],x+neighbour[i][1]]
                label_mask[y,x] = label_low
    
    # Count Pixel size of each component
    size_count = np.zeros(label_count)
    for x in range(label_mask.shape[1]):
        for y in range(label_mask.shape[0]):
            size_count[label_mask[y,x]] += 1

    for x in range(label_mask.shape[1]):
        for y in range(label_mask.shape[0]):
            if (size_count[label_mask[y,x]] < min_comp_size):
                label_mask[y,x] = 0
                size_count[label_mask[y,x]] -= 1

    prev = 0
    count = 0
    for x in range(label_mask.shape[1]):
        for y in range(label_mask.shape[0]):
            if label_mask[y,x]>prev:
                prev = label_mask[y,x]
                count += 1

    print('For Testing prev count is {}'.format(prev))
    print('Egg count is {}'.format(count))
    

    # gray_image = np.array((label_mask != 0),dtype=np.uint8)

    color_img = cv2.cvtColor(im1,cv2.COLOR_GRAY2RGB)
    color_img[:,:,0] = color_img[:,:,0] - label_mask * 40
    color_img[:,:,1] = color_img[:,:,1] - label_mask * 12
    color_img[:,:,2] = color_img[:,:,2] - label_mask * 42
    cv2.imshow('colour image',color_img)
    cv2.waitKey(0)
    return color_img
    


                            
 


if __name__ == '__main__':
    # Map command line arguments to function arguments.
    im1 = cv2.imread(sys.argv[1],0)
    size = int(sys.argv[2])
    outputfile = sys.argv[3]
    im = count_eggs_4(im1,size)
    cv2.imwrite(outputfile,im)
