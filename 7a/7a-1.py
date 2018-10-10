# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do"
# "I have not given or received any unauthorized aid on this assignment"
#
# Name: Alexander Bockelman
#       Jackson Sanders
#       Patrick Chai
#       Jose Carrillo
#
# Section: 211
# Assignment: Lab 7a- Activity 1
# Date: October 10 2018

widgets  = []               
user_input = 0
index = 0                   # Starts counter for how many days we will take widget production measurements
days_increasing = 0         # Acts as counter which will be used when comparing indexes in order to determine inc/dec 
days_decreasing = 0
count = 0
while user_input >= 0:      
    user_input = input("Enter widgets: ")
    user_input = int(user_input)
    if user_input < 0:                              # Entering a negative value will stop the program
        print("Values accepted.")
        break                                       # Donezo
    widgets.append(user_input)                      # Adds on more values to the values in the widgets list

for interval_size in range(1, len(widgets)):  # interval size
    count = 0
    days_increasing = 0
    days_decreasing = 0
    for index in range(0, len(widgets)-interval_size):                
    # No need to check the the last few indexes within the list size
        if widgets[index+interval_size] > widgets[index]:
            days_increasing += 1                                        
        # add increasing intervals to increasing count
        elif widgets[index+interval_size] < widgets[index]:
            days_decreasing += 1
        # add decreasing intervals to decreasing count
        count += 1
        # percentages are derived from number of inc/dec intervals divided by count

    #print("for intervals of ",interval_size," size, ", days_increasing/count*100,"\n are increasing and ", days_decreasing/count*100,"\n are decreasing")
    print("For {}-day intervals {:.1%}% were increasing and {:.1%}% were decreasing".format(interval_size, days_increasing/count, days_decreasing/count))
    # % signs format the values so that they display the float value to two decimal places
    





