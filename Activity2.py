# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do"
# "I have not given or received any unauthorized aid on this assignment"
#
# Name: Alexander Bockelman
#       Jackson Sanders
#       Patrick Chai
#       Jose Carrillo
#       Wayne Ussery
# Section: 211
# Assignment: Lab 3a-Activity 2
# Date: 12 September 2018
print("The following program formats four people’s birthdays. Enter the following information for each person:")
print("-------------------------------------------------------------------------------------------------------")
print("Person 1:")
print("---------")
full_name_1 = input("Name = ")
birth_year_1 = str(int(input("Year of Birth = ")))
birth_month_1 = str(int(input("Month of Birth = ")))
birth_day_1 = str(int(input("Day of Birth = ")))
print("---------")
print("Person 2:")
print("---------")
full_name_2 = input("Name = ")
birth_year_2 = str(int(input("Year of Birth = ")))
birth_month_2 = str(int(input("Month of Birth = ")))
birth_day_2 = str(int(input("Day of Birth = ")))
print("---------")
print("Person 3:")
print("---------")
full_name_3 = input("Name = ")
birth_year_3 = str(int(input("Year of Birth = ")))
birth_month_3 = str(int(input("Month of Birth = ")))
birth_day_3 = str(int(input("Day of Birth = ")))
print("---------")
print("Person 4:")
print("---------")
full_name_4 = input("Name = ")
birth_year_4 = str(int(input("Year of Birth = ")))
birth_month_4 = str(int(input("Month of Birth = ")))
birth_day_4 = str(int(input("Day of Birth = ")))
space_l = 40
space_r = 20
print("Name".ljust(space_l) + "Date of Birth (D-M-Y)".rjust(space_r))
print("----".ljust(space_l) + "---------------------".rjust(space_r))
print(full_name_1.ljust(space_l) + (birth_day_1 + "-" + birth_month_1 + "-" + birth_year_1).rjust(space_r))
print(full_name_2.ljust(space_l) + (birth_day_2 + "-" + birth_month_2 + "-" + birth_year_2).rjust(space_r))
print(full_name_3.ljust(space_l) + (birth_day_3 + "-" + birth_month_3 + "-" + birth_year_3).rjust(space_r))
print(full_name_4.ljust(space_l) + (birth_day_4 + "-" + birth_month_4 + "-" + birth_year_4).rjust(space_r))