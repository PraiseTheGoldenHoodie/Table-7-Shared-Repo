# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Names: 	Alexander Bockelman
#           Jose Carrillo
# 	 		Patrick Chai
# 	 		Jackson Sanders
# Section:		211
# Assignment:	8a-2
# Date:		27 10 2018

#User input phase
data_already_ordered = False
points = []
while True:
    user_in = input("build-model> Enter another point [or 'done'] (format: x y): ")
    if user_in == 'done':
        break
    user_in = user_in.split()
    if len(user_in) != 2:
        print("Enter exactly two values!")
        continue
    point = (float(user_in[0]), float(user_in[1]))
    if not data_already_ordered:
        for ins_ind in range(len(points), 0, -1):
            if points[ins_ind-1][0] <= point[0]:  #if two have same x, insert new after old to maintain order entered
                points.insert(ins_ind, point)
                break
        else:
            points.insert(0, point)
        print(points)
    else:
        points.append(point)

print(points)

# Interpolation phase
while True:
    user_in = input("apply-model> Enter x [or 'done'] (format: x): ")
    if user_in == 'quit':
        break
    user_in = float(user_in)
    #TODO