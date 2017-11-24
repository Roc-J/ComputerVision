# -*- coding:utf-8 -*- 
# Author: Roc-J

import sys
import cv2
import numpy as np

input_file = sys.argv[1]
img = cv2.imread(input_file)
cv2.imshow('Input image ', img)

img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
img_gray = np.float32(img_gray)

# 哈里斯角检测器
img_harris = cv2.cornerHarris(img_gray, 7, 5, 0.04)
img_harris = cv2.dilate(img_harris, None)
img[img_harris > 0.01 * img_harris.max()] = [0, 0, 0]

cv2.imshow('Harris Corners', img)
cv2.waitKey()