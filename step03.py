# This is the second program in a series of 4 program to make the analysis for the paper
# entitled 'Analysis of atmospheric methane concentrations as function of geographic, 
# land cover type and season' by Christoffer Karoff.
# This program draw all the histograms.
import os
import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
from tqdm import tqdm
from mplot import mplot1,mplot2

# Download a continent shape file from here: https://hub.arcgis.com/datasets/esri::world-continents/ and load it in.
# You might was to consitere reducing the resolution. This can be fone here: https://mapshaper.org
poly = gpd.read_file('World_Continents/4a7d27e1-84a3-4d6a-b4c2-6b6919f3cf4b202034-1-2zg7ul.ht5ut.shp')

# Importing the geometry for the different continents
Africa=poly.geometry[0]
Asia=poly.geometry[1]
Australia=poly.geometry[2]
Northamerica=poly.geometry[3]
Oceania=poly.geometry[4]
Southamerica=poly.geometry[5]
Antarctica=poly.geometry[6]
Europa=poly.geometry[7]

# Defining text strings needed for the figures
variable=['xch4','xco']
subtitles=['Vinter','Spring','Summer','Fall','All Seasons']
continents=['Africa','Asia','Australia','North America','Oceania','South America','Antarctica','Europa','World']

# Defining the bouders of the different seasons
seasons=[58108, 58197, 58290, 58384, 58473, 58562, 58655, 58749, 58839, 58928, 59020, 59114]

# Loops over all continents
for i in tqdm(range(9)):
# Loops over all seasons
	for j in range(5):
# Loops over all land cover type
		for vari in variable:
			files=glob.glob('temp/*')
			for f in files:
				os.remove(f)
# Read in 1000.000 lines at a time and stor the distributions in 'temp'
			for df in pd.read_csv('methane_all02.txt', chunksize=100000):
				gdf =gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.lon, df.lat))
				if (i<8):
					subset0=df[gdf.within(poly.geometry[i])]
# The last continent is the whole world
				else:
					subset0=df
# The first time interval is anytime
				if (len(subset0['times']) > 2):
					if (j==4):
						subset=subset0
					else:
						subset=subset0[((seasons[j]<subset0['times']) & (seasons[j+1]>subset0['times'])) | ((seasons[j+4]<subset0['times']) & (seasons[j+5]>subset0['times']))]
# Call the plotting routine that calculates the distributions and save them in 'term'
					mplot1(subset,continents[i]+' '+subtitles[j],vari,'fig/'+continents[i]+'_'+subtitles[j]+'.png')
			files=glob.glob('temp/*')
# If there are files in 'temp' make the plot.
			if (len(files) > 2):
				mplot2(continents[i]+' '+subtitles[j],vari,'fig/'+vari+'_'+continents[i]+'_'+subtitles[j]+'.png')


