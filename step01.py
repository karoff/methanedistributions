# This is the first program in a series of 4 program to make the analysis for the paper
# entitled 'Analysis of atmospheric methane concentrations as function of geographic, 
# land cover type and season' by Christoffer Karoff.
# This program reads in the XCH4 and CO2 measurements from the NetCDF files prepared by
# the WFM-DOAS algorithm
import xarray as xr
import os
import glob
import jdcal
from tqdm import tqdm
# Download the data from https://www.iup.uni-bremen.de/carbon_ghg/products/tropomi_wfmd/
# and point to the directury, where you have stored them
path = '/Volumes/Methane/data/'
# We now open the files one by one. Read in the observing times, measurements, uncertainties
# and coordinates
for filename in tqdm(glob.glob(os.path.join(path, '*/*.nc'))):
	file=xr.open_dataset(filename)
	time=file['time'].values
	times=[]
	for i in range(len(time)):
		time2=str(time[i])
# We converte the times to julian dates
        times.append(jdcal.gcal2jd(time2[0:4],time2[5:7],time2[8:10])[1])
	xch4=file['xch4'].values
	xch4u=file['xch4_uncertainty'].values
	xco=file['xco'].values
	xcou=file['xco_uncertainty'].values
	latitude=file['latitude'].values
	longitude=file['longitude'].values
# We then store the parameters in the file methane_all01.txt
	for i in range(len(xch4)):
		l=str(i)+', '+str(times[i])+', '+str(longitude[i])+', '+str(latitude[i])+', '+str(xch4[i])+', '+str(xch4u[i])+', '+str(xco[i])+', '+str(xcou[i])+'\n'
		outfile=open('methane_all01.txt','a')
		outfile.writelines(l) 
		outfile.close()

