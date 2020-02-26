#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 16:48:44 2019

@author: Brenda
"""

#Currently works for dicts with no nan values (potential workaround: find+remove indices corresponding to nan)

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_excel(r'/Users/Brenda/Dropbox/Research/Data/Analysis/Python/PG_all_variables.xlsx',index_col=0)

#Wetting Var
DOPG_CA_mmt = data.loc[["MMT0","DOPG10","DOPG25","DOPG50"],["CA0_avg"]].to_numpy()
DOPG_TC_mmt = data.loc[["MMT0","DOPG10","DOPG25","DOPG50"],["TC_avg"]].to_numpy()
DOPG_a_mmt = data.loc[["MMT0","DOPG10","DOPG25","DOPG50"],["a_avg"]].to_numpy()

DOPG_CA = data.loc[["DOPG10","DOPG25","DOPG50"],["CA0_avg"]].to_numpy()
DOPG_TC = data.loc[["DOPG10","DOPG25","DOPG50"],["TC_avg"]].to_numpy()
DOPG_a = data.loc[["DOPG10","DOPG25","DOPG50"],["a_avg"]].to_numpy()

DSPG_CA_mmt = data.loc[["MMT0","DSPG10","DSPG25","DSPG50"],["CA0_avg"]].to_numpy()
DSPG_TC_mmt = data.loc[["MMT0","DSPG10","DSPG25","DSPG50"],["TC_avg"]].to_numpy()
DSPG_a_mmt = data.loc[["MMT0","DSPG10","DSPG25","DSPG50"],["a_avg"]].to_numpy()
DSPG_CA = data.loc[["DSPG10","DSPG25","DSPG50"],["CA0_avg"]].to_numpy()
DSPG_TC = data.loc[["DSPG10","DSPG25","DSPG50"],["TC_avg"]].to_numpy()
DSPG_a = data.loc[["DSPG10","DSPG25","DSPG50"],["a_avg"]].to_numpy()

#PhysVar
DOPG_AvgDiam = data.loc[["DOPG10","DOPG25","DOPG50"],["Avg diameter (nm)"]].to_numpy()
DOPG_AggDen = data.loc[["DOPG10","DOPG25","DOPG50"],["Aggregate/nm2 Estimate"]].to_numpy()
DOPG_EdgeFrac = data.loc[["DOPG10","DOPG25","DOPG50"],["edge/total aggregates"]].to_numpy()
DOPG_flbin25_junc = data.loc[["DOPG10","DOPG25","DOPG50"],["Bin25Fl Junc"]].to_numpy()
DOPG_flbin50_junc = data.loc[["DOPG10","DOPG25","DOPG50"],["Bin50Fl Junc"]].to_numpy()
DOPG_flbin75_junc = data.loc[["DOPG10","DOPG25","DOPG50"],["Bin75Fl Junc"]].to_numpy()
DOPG_flbin25_skelrat = data.loc[["DOPG10","DOPG25","DOPG50"],["Bin25Fl SkelRat"]].to_numpy()
DOPG_flbin50_skelrat = data.loc[["DOPG10","DOPG25","DOPG50"],["Bin50Fl SkelRat"]].to_numpy()
DOPG_flbin75_skelrat = data.loc[["DOPG10","DOPG25","DOPG50"],["Bin75Fl Skelrat"]].to_numpy()
DOPG_afmbin25_junc = data.loc[["DOPG10","DOPG25","DOPG50"],["Bin25AFM Junc"]].to_numpy()
DOPG_afmbin50_junc = data.loc[["DOPG10","DOPG25","DOPG50"],["Bin50AFM Junc"]].to_numpy()
DOPG_afmbin75_junc = data.loc[["DOPG10","DOPG25","DOPG50"],["Bin75AFM Junc"]].to_numpy()
DOPG_afmbin25_skelrat = data.loc[["DOPG10","DOPG25","DOPG50"],["Bin25AFM SkelRat"]].to_numpy()
DOPG_afmbin50_skelrat = data.loc[["DOPG10","DOPG25","DOPG50"],["Bin50AFM SkelRat"]].to_numpy()
DOPG_afmbin75_skelrat = data.loc[["DOPG10","DOPG25","DOPG50"],["Bin75AFM Skelrat"]].to_numpy()

DSPG_flbin25_junc = data.loc[["DSPG10","DSPG25","DSPG50"],["Bin25Fl Junc"]].to_numpy()
DSPG_flbin50_junc = data.loc[["DSPG10","DSPG25","DSPG50"],["Bin50Fl Junc"]].to_numpy()
DSPG_flbin75_junc = data.loc[["DSPG10","DSPG25","DSPG50"],["Bin75Fl Junc"]].to_numpy()
DSPG_flbin25_skelrat = data.loc[["DSPG10","DSPG25","DSPG50"],["Bin25Fl SkelRat"]].to_numpy()
DSPG_flbin50_skelrat = data.loc[["DSPG10","DSPG25","DSPG50"],["Bin50Fl SkelRat"]].to_numpy()
DSPG_flbin75_skelrat = data.loc[["DSPG10","DSPG25","DSPG50"],["Bin75Fl Skelrat"]].to_numpy()
DSPG_afmbin25_junc = data.loc[["DSPG10","DSPG25","DSPG50"],["Bin25AFM Junc"]].to_numpy()
DSPG_afmbin50_junc = data.loc[["DSPG10","DSPG25","DSPG50"],["Bin50AFM Junc"]].to_numpy()
DSPG_afmbin75_junc = data.loc[["DSPG10","DSPG25","DSPG50"],["Bin75AFM Junc"]].to_numpy()
DSPG_afmbin25_skelrat = data.loc[["DSPG10","DSPG25","DSPG50"],["Bin25AFM SkelRat"]].to_numpy()
DSPG_afmbin50_skelrat = data.loc[["DSPG10","DSPG25","DSPG50"],["Bin50AFM SkelRat"]].to_numpy()
DSPG_afmbin75_skelrat = data.loc[["DSPG10","DSPG25","DSPG50"],["Bin75AFM Skelrat"]].to_numpy()

#########Dictionary time############
DOPG_Wet = {'DOPG_CA': DOPG_CA.reshape(-1, 1), 'DOPG_TC':DOPG_TC.reshape(-1, 1),'DOPG_a':DOPG_a.reshape(-1,1)}
DOPG_Phys = {'DOPG_AvgDiam': DOPG_AvgDiam.reshape(-1, 1), 'DOPG_AggDen':DOPG_AggDen.reshape(-1, 1),'DOPG_EdgeFrac':DOPG_EdgeFrac.reshape(-1,1),'DOPG_flbin25_junc':DOPG_flbin25_junc.reshape(-1, 1),'DOPG_flbin50_junc':DOPG_flbin50_junc.reshape(-1, 1),'DOPG_flbin75_junc':DOPG_flbin75_junc.reshape(-1, 1),'DOPG_flbin25_skelrat':DOPG_flbin25_skelrat.reshape(-1, 1),'DOPG_flbin50_skelrat':DOPG_flbin50_skelrat.reshape(-1, 1),'DOPG_flbin75_skelrat':DOPG_flbin75_skelrat.reshape(-1, 1),'DOPG_afmbin25_junc':DOPG_afmbin25_junc.reshape(-1, 1),'DOPG_afmbin50_junc':DOPG_afmbin50_junc.reshape(-1, 1),'DOPG_afmbin75_junc':DOPG_afmbin75_junc.reshape(-1, 1),'DOPG_afmbin25_skelrat':DOPG_afmbin25_skelrat.reshape(-1, 1),'DOPG_afmbin50_skelrat':DOPG_afmbin50_skelrat.reshape(-1, 1),'DOPG_afmbin75_skelrat':DOPG_afmbin75_skelrat.reshape(-1, 1)}

DSPG_Wet = {'DSPG_CA': DSPG_CA.reshape(-1, 1), 'DSPG_TC':DSPG_TC.reshape(-1, 1),'DSPG_a':DSPG_a.reshape(-1,1)}
DSPG_Phys = {'DSPG_flbin25_junc':DSPG_flbin25_junc.reshape(-1, 1),'DSPG_flbin50_junc':DSPG_flbin50_junc.reshape(-1, 1),'DSPG_flbin75_junc':DSPG_flbin75_junc.reshape(-1, 1),'DSPG_flbin25_skelrat':DSPG_flbin25_skelrat.reshape(-1, 1),'DSPG_flbin50_skelrat':DSPG_flbin50_skelrat.reshape(-1, 1),'DSPG_flbin75_skelrat':DSPG_flbin75_skelrat.reshape(-1, 1),'DSPG_afmbin25_junc':DSPG_afmbin25_junc.reshape(-1, 1),'DSPG_afmbin50_junc':DSPG_afmbin50_junc.reshape(-1, 1),'DSPG_afmbin75_junc':DSPG_afmbin75_junc.reshape(-1, 1),'DSPG_afmbin25_skelrat':DSPG_afmbin25_skelrat.reshape(-1, 1),'DSPG_afmbin50_skelrat':DSPG_afmbin50_skelrat.reshape(-1, 1),'DSPG_afmbin75_skelrat':DSPG_afmbin75_skelrat.reshape(-1, 1)}

#testLR = LinearRegression().fit(Lip1EdgeFrac,Lip1a)
#print(testLR.score(Lip1EdgeFrac,Lip1a),testLR.coef_)


for N,W in DOPG_Wet.items(): #Am using N,M here to refer to the Key and P,W to the Value
    for M,P in DOPG_Phys.items():
        LR = LinearRegression().fit(P,W)
        print(N, M, 'r2', LR.score(P,W), 'slope', LR.coef_)

for NS,WS in DSPG_Wet.items(): #Am using N,M here to refer to the Key and P,W to the Value
    for MS,PS in DSPG_Phys.items():
        LR = LinearRegression().fit(PS,WS)
        print(NS, MS, 'r2', LR.score(PS,WS), 'slope', LR.coef_)        
        
####Special DSPG ones that have 10%, 25%, and 30% only####
DSPG_AvgDiam = data.loc[["DSPG10","DSPG25","DSPG30"],["Avg diameter (nm)"]].to_numpy()
DSPG_AggDen = data.loc[["DSPG10","DSPG25","DSPG30"],["Aggregate/nm2 Estimate"]].to_numpy()
DSPG_EdgeFrac = data.loc[["DSPG10","DSPG25","DSPG30"],["edge/total aggregates"]].to_numpy() 
 
DSPG_CA_c = data.loc[["DSPG10","DSPG25","DSPG30"],["CA0_avg"]].to_numpy()  #C for Cypher, since we're doing this for cypher data.
DSPG_TC_c = data.loc[["DSPG10","DSPG25","DSPG30"],["TC_avg"]].to_numpy()
DSPG_a_c = data.loc[["DSPG10","DSPG25","DSPG30"],["a_avg"]].to_numpy() 

DSPGc_Wet = {'DSPG_CA':DSPG_CA_c.reshape(-1, 1),'DSPG_TC':DSPG_TC_c.reshape(-1, 1),'DSPG_a':DSPG_a_c.reshape(-1, 1)}
DSPGc_Phys = {'DSPG_AvgDiam':DSPG_AvgDiam.reshape(-1, 1),'DSPG_AggDen':DSPG_AggDen.reshape(-1, 1),'DSPG_EdgeFrac':DSPG_EdgeFrac.reshape(-1, 1)}   

for O,X in DSPGc_Wet.items(): #Am using N,M here to refer to the Key and P,W to the Value
    for Q,R in DSPGc_Phys.items():
        LR = LinearRegression().fit(R,X)
        print(O, Q, 'r2', LR.score(R,X), 'slope', LR.coef_)