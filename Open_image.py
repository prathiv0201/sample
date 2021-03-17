# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 11:02:48 2021

@author: Pranesh Jayaprakash
"""
import numpy as np
import cv2
import pickle,os
img=cv2.imread(r"C:\Users\Pranesh Jayaprakash\Downloads\WhatsApp Image 2021-02-11 at 10.35.09 AM.jpeg",cv2.IMREAD_UNCHANGED)
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyallwindows()