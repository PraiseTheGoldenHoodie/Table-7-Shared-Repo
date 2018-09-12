# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Jackson Sanders
# Section:		211
# Assignment:	Lab 3a Activity 1
# Date:		    9 12 2018

# seconds per revolution to hertz (cycle per second)
# just invert it

seconds = input("How many seconds would you like to convert to Hertz?")
seconds = float(seconds)
hertz = seconds ** (-1)
hertz = str(hertz)
seconds = str(seconds)
print(""+seconds+" second(s) convert to "+hertz+" hertz")