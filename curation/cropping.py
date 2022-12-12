from glob import glob
import numpy as np
import pandas as pd
import os
import cv2

def crop(path):
    
    origin_img = cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGB)
    
    gray_img = cv2.cvtColor(origin_img, cv2.COLOR_RGB2GRAY)
    img = np.array(gray_img, dtype=np.uint8)
    
    
    #opeing 기법 적용
    kernel = np.ones((5,5),np.uint8)
    opeing_img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations = 3)
    
    #Canny edge 방법을 적용하여 edge 검출
    edge_img = cv2.Canny(opeing_img,10,70)
    

    # left, right, top, bottom index를 찾아서 cropping 진행
    
    len_width = len(edge_img[144,:])

    #vertical 방향으로 idx 확인
    img_index_left = []
    img_index_right = []

    for i in range(len_width):
        vertical_sum_left = np.sum(edge_img[:,i]/255)
        
        if vertical_sum_left > 110:
            img_index_left.append(i)

        #gray scale의 각 픽셀 값이 8비트이기 때문에 255로 나누어 주기
        vertical_sum_right = np.sum(edge_img[:,-(i+1)]/255)
        
        if vertical_sum_right > 100:
            real_right_idx = len_width - (i+1) 
            img_index_right.append(real_right_idx)    

            
    len_height = len(edge_img[:,144])
    #horizontal 방향으로 idx 확인
    img_index_up = []
    img_index_down = []
    
    for i in range(len_height):

        horizontal_sum_up = np.sum(edge_img[i,:]/255)
        if horizontal_sum_up > 200:
            img_index_up.append(i)

        horizontal_sum_down = np.sum(edge_img[-(i+1),:]/255)
        horizontal_sum_end = np.sum(edge_img[-1,:]/255)

        if horizontal_sum_down > 200:
            if horizontal_sum_end != 0:
                real_down_idx = len_height-1
                img_index_down.append(real_down_idx)    
            else:
                real_down_idx = len_height - (i+1) 
                img_index_down.append(real_down_idx)    

    cropped_img = origin_img[img_index_up[0]:img_index_down[0], img_index_left[0]:img_index_right[0]]
    
    return cropped_img