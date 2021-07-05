# Data cleaning project - NYC Trees

## Description :
The task of this assignement is to clean the dataset "2015 Street Tree Census: Tree Data"
(source: https://data.cityofnewyork.us/Environment/2015-Street-Tree-Census-Tree-Data/uvpi-gqnh). By cleaning they mean:
- The dataset contains no missing values (" " or null)
- No duplicates.
- Values are consolidated
- Data format is correct
- No blank spaces

## Installation:
Just run nyc-trees.py

## Usage 
To clean the dataset "2015 Street Tree Census: Tree Data" (input dataset:  data_100000.csv size (100000x42), output: data_trees_100000_clean.csv size (100000x22))

##(Visuals)

## Contributors:
Solo project.

## Timeline:
In order to perform a good cleaning, we need to know what the dataset is about and what kind of information is in it. 

![dataset](table.png)

To know my data, I used a smallest dataset (only 10000 rows) to save running time.
I take a quick look to the dataset to now the size and some basic characteristics as columns name, data type, etc...

![info](dataset_info.png)

A description about each column is provided in the document *StreetTreeCensus2015TreesDataDictionary20161102.pdf* so the first step is to read the document in order
to decide which columns can be dropped and the type of data or content we should find on each column.

Considering this, after the first reading, I decided to drop ([column index in the dataset] column name):
* [1] tree_id 
According to the document "It specifically identifies data entered by a specific user on a specific survey, not the tree itself"

* [3] the_geom
It seems just a combination of latitude and longitude in one column.

* [11] steward
"Indicates the number of unique signs of stewardship observed for this tree. Not recorded for stumps or dead trees." This column doesn't seem relevant to me.

* [15] problems
This is like the sum of columns 16, 17, 18, putting all the problems a tree might have together. Thus redundant information.

* [30] boroname
"Name of borough in which tree point is located" column 29 has the code for the borough so I keep only 29.

* [31] cncldist

* [32] st_assem

* [33] st_senate
These three columns have information the district and other details that can be obtained using for instance columns 29.

* [37] state
The entire columns has the same value 'New York' so it can be deleted, and in the dataset specification I will add that is data only from New York.

For the rest, more tests are needed.

Other steps to do:

-For sure I will keep latitude and longitude. And every time I have a reference to a place with a name and a code (in different columns), I will keep only the column with the code. It is easier to make mistakes written a name than typing a number.

-Decapitalize all the text

After further study, I'll keep the columns related with the location. Normally with latitude and longitude I can derive all the other ones. The survey is about the trees so we must keep all the columns with relevant info abour the trees and their health...always avoiding duplicates or redundant information. The index of columns to be kept:
- 0, 4, 5, 6, 7, 8, 9, 10, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 29, 34, 38 and 39; Thus from 42 columns we keep only 22.

After that decision, enumerated bellow are the steps to follow to clean the dataset.

###### Cleaning steps: 

- Drop the unwanted colums (20).
- Check for duplicates.
- Change date column from object to date.
- Decapitalize all the strings
- Change 'yes' and 'no' from multiple columns to boolean True/False.
- Replace empty spaces par nan, for numerical columns, and None for object ones.
- Check for remaining issues.
- Print the final cleaned dataset to a csv file.


###### Final remark:

At the end, I still have ~5% null values in three columns: 'health', 'spc_latin', 'spc_common'. 
Because we don't know the final use of the dataset, I consider 5% of data as not negligable so I decided to keep it.
