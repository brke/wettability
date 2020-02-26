#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 06:25:22 2019

@author: Brenda
"""
import numpy as np
import pandas as pd
import glob
import os
import matplotlib.pyplot as plt
from scipy import optimize

directory = os.chdir('/Users/Brenda/Dropbox/Research/Data/Analysis/Python/PG_radii/') #tells the code where your files are
aList = []  #these lines set up lists that will be filled with information we want
kList = []
sampleList = []

for filename in glob.glob("*.csv"):        #initializes a loop so that every file in the directory is analyzed
    
    #csv read
    data = pd.read_csv(filename)
    #radius= some index
    diameter = data.iloc[:,3] #python claims this index doesn't exist and i don't know why, but the code still generates believable a and K vals
    time = data.iloc[:,0]
    #fit radius/radius0
    D0 = data.iloc[0,3]
    radRAT = (diameter/2)/(D0/2)

    def func(x, a, b):
        return a*(pow(x,b))+1
    
    params,params_covariance = optimize.curve_fit(func,time,radRAT,p0=[1,0.1])

    alpha = params[0]
    k = params[1]
    
    sampleList.append(filename)   #these lines write the values to the lists initialized in lines 16 + 17
    aList.append(alpha)
    kList.append(k)
    
    
#these lines write the values to a csv file, along with the sample name
dataframe = pd.DataFrame({"sample":sampleList,"a":aList, "k":kList})
dataframe.to_csv('/Users/Brenda/Dropbox/Research/Data/Analysis/Python/pg_a_k.csv')