#About daye
a = 280402
b = 190784
c = 100321
d = abs(c-a)
e = abs(a-b)
print("d is", d)
print("e is", e)
print(d > e)
print("According to the result, d is greater.")

#About Booleans
#Round 1
X = True 
Y = False
Z = (X and not Y) or (Y and not X)
print(Z)
W = X != Y
print(W)
#Round 2
X = False
Y = True
Z = (X and not Y) or (Y and not X)
print(Z)
W = X != Y
print(W)