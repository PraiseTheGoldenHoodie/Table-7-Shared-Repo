# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Patrick Chai
# Section:		211
# Assignment:	Lab 3
# Date:	    9/12/2018
from math import*
import numpy
btu = input("how many btu would you like to convert to joules? ")
btu = int(btu)
joules = btu*1055.06
joules = str(joules)
btu = str(btu)
print(btu+" btu will convert to "+joules+" joules")