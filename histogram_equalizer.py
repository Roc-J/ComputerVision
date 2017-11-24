# -*- coding:utf-8 -*- 
# Author: Roc-J

import sys

import cv2
import numpy as np

input_file = sys.argv[1]
img = cv2.imread(input_file)

# 转化为灰度
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Input grayscale image', img_gray)

# 均衡直方图
img_gray_histeq = cv2.equalizeHist(img_gray)
cv2.imshow('Histogram equlized - grayscale', img_gray_histeq)

img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

img_yuv[:, :, 0] = cv2.equalizeHist(img_yuv[:, :, 0])

img_histeq = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

cv2.imshow('Input color image', img)
cv2.imshow('Histogram equalized - color', img_histeq)

cv2.waitKey()