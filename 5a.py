points = 0
###############
# User Inputs #
###############
sex = input("what is your gender? (M/F) ").upper()
if sex != "M" and sex != "F":
    sex = input("not a valid gender, please enter again (M/F) ").upper()
    if sex != "M" and sex != "F":
        print("still not valid, assuming gender as male")  # you suck
        sex = "M"

age = float(input("what is your age? "))
# since we can't use try-except yet, entering non-float will crash program. This goes for all float inputs too.

smoke = input("do you smoke? (y/n) ").upper()
if smoke == "Y":
    smoke = True
elif smoke == "N":
    smoke = False
else:
    print("invalid response, assuming you don't smoke")  # when you ASSUME, you make an ASS of U and ME
    smoke = False

HDL = float(input("what is your HDL? "))

sys_BP = float(input("what is your systolic BP? "))

######################
# Point calculations #
######################
if sex == "M":
    if age < 35:
        points -= 9
        # cholesterol
        tot_chol = input("what is your total cholesterol? ")
        tot_chol = float(tot_chol)
        if tot_chol < 160:
            points += 0
        elif tot_chol < 200:
            points += 4
        elif tot_chol < 240:
            points += 7
        elif tot_chol < 280:
            points += 9
        else:
            points += 11
        # cholesterol

    elif age < 40:
        points -= 4
        # cholesterol
        tot_chol = input("what is your total cholesterol? ")
        tot_chol = float(tot_chol)
        if tot_chol < 160:
            points += 0
        elif tot_chol < 200:
            points += 4
        elif tot_chol < 240:
            points += 7
        elif tot_chol < 280:
            points += 9
        else:
            points += 11
        # cholesterol

    elif age < 45:
        points += 0  # Is this line necessary?
        # cholesterol
        tot_chol = input("what is your total cholesterol? ")
        tot_chol = float(tot_chol)
        if tot_chol < 160:
            points += 0
        elif tot_chol < 200:
            points += 3
        elif tot_chol < 240:
            points += 5
        elif tot_chol < 280:
            points += 6
        else:
            points += 8
        # cholesterol

    elif age < 50:
        points += 3
        # cholesterol
        tot_chol = input("what is your total cholesterol? ")
        tot_chol = float(tot_chol)
        if tot_chol < 160:
            points += 0
        elif tot_chol < 200:
            points += 3
        elif tot_chol < 240:
            points += 5
        elif tot_chol < 280:
            points += 6
        else:
            points += 8
        # cholesterol

    elif age < 55:
        points += 6
        # cholesterol
        tot_chol = input("what is your total cholesterol? ")
        tot_chol = float(tot_chol)
        if tot_chol < 160:
            points += 0
        elif tot_chol < 200:
            points += 2
        elif tot_chol < 240:
            points += 3
        elif tot_chol < 280:
            points += 4
        else:
            points += 5
        # cholesterol

    elif age < 60:
        points += 8
        # cholesterol
        tot_chol = input("what is your total cholesterol? ")
        tot_chol = float(tot_chol)
        if tot_chol < 160:
            points += 0
        elif tot_chol < 200:
            points += 2
        elif tot_chol < 240:
            points += 3
        elif tot_chol < 280:
            points += 4
        else:
            points += 5
        # cholesterol

    elif age < 65:
        points += 10
        # cholesterol
        tot_chol = input("what is your total cholesterol? ")
        tot_chol = float(tot_chol)
        if tot_chol < 160:
            points += 0
        elif tot_chol < 200:
            points += 1
        elif tot_chol < 240:
            points += 1
        elif tot_chol < 280:
            points += 2
        else:
            points += 3
        # cholesterol

    elif age < 70:
        points += 11
        # cholesterol
        tot_chol = input("what is your total cholesterol? ")
        tot_chol = float(tot_chol)
        if tot_chol < 160:
            points += 0
        elif tot_chol < 200:
            points += 1
        elif tot_chol < 240:
            points += 1
        elif tot_chol < 280:
            points += 2
        else:
            points += 3
        # cholesterol

    elif age < 75:
        points += 12
        # cholesterol
        tot_chol = input("what is your total cholesterol? ")
        tot_chol = float(tot_chol)
        if tot_chol < 160:
            points += 0
        elif tot_chol < 200:
            points += 0
        elif tot_chol < 240:
            points += 0
        elif tot_chol < 280:
            points += 1
        else:
            points += 1
        # cholesterol

    else:
        points += 13
        # cholesterol
        tot_chol = input("what is your total cholesterol? ")
        tot_chol = float(tot_chol)
        if tot_chol < 160:
            points += 0
        elif tot_chol < 200:
            points += 0
        elif tot_chol < 240:
            points += 0
        elif tot_chol < 280:
            points += 1
        else:
            points += 1
        # cholesterol
# TODO: everything else besides cholesterol
# TODO: females






