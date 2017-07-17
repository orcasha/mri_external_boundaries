# -*- coding: utf-8 -*-
"""
Attempt script to produce outline of structural MRI scan.
Stage 1: Find image boundaries (check).
Stage 2: Find internal boundaries
To do - Erode 

Created on Fri Jun 24 13:39:55 2016

@author: peter
"""
from __future__ import division
import cv2
from skimage import filters
import numpy as np
import nibabel as nb

tempIm=nb.load('/home/peter/mricron/templates/ch2better.nii.gz')
#tempIm=nb.load('/home/peter/resources/space_templates/MNI152_T1_1mm_brain.nii')

im_data=tempIm.get_data()

d_bdr=np.zeros([np.shape(im_data)[0],np.shape(im_data)[1],np.shape(im_data)[2]])

thr_val=filters.threshold_otsu(im_data)

d_th=im_data>thr_val

brain_vox=np.where(d_th==1)

d_th=d_th.astype(int)

#for x in range(0,np.shape(d_th)[2]):
#    imslice=d_th[x]
#    imshow(imslice)
#    contours, hierarchy = cv2.findContours(imslice,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#    d_bdr[x]=np.array(contours)
        
img1=nb.Nifti1Image(d_th, header=tempIm.get_header(), affine=tempIm.get_affine()); img1.to_filename('/home/peter/Desktop/test_thr.nii')

#img2=nb.Nifti1Image(d_bdr, header=tempIm.get_header(), affine=tempIm.get_affine()); img1.to_filename('/home/peter/Desktop/test_bdr.nii')


