# This is the second program in a series of 4 program to make the analysis for the paper
# entitled 'Analysis of atmospheric methane concentrations as function of geographic, 
# land cover type and season' by Christoffer Karoff.
# This program look up the MODIS land cover classification for each XCH4 and XCO measurement
# and write them to a file
import pandas as pd
import numpy as np
import array as arr
import jdcal
from tqdm import tqdm
from pathlib import Path
import ee
ee.Initialize()
# Ask for the MODIS land cover classification in the region 3500 m from the central point
# of the XCH4 and XCO measurements
scale=3500
# Import the MODIS land cover classification collection.
lc = ee.ImageCollection('MODIS/006/MCD12Q1')
# Read in the methan measurements that we saved in the first program
headernames=['index', 'times', 'lon', 'lat', 'xch4', 'xch4u', 'xco', 'xcou']
# There are too many XCH4 and XCO measurements to that we can just make one call to 
# Google EE and it takes too long time to go through them one by one. We therefore
# call for 5000 in each call
for df in tqdm(pd.read_csv('methane_all01.txt', chunksize=5000, header=None, names=headernames)):
	timel=df['times']
	x=df['lon']
	y=df['lat']
	df.insert(8,'lc',0)
	xy=[]
# The MODIS land cover classifications have a resolution of one year. 
# We thus define an initial and final data that are 183 days from the time of the XCH4
# and XCO measurements on either side.
	time1=timel[df.index[0]]-183
	time2=timel[df.index[0]]+183
# We then converte from calendar date to julian data
    y1=jdcal.jd2gcal(2400000.5,time1)[0]
	m1=jdcal.jd2gcal(2400000.5,time1)[1]
	d1=jdcal.jd2gcal(2400000.5,time1)[2]
	y2=jdcal.jd2gcal(2400000.5,time2)[0]
	m2=jdcal.jd2gcal(2400000.5,time2)[1]
	d2=jdcal.jd2gcal(2400000.5,time2)[2]
# and write the dates as a string in the correct format
if (d1<10):
		i_date=str(y1)+'-'+str(m1)+'-0'+str(d1)
	else:
		i_date=str(y1)+'-'+str(m1)+'-'+str(d1)
	if (d2<10):
		f_date=str(y2)+'-'+str(m2)+'-0'+str(d2)
	else:
		f_date=str(y2)+'-'+str(m2)+'-'+str(d2)
	for i in df.index:
		xy.append([x[i],y[i]])
	poi=ee.Geometry.MultiPoint(xy)	
	lc_poi=lc.filterDate(i_date,f_date).select('LC_Type1')
	try:
		lc_r_poi=lc_poi.getRegion(poi,scale).getInfo()
# If for some reason we get less that 5000 replys, we assume that something
# went wrong
		if (len(lc_r_poi)>5000):
# We then save the 5000 values
            for i in range(5000):
				df.at[df.index[i],['lc']]=lc_r_poi[i+1][4] 

			file_path=Path('methane_all02.txt')
			if file_path.exists():	
				df.to_csv(file_path, mode='a', header=False, index=False)
			else:
				df.to_csv(file_path, mode='w', header=True, index= False)
	except:
		pass
