# Program for plotting XCH4 and XCO distributions
link to paper

## Overview and contents 
This repository contains code and spreadsheets supporting the paper "Analysis of atmospheric methane concentrations as function of geographic, land cover type and season".

The analysis is based on observations from the TROPOMI instrument on Sentinel-5P reduced with the [WFM-DOAS algorithm](https://www.iup.uni-bremen.de/carbon_ghg/products/tropomi_wfmd/) and the [RemoTeC algorithm](https://www.sron.nl/earth-data-access).

For the analysis distribution of XCH4 and XCO are calculated as function of continent, land cover type and season.

Information of land cover type is obtained from [MODIS](https://developers.google.com/earth-engine/datasets/catalog/MODIS_006_MCD12Q1) and [ESA](https://esa-worldcover.org/en/about/about)



Continent maps are obtained from [Esri](https://hub.arcgis.com/datasets/esri::world-continents/).

## Software requirements and installation
The programs makes use of the following standard packages: xarray, os, glob, jdcal, pandas, geopandas, numpy, tqdm, pathlib, matplotlib, seaborn and the Earth Engine Python API ee. Instructions for installing ee can be found [here](https://developers.google.com/earth-engine/guides/python_install).

## Program structure
There are 4 program that needs to be run in consecutive order. These are:

 - [step01.py](step01.py) - This program reads in the XCH4 and CO2 measurements from the NetCDF files prepared by the WFM-DOAS algorithm.
 - [step02.py](step02.py) - This program look up the MODIS land cover classification for each XCH4 and XCO measurement and write them to a file.
 - [step03.py](step03.py) - This program draw all the histograms.
 - [step04.py](step04.py) - This program plots a large color coded matrix, which shows the mean value of all the distributions. 

## Plots
A folder with pre-made plots can be found here: [SRON_ESA](SRON_ESA), [SRON_MODIS](SRON_MODIS), [WFMD_ESA](WFMD_ESA) and [WFMD_MODIS](WFMD_MODIS),.



