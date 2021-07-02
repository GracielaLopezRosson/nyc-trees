# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 12:33:55 2021

@author: graci
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

trees = pd.read_csv("data_100000.csv")#

trees.info()

#1st dropping after checking the column description. I will drop:

cols_to_drop = ['tree_id', 'block_id','the_geom', 'steward',
            'guards', 'sidewalk', 'user_type', 'problems', 'address',
            'zip_city', 'cb_num',  'boroname', 'cncldist', 'st_assem',
       'st_senate',  'nta_name', 'boro_ct', 'state',  'x_sp', 'y_sp']
 

"""
Function to drop columns:
 'lista' is an array with the columns you want to delete from dataset df
"""
def columns_to_drop(df, lista):
    df1 = df.drop(columns=lista)
    return df1

trees_v1 = columns_to_drop(trees, cols_to_drop)

#Check for duplicates
trees_v1[trees_v1.duplicated()]

trees_v1['created_at'] = pd.to_datetime(trees_v1['created_at'])

#To decapitalize all the 'object type' columns
trees_v2 = trees_v1.apply(lambda x: x.str.lower() if x.dtype == "object" else x)

# Boolean insted 'yes'/'no'
cols_to_bool = ['root_stone','root_grate', 'root_other', 'trnk_wire', 'trnk_light', 'trnk_other',
       'brnch_ligh', 'brnch_shoe', 'brnch_othe']

for col in cols_to_bool:
    trees_v2[col] = trees_v2[col].map({'yes': True, 'no': False})

trees_v2['health'].replace('', np.NaN)
trees_v2['spc_latin'].replace('', np.NaN)
trees_v2['spc_common'].replace('', np.NaN)


trees_v2.to_csv('data_trees_100000_clean.csv') #My final deliverable CSV table 
