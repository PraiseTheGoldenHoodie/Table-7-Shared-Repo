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
tol = 0.001
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
eq1 = "7/7"
eq2 = "2/7 + 5/7"
print("is {} the same as {}? {}".format(eq1, eq2, eval(eq1) == eval(eq2)))
eq1 = "7/7"
eq2 = "(1/7)*2 + (1/7)*5"
print("is {} the same as {}? {}".format(eq1, eq2, eval(eq1) == eval(eq2)))

