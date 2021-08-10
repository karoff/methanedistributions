# This is the a help program for a series of 4 program to make the analysis for the paper
# entitled 'Analysis of atmospheric methane concentrations as function of geographic, 
# land cover type and season' by Christoffer Karoff.
# There are two routines in this files. 'mplot1' that calculates the distributions and
# save them in 'temp' and 'mplot2' that makes the plots."
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
def mplot1(df,title,va,figname):
# Again difine the text strings for the caption'
	c=['c1','c2','c3','c4','c5','c6','c7','c8','c9','c10','c11','c12','c13','c14','c15','c16','c17','c18','all']
	titles=['Evergreen Needleleaf Forests','Evergreen Broadleaf Forests','Deciduous Needleleaf Forests','Deciduous Broadleaf Forests','Mixed Forests','Closed Shrublands','Open Shrublands','Woody Savannas','Savannas','Grasslands','Permanent Wetlands','Croplands','Urban and Built-up Lands','Cropland/Natural Vegetation Mosaics','Permanent Snow and Ice','Barren','Water Bodies','Any Land']
# The bin size dependts on which variable we are looking af.
	if (va=='xch4'):
		nbin=list(np.arange(1750,1950,4))
	if (va=='xco'):
		nbin=list(np.arange(50,150,3))
	for i in range(18):
		h_new=np.histogram(df[va][df['lc']==i+1], bins=nbin)
		if (i==17):
			h_new=np.histogram(df[va],bins=nbin)
		if (sum(h_new[0])>2):
			file_path=Path('temp/'+c[i]+'.npy')
			if file_path.exists():
				h_old=np.load(file_path, allow_pickle=True)
				h_old[0]+=h_new[0]
				np.save(file_path,h_old)
			else:
				h_old=h_new
				np.save(file_path,h_old)

def mplot2(title,va,figname):
# Now do the same thing, but this time, make the plots.
	c=['c1','c2','c3','c4','c5','c6','c7','c8','c9','c10','c11','c12','c13','c14','c15','c16','c17','c18','all']
	titles=['Evergreen Needleleaf Forests','Evergreen Broadleaf Forests','Deciduous Needleleaf Forests','Deciduous Broadleaf Forests','Mixed Forests','Closed Shrublands','Open Shrublands','Woody Savannas','Savannas','Grasslands','Permanent Wetlands','Croplands','Urban and Built-up Lands','Cropland/Natural Vegetation Mosaics','Permanent Snow and Ice','Barren','Water Bodies','Any Land']
	if (va=='xch4'):
		nbin=list(np.arange(1752,1948,4))
	if (va=='xco'):
		nbin=list(np.arange(51.5,148.5,3))
	fig,ax = plt.subplots(6,3, figsize=(10,12),sharex=True,constrained_layout=True)
	fig.suptitle(title)
	ax=ax.ravel()
	for i in range(18):
		file_path=Path('temp/'+c[i]+'.npy')
		if file_path.is_file():
			h_old=np.load(file_path,allow_pickle=True)
			if (sum(h_old[0]) > 100):
				#centroids
				#ax[i].hist(h_old[1],weights=h_old[0])
				ax[i].bar(nbin,h_old[0],width=4)
				m=np.average(nbin,weights=h_old[0])
				ax[i].axvline(x=m,color='r')
				ax[i].text(0.12,0.9,"{:.0f}".format(m),fontsize=12,ha='center', va='center', transform=ax[i].transAxes,color='red')
		ax[i].set_title(titles[i])
	if (va=='xch4'):
		ax[16].set_xlabel('XCH$_4$ [ppb]')
	if (va=='xco'):
		ax[16].set_xlabel('XCO [ppb]')
	plt.savefig(figname)
