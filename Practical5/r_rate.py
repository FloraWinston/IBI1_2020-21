# The script about the rate of reproduction of virus

# define r rate and the number of IBI1 stduents n  
r = 1.1; n = 84
# define a for-loop for repeating 5 times
for i in range(1,6):
    # define a as the number of individuals infected
	a = r * n
	# reset the value of n for further loop
	n = a

# Then generate the output
print(f'Since the r rate is {str(r)}, the total number of individuals infected after 5 generations is {str(a)}.')
