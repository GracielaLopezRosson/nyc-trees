# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 12:33:55 2021

@author: graci
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

trees = pd.read_csv("data_10000.csv")#

trees.info()
"""
1st dropping after checking the column description. I will drop:
['tree_id', 'the_geom', 'steward','problems',  'boroname', 'cncldist', 
'st_assem', 'st_senate', 'state']
"""
lista = ['tree_id','the_geom', 'steward']
#trees.drop(columns=['tree_id', 'the_geom', 'steward','problems',  'boroname', 'cncldist', 
#'st_assem', 'st_senate', 'state'], inplace=True)
test = trees.drop(columns=lista)

"""
Function to drop columns:
 'lista' is an array with the columns you want to delete from dataset df
"""
def columns_to_drop(df, lista):
    df1 = df.drop(columns=lista)
    return df1
    
#To decapitalize all the 'object type' columns
df2 = trees.apply(lambda x: x.str.upper() if x.dtype == "object" else x)


#
#final_list_houses.to_csv('final_list_houses_dataset.csv') #My final deliverable CSV table 
