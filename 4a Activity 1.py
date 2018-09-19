from math import*

tol=10**-5
y = (sqrt(2)/2)/(sqrt(2)/2)
x = tan(pi/4)

print("is tan(pi/4) the same as (sqrt(2)/2)/(sqrt(2)/2)? ",(y) == (x))
print("is tan(pi/4) within tolerance of (sqrt(2)/2)/(sqrt(2)/2)? ", fabs(y - x)<=tol)