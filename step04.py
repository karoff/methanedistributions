# This is the first program in a series of 4 program to make the analysis for the paper
# entitled 'Analysis of atmospheric methane concentrations as function of geographic, 
# land cover type and season' by Christoffer Karoff.
# This program plots a large color coded matrix, which shows the mean value of all the distributions. 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np
# Read in a prewritten csv file with all the mean values and plot it with seaborn
df = pd.read_csv('matrix.csv',index_col=0)
df.index = df.index.astype(str)
fig, ax = plt.subplots(figsize=(18, 18))
sb.heatmap(df, annot=True, fmt='.0f', cbar_kws={'orientation': 'horizontal','shrink':0.8,'label':'XCH$_4$ [ppb]'},cmap='rocket_r')
plt.savefig('fig/matrix.png')
