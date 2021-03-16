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
# print out the sorted list anddo not change the previous list
print(sorted(average_exon_length))

# draw a boxplot
# These codes are adapted from the lecture PowerPoint, thanks for providing these useful examples.
# import the library for pie chart
# Note: only import matplotlib is nut enough for making boxplot
import matplotlib.pyplot as py
# modity the boxplot
py.boxplot(average_exon_length, vert = True, whis = 1.5, widths = 1.5, meanline = True, showmeans = True, 
           labels =['The average of exon length'],)
# To show user the boxplot
py.show()




