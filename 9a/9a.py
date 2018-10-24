# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Names: 	Alexander Bockelman
#           Jose Carrillo
# 	 		Patrick Chai
# 	 		Jackson Sanders
# Section:		211
# Assignment:	9a
# Date:		24 10 2018

input_path = "input.txt"
output_path = "output.txt"

with open(input_path, 'r') as fileName:
    english_lines = fileName.readlines()
for line in english_lines:
    print(line.split())
