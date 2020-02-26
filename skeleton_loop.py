#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 16:26:35 2019

@author: Brenda
"""
#importing all the python packages we're going to use
import numpy as np
import pandas as pd
from skimage import io
import glob
import os

directory = os.chdir('/Users/Brenda/Dropbox/Research/Data/Analysis/2019Images for analysis - PGs/PG AFM Skel') #tells the code where your files are
ratioList = []  #these lines set up lists that will be filled with information we want
sampleList = []

for filename in glob.glob("*.tif"):        #initializes a loop so that every file in the directory is analyzed
    
    skeleton = io.imread(filename)          #reads the file as a matrix where white pixels have a value of 0 and black pixels have a value of 255
    blackpixels = np.count_nonzero(skeleton) #counts all the black pixels
    skel_ratio = blackpixels/skeleton.size   #divides the number of black pixels by the total number of pixels in the image
    
    print(filename,skel_ratio)    #I put this here as a "sanity check"; it should list every file in the directory
    
    sampleList.append(filename)   #these lines write the values to the lists initialized in lines 16 + 17
    ratioList.append(skel_ratio)
    
    
#these lines write the values to a csv file, along with the sample name
dataframe = pd.DataFrame({"sample":sampleList,"skel ratio":ratioList})
dataframe.to_csv('/Users/Brenda/Dropbox/Research/Data/Analysis/2019Images for analysis - PGs/PGafm_skelratio.csv')