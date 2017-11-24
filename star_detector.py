# -*- coding: utf-8 -*-
# Roc-J

import sys
import cv2

file_name = sys.argv[1]
file_img = cv2.imread(file_name)
orb = cv2.ORB()
keypoints = orb.detect(file_img, None)
cv2.drawKeypoints(file_img, keypoints, file_img, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('Star features', file_img)
cv2.waitKey()
