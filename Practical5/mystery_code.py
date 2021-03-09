# What does this piece of code do?
# Answer: This script is used to choose an integer whose value is more than 0 but less than 50.

# Import libraries
# randint allows drawing a random number, 
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

# define Boolean variable p for the condition of while-loop
p=False
while p==False:
	# change the value of p and define n, the number we want
	p = True
	n = randint(1,100)
	# use if statement th test whether the value of n is what we want
	# If not, then continue the while-loop, until the proper value comes out.
	if n > 50:
		p = False
# Finally, print out n.
print(n)