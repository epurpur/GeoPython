#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 16:26:07 2019

@author: ep9k
"""

#these packages do not come with base python or Anaconda and must be installed on their own using pip or conda
import geopandas as gpd
import pandas as pd
import os







filepath = '/Users/ep9k/Desktop/GeopythonData/MikeTroutData.csv'


####Pandas
#Let's first work with pandas to get familiar with it
#df = pd.read_csv(filepath)

#As you can see, this looks like a spreadsheet. But now it is a pandas dataframe object which we can manipulate in python
#print(df)
#print(type(df))

#prints a list of the column headers. This becomes very helpful when you have a large dataset with many columns and rows
#print(df.columns)

#Access individual columns
#print(df['HR'])

#lots of functions are available to work with dataframe objects
#print(df['HR'].sum())


#make a new column on the fly
#df['Hits per Home Run'] = df['H'] / df['HR']
#print(df)  #now there are 11 columns
#print(df['Hits per Home Run'])

#you can also access columns this way 
#print(df.Salary)

#Access rows in pandas dataframe using .iloc.  This works for rows at particular positions
#print(df.iloc[0])   #print first year

#print(df.iloc[0:5])  #print first 5 rows


#Access rows with particular labels using .loc
#print(df.loc[df['Age'] > 24])  #prints all rows where age > 24



####GeoPandas

#filepath = '/Users/ep9k/Desktop/GeopythonData/Europe_Borders.shp'

#data = gpd.read_file(filepath)

#reads the data as a dataframe again
#print(data)
#print(data.crs)

#Uses the geometry column to plot the objects on a graphic
#data.plot()

#You can change the coordinate reference system of the data
#a coordinate reference system is a system which gives location and units of measurement to all locations on the globe
#There are many coordinate reference systems (crs). They are identified with an EPSG number
#EPSG - European Petroleum Survey Group. EPSG # is a unique number for each CRS
#data_reproject = data.copy()
#data_reproject = data_reproject.to_crs(epsg=3035)
#print(data_reproject)          #now unit of measurement is in meters instead of decimal degrees


#Filter through the dataset and save individual parts as GIS files (shapefiles)
#grouped = data.groupby('TZID')
#        
#output_folder = '/Users/ep9k/Desktop/GeopythonData/'
#
##Create Results Folder using OS package
#result_folder = os.path.join(output_folder, 'EuropeanCountries')
#if not os.path.exists(result_folder):
#    os.makedirs(result_folder)
#    
##now save each individual item to its own separate shapefile
#for key, values in grouped:
#    # Format the filename (replace spaces with underscores)
#    output_name = f'{key}.shp'.replace('Europe/','')
##    print(f'Processing {key}')
#    output_path = os.path.join(result_folder, output_name)
#    values.to_file(output_path)
#    







