# -*- coding: utf-8 -*-
"""
Created on Mon July 16th,2018

@author:  IPMI, ISTB, University of Bern
"""

import os
import SimpleITK as sitk

inputDir = '/input'
outputDir = '/output'

# Load the image
fatImage = sitk.ReadImage(os.path.join(inputDir, 'fat.nii.gz'))
innImage = sitk.ReadImage(os.path.join(inputDir, 'inn.nii.gz'))
oppImage = sitk.ReadImage(os.path.join(inputDir, 'opp.nii.gz'))
watImage = sitk.ReadImage(os.path.join(inputDir, 'wat.nii.gz'))

# SimpleITK: binary threshold between 0 - 20
resultImage = sitk.BinaryThreshold(fatImage, lowerThreshold=0, upperThreshold=20)

sitk.WriteImage(resultImage, os.path.join(outputDir, 'result.nii.gz'))