from glob import glob
import numpy as np
import pandas as pd
import os
import cv2

def crop_external(path):
    origin_img = cv2.imread(path)
    origin_img = cv2.cvtColor(origin_img ,cv2.COLOR_BGR2RGB)

    gray_img = cv2.cvtColor(origin_img, cv2.COLOR_RGB2GRAY)
    img = np.array(gray_img, dtype=np.uint8)


    #opeing 기법 적용
    kernel = np.ones((7,7),np.uint8)
    opeing_img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations = 3)

    #Canny edge 방법을 적용하여 edge 검출
    edge_img = cv2.Canny(opeing_img,10,90)


    # left, right, top, bottom index를 찾아서 cropping 진행

    len_width = len(edge_img[144,:])

    #vertical 방향으로 idx 확인
    img_index_left = []
    img_index_right = []

    for i in range(len_width):
        vertical_sum_left = np.sum(edge_img[:,i]/255)
        left_init = np.sum(edge_img[:,0]/255)

        if left_init == 0: 
            if vertical_sum_left > 10:
                img_index_left.append(i)

        else:
            img_index_left.append(0)

        #gray scale의 각 픽셀 값이 8비트이기 때문에 255로 나누어 주기
        vertical_sum_right = np.sum(edge_img[:,-(i+1)]/255)
        right_init = np.sum(edge_img[:,-1]/255)

        if right_init == 0: 
            if vertical_sum_right > 10:
                real_right_idx = len_width - (i+1) 
                img_index_right.append(real_right_idx) 

        else:
            right_index = len_width - 1    
            img_index_right.append(right_index)

    index_left = img_index_left[0]
    index_right = img_index_right[0]

    len_height = len(edge_img[:,144])
    #horizontal 방향으로 idx 확인
    img_index_up = []
    img_index_down = []

    for i in range(len_height):

        horizontal_sum_up = np.sum(edge_img[i,:]/255)
        up_init = np.sum(edge_img[0,:]/255)

        if up_init == 0:
            if horizontal_sum_up > 10:
                img_index_up.append(i)

        else:
            img_index_up.append(0) 

        horizontal_sum_down = np.sum(edge_img[-(i+1),:]/255)
        down_init = np.sum(edge_img[-1,:]/255)

        if down_init == 0: 
            if horizontal_sum_down > 10:
                real_down_idx = len_height - (i+1) 
                img_index_down.append(real_down_idx)

        else:
            down_index = len_height - 1 
            img_index_down.append(down_index)

    index_up = img_index_up[0]
    index_down = img_index_down[0]

    origin_img = origin_img[index_up:index_down, index_left:index_right]
    
    return origin_img