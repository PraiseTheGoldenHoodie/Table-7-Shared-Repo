# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names: 	Alexander Bockelman
#           Jose Carrillo
# 	 		Patrick Chai
# 	 		Jackson Sanders
# Section:		211
# Assignment:	4a-1-[x]
# Date:		19 9 2018

from math import *
# Examples at beginning and what they yield
# a = 1/7
# print(a)
# b = a*7
# print(b)  # = 1.0
# c = 2*a
# d = 5*a
# e = c+d
# print(e)  # = 0.99999...
# x = sqrt(1/3)
# print(x)
# print(x*x*3)  # = 1.0
# print(x*3*x)  # = 0.99999...
tol = 0.001
a = tan(pi/4)
b = 1
x = .9
y= 1
print("is {} the same as {}? {}".format(a, b, abs(a-b) <= tol))
print("is {} the same as {}? {}".format(x, y, abs(x-y) <= tol))


