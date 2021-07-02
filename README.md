# nyc-trees

# Description :
The task of this assignement is to clean the dataset "2015 Street Tree Census: Tree Data"
(source: https://data.cityofnewyork.us/Environment/2015-Street-Tree-Census-Tree-Data/uvpi-gqnh). By cleaning they mean:
- The dataset contains no missing values ("" or null)
- No duplicates.
- Values are consolidated
- Data format is correct
- No blank spaces

# Installation:
Just run nyc-trees.py

# Usage 
To clean the dataset "2015 Street Tree Census: Tree Data" (input dataset:  data_100000.csv size (42x100000), output: data_trees_100000_clean.csv size ())

#(Visuals)

# Contributors:
Solo project.

# Timeline:
In order to perform a good cleaning, we need to know what the dataset is about and what kind of information is in it. 
I take a quick look to the dataset to now the size and some basic characteristics as columns name, data type, etc...

![info](dataset_info.png)
A description about each column is provided in the document StreetTreeCensus2015TreesDataDictionary20161102.pdf so the first step is to read the document in order
to decide which columns can be dropped and the type of data or content we should find on each column.

Considering this, after the first reading, I decided to drop:

