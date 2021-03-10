# For Fibonacci sequence
# define the first two integers of the sequence
a = 1; b = 1
print(a); print(b)
# use a for-loop to do addition
# totally will add 11 times for values
for i in range(1,12):
    # define x as one number of sequence to do the addition
    x = a + b
    # redefine a, b when the loop is continuing
    # prepare for the next turn of loop
    b = a
    a = x
    # display the value
    print(x)

