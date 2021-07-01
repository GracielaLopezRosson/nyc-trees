# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 12:33:55 2021

@author: graci
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

trees = pd.read_csv("data_10000.csv")#

trees.info()# The most important info to know how the initial file looks like.

#houses.head() #To see the head info of my table, so the parameters or names of each column.

#houses['price'] = houses['Price [€]']#.str.replace('no', 'NaN').astype(float)
#houses['area'] = houses['Area [m²]'].astype(float)

#houses1 = houses[houses['Price [€]']!= 'no'] #to drop the 'no' of the price column. Now I have 10058 entries (I lost 34)

#immo = houses1.rename(columns = { 'Unnamed: 0':'ID',
#                            'Area [m²]': 'area',
#                            'Price [€]':'price',
#                            'state of the building':'building_status', 
#                            'number of facades':'number_facades', 'number of bedrooms':'number_bedrooms',
#                             'fully equipped kitchen':'kitchen_equipped',
#                             'open fire':'open_fire',
#                             'locality [zip code]':'zip_code',
#                             'surface of the land [m²]':'land_surfaces',
#                             'terrace surface [m²]':'terrace_surface',
#                             'swimming pool':'swimming_pool',
#                             'type of property':'property_type',
#                             'subtype of property':'subtype_property',
#                             'garden surface [m²]': 'garden_surface'}, inplace = False)
#
#immo['price'] = immo['price'].astype(float)#str.replace('no', 'NaN').
#immo.price.describe() #statistics
#
#"""
#Checking the data
#"""
#immo['area'].isna().sum()
## = 1725
#immo['price'].isna().sum()
#
#new_immo = immo[immo.area > 0] #####This is the one to work with!!!!
#
#new_immo.to_csv('immo_eliza_dataset.csv')
#
###immo['price'].isna().any() #True

#




#area = houses["Area"] #To have my data as separated columns:
#surface_land = houses["surface of the land"]
#number_of_bedrooms = houses["number of bedrooms"]
#
#print(houses["Area"].shape) #to check the length of my new column, if it's the same than my DataFrame
#print(houses["surface of the land"].shape)
#
#"""
#Filtering the 'good data':
#There are two ways to filter the data:
#    
#1. Using the area as parameter: the area should be bigger than 0 in order to sell the property.
#With that, we eliminate all the 'projects' where the surface/area of each property is not well defined yet.
#Doing this, we lost ~2000 properties.
#
#2. Using the surface of the land. It is strange, but sometimes you get the surface of the land and no the
#are. With this method, we lost only ~1000
#
#This new data set is our starting point.
#"""
##valid_houses = houses[houses["Area"] > 0] #For method 1
#valid_houses = houses[houses["surface of the land"] > 0] #For method 2
#
#
#
## To improve the name of the columns:
#final_list_houses = valid_houses.rename(columns={'Area': 'Area [m²]', 'Price': 'Price [€]', 'locality': 'locality [zip code]',
#                                                 'surface of the land': 'surface of the land [m²]', 'terrace surface': 'terrace surface [m²]',
#                                                 'garden surface': 'garden surface [m²]'})
#
#
#
#final_list_houses.to_csv('final_list_houses_dataset.csv') #My final deliverable CSV table 
