# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Names: 	Alexander Bockelman
#           Jose Carrillo
# 	 		Patrick Chai
# 	 		Jackson Sanders
# Section:		211
# Assignment:	lab 11a-1 
# Date:		7 11 2018
value_name = input('what is the name of the values file? ')
measurement_name = input('what is the name of the corresponding measurements file? ')

with open(value_name, 'w') as data_values:
    values = data_values
with open(measurement_name, 'w') as measurement_values:
    measurement = measurement_values
query = float(input('what is the query value? '))
max = -9**9
min = 9**9

for i in range(0,len(measurement)):
    if measurement[i]>max:
        max = measurement[i]
    if measurement[i] < min:
        min = measurement[i]


top = (query - values[0])*(measurement[len(measurement)-1]-measurement[0])
bottom = values[len(values)-1] - values[0]
y = top/bottom + measurement[0]
print(y)


