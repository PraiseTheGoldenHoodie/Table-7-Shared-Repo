# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Names: 	Alexander Bockelman
#           Jose Carrillo
# 	 		Patrick Chai
# 	 		Jackson Sanders
#           Wayne Ussery
# Section:		211
# Assignment:	Lab2a-3
# Date:		03 09 2018
import numpy
from math import*
init_time = 30
init_position = 50
final_time = 45
final_position = 615

interpol_time = 37

change_in_time = final_time - init_time
fraction_completed = (interpol_time - init_time) / change_in_time
interpol_position = (final_position - init_position) * fraction_completed + init_position
interpol_position=round(interpol_position,3)
interpol_position = str(interpol_position)
print("the distance at 37 seconds is "+interpol_position+" meters")
print(

"optional activity:"
)

change_time=1170
#1170 is from 1200-30 seconds because we started at thirty seconds
# optional time/distance is part of the optional lab
velocity=(final_position-init_position)/(final_time-init_time)

total_distance=velocity*change_time+50
#the plus 50 is because we started at 50 meters
total_distance=total_distance%(pi*1000)

total_distance=round(total_distance,3)
total_distance = str(total_distance)
print("the distance at 20 minutes is "+total_distance+" meters")



