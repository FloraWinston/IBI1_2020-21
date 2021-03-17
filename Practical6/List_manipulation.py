# import libraries first
import matplotlib as plt
import numpy as np 

# import two provided lists 
gene_lengths = [9410,394141,4442,105338,19149,76779,126550,36296,842,15981]
exon_counts = [51,1142,42,216,25,650,32533,57,1,523]
# calculate average exon length for every gene
# create a new empty list to store the value of average exon length
average_exon_length = []
# then use for-loop to repeate the division
for i in range(len(gene_lengths)):
    # do the division
    a = gene_lengths[i]/exon_counts[i]
    # add a to the list used for storage
    average_exon_length.append(a)
# print out the sorted list and do not change the previous list
print(sorted(average_exon_length))

# draw a boxplot
# These codes are adapted from the lecture PowerPoint, thanks for providing these useful examples.
# And I also look for online sources to make further adaptation. 

# import the library for pie chart
# Note: only import matplotlib is nut enough for making boxplot
import matplotlib.pyplot as plt 
# modity the boxplot
# Note1 vert is used to place the boxplot vertically.
# Note2 whis is used to determine whisker
# Note3 widths is used to decide the width of the boxplot
# Note4 meanline and showmeans is used to adjust the existance of mean value.
# Note5 patch_artist is used to adjuat the appearance of boxplot (also cooperate with last five functions
# Note6 labels indicates the label on the boxplot. 
plt.boxplot(average_exon_length, vert = True, whis = 1.5, widths = 0.3, patch_artist = True, meanline = True, showmeans = True, 
           labels = ['The average of exon length'], boxprops = {'facecolor' : 'lightblue', 'color' : 'grey'}, 
           flierprops = {'marker':'o'}, capprops = {'color':'grey', 'markersize':4},
           meanprops = {'markerfacecolor':'green','markersize':4},
		   medianprops = {'linestyle':'-','color':'orange'})
# To show user the boxplot
plt.show()
