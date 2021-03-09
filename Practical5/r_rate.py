# The script about the rate of reproduction of virus

# define r rate and the number of individuals in the poplulation 
r = 1.1; n = 84

# define a varibale x that have the same value as n for the use of for-loop
x = 84
# define a for-loop for repeating 5 times
for i in range(1,6):
    # define a as the number of individuals infected
	a = r * x
	# reset the value of x for further loop
	x = a

# use if statement to test whether the number of individuals infected is higher than n
if a > n :
	a = n

# Then generate the output
print(f'Since the r rate is {str(r)}, the total number of individuals infected after 5 generations is {str(a)}.')
