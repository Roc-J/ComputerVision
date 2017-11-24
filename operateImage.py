# -*- coding:utf-8 -*- 
# Author: Roc-J

import sys
import cv2
import numpy as np

input_file = sys.argv[1]
img = cv2.imread(input_file)

cv2.imshow('Original', img)

# 裁剪图像
h, w = img.shape[:2]
start_row, end_start = int(0.21*h), int(0.73*h)
start_col, end_col = int(0.37*w), int(0.92*w)

img_cropped = img[start_row:end_start, start_col:end_col]
cv2.imshow('Cropped', img_cropped)

# 调整图像大小
scaling_factor = 1.3
img_scaled = cv2.resize(img, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_LINEAR)
cv2.imshow('Uniform resizing', img_scaled)

img_scaled = cv2.resize(img, (250, 400), interpolation=cv2.INTER_AREA)
cv2.imshow('Skewed resizing', img_scaled)

# 保存图像

cv2.waitKey()
