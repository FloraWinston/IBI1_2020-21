# import the library first 
import matplotlib as plt
import numpy as np 
import pandas as pd 

# deifne and print dictionary
number_of_cases = {'Country':'Total Cases','USA':29862124,'India':11285561,'Brazil':11205972,'Russia':4360823,'UK':4234924}
print(number_of_cases)

# Here is another way to print dictionary
# I adapted codes from https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.filter.html
# Create a dataframe then fill the value (indexs are not adapted, so it remains as numbers.) 
df = pd.DataFrame(np.array((['USA',29862124], ['India',11285561], ['Brazil',11205972], ['Russia',4360823], ['UK',4234924])),
                  # define the number of columns
                  columns=['Country','Total Cases'])
# print this dataframe
print(df)


# Use the data to make a piechart
# These codes are adapted from the lecture PowerPoint, thanks for providing these useful examples.
# And I also look for online sources to undestand their meanings.
 
# import the library for pie chart
# Note: only import matplotlib is nut enough for making piechart
import matplotlib.pyplot as plt
#This definition represents the label of different color parts of the pie chart. 
labels = 'USA','India','Brazil','Russia','UK'
# This definition represents the size of each part, indicated by numbers, and also useful for calculating the percentage.
sizes = [29862124,11285561,11205972,4360823,4234924]
# This definition indicates that how long certian parts is away from the main part of pie chart.
explode = (0,0,0,0,0)
# Combine all indexs together then make a pie chart. 
# Note1: shadow indicates the shadow part of the pie chart (if True, then pie chart will have a shadow).
# Note2: startangle indicates the direction of the pie chart (i.e., if values changed, then the pie chart will rotate.).
# Note3: autpct is used to calculated percentage, and also label them on the pie chart.
# Note4: colors is used to change the color of pie chart.
plt.pie(sizes,explode = explode, labels = labels, shadow = False, startangle = 90, autopct='%1.1F%%', colors = ['C9','C2','C1','C6','C4'])
# Make sure that x,y axis have the same scale
plt.axis('equal')
# To show user the pie chart
plt.show()

