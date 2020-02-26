#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 17:50:21 2019

@author: Brenda
"""

#import necessary python packages, which contain functions we'll use below
import matplotlib.pyplot as plt
import imageio
import numpy as np
import os
import glob

#establish input+output directories
path = os.chdir('/Users/Brenda/Dropbox/Research/Data/Analysis/Python/DOPG10')
output_path = ('/Users/Brenda/Dropbox/Research/Data/Analysis/Python/DOPG10/bin')

for filename in glob.glob("*.png"):
    #import image as a matrix (an ndarray)
    img = imageio.imread(filename)
    
    ##threshold according to percentile
    bin75 = np.percentile(img,75)     #gives 75th percentile value in the image matrix; we'll use this as the threshold 
    imgthresh75 = np.empty(img.shape) #creates a new matrix for the binarized image
    imgthresh75[img > bin75] = 0      #fills empty matrix with black for parts of the image above the threshold 
    imgthresh75[img < bin75] = 255    #fills matrix with white below the threshold    
    plt.imshow(imgthresh75, interpolation='nearest') #shows new, binarized image
    plt.show()                          
    output_filepath =  os.path.join(output_path, filename + "_75" + '.png') #makes filename for binarized image based off of original name
    imageio.imwrite(output_filepath,imgthresh75) #writes the new binary image to the output directory
    
    
    bin50 = np.percentile(img,50)  
    imgthresh50 = np.empty(img.shape)
    imgthresh50[img > bin50] = 0
    imgthresh50[img < bin50] = 255        
    plt.imshow(imgthresh50, interpolation='nearest')
    plt.show()
    output_filepath =  os.path.join(output_path, filename + "_50" + '.png')
    imageio.imwrite(output_filepath,imgthresh50)
    
    bin25 = np.percentile(img,25)
    imgthresh25 = np.empty(img.shape)
    imgthresh25[img > bin25] = 0
    imgthresh25[img < bin25] = 255
    plt.imshow(imgthresh25, interpolation='nearest')
    plt.show()
    output_filepath =  os.path.join(output_path, filename + '_25' + '.png')
    imageio.imwrite(output_filepath,imgthresh25)
