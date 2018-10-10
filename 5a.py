# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do"
# "I have not given or received any unauthorized aid on this assignment"
#
# Name: Alexander Bockelman
#       Jackson Sanders
#       Patrick Chai
#       Jose Carrillo
# Section: 211
# Assignment: Lab 5a- Activity 2
# Date: 28 September 2018

points = 0
gender = input("what is your gender? (M/F)").upper()
if gender!="M" and gender!="F":
    gender = input("not a valid gender, please enter again (M/F) ").upper()
    if gender != "M" and gender != "F":
        print("Error. Enter a correct Gender (M/F)")

age = input("what is your age? ")
age = float(age)

smoke = input("do you smoke? (y/n) ").upper()
if smoke !="Y" and smoke !="N":
    print("not valid, you don't smoke")
    smoke = False
elif smoke=="Y":
    smoke = True
else:
    smoke = False

HDL = input("what is your HDL? ")
HDL = float(HDL)

sys_BP = input("what is your systolic BP? ")
sys_BP = float(sys_BP)

sys_treat = input("has your systolic BP been treated? (y/n) ").upper()
if sys_treat != "Y" and sys_treat != "N":
    print("not valid, we will assume untreated")
    sys_treat = False
elif sys_treat == "N":
    sys_treat = False
else:
    sys_treat = True

tot_chol = input("what is your total cholesterol? ")
tot_chol = float(tot_chol)

#=================================================================================================
#=================================================================================================
#========================================= MEN =================================================
#=================================================================================================
#=================================================================================================

if gender=="M":

    # HDL
    if HDL < 40:
        points += 2
    elif HDL < 50:
        points += 1
    elif HDL < 60:
        points += 0
    else:
        points -= 1
    # HDL

    #systolic BP
    if sys_treat == True:
        if sys_BP<120:
            points+=0
        elif sys_BP <130:
            points+=1
        elif sys_BP<140:
            points+=2
        elif sys_BP<160:
            points+=2
        else:
            points+=3
    elif sys_treat == False:
        if sys_BP<120:
            points+=0
        elif sys_BP <130:
            points+=0
        elif sys_BP<140:
            points+=1
        elif sys_BP<160:
            points+=1
        else:
            points+=2
        #systolic BP end

    if age<35:
        points-=9
        # cholesterol
        if tot_chol<160:
            points+=0
        elif tot_chol<200:
            points+=4
        elif tot_chol<240:
            points+=7
        elif tot_chol<280:
            points+=9
        else:
            points+=11
        #cholesterol

        if smoke:
            points += 8

    elif age<40:
        points-=4
        # cholesterol
        if tot_chol<160:
            points+=0
        elif tot_chol<200:
            points+=4
        elif tot_chol<240:
            points+=7
        elif tot_chol<280:
            points+=9
        else:
            points+=11
        # cholesterol

            if smoke:
                points += 8


    elif age<45:
        points+=0
        # cholesterol
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

            if smoke:
                points += 5

    elif age<50:
        points+=3
        # cholesterol
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

            if smoke:
                points += 5

    elif age<55:
        points+=6
        # cholesterol
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

            if smoke:
                points += 3


    elif age<60:
        points+=8
        # cholesterol
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

            if smoke:
                points += 3


    elif age<65:
        points+=10
        # cholesterol
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

            if smoke:
                points += 1


    elif age<70:
        points+=11
        # cholesterol
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

            if smoke:
                points += 1


    elif age<75:
        points+=12
        # cholesterol
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

            if smoke:
                points += 1


    else:
        points+=13
        # cholesterol
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

            if smoke:
                points += 1

        # point calculation
    if points < 0:
         print("your ten year risk is less than 1%")
    elif points < 4:
        print("your ten year risk is 1%")
    elif points < 7:
        print("your ten year risk is 2%")
    elif points < 8:
        print("your ten year risk is 3%")
    elif points < 9:
        print("your ten year risk is 4%")
    elif points < 10:
        print("your ten year risk is 5%")
    elif points < 11:
        print("your ten year risk is 6%")
    elif points < 12:
        print("your ten year risk is 8%")
    elif points < 13:
        print("your ten year risk is 10%")
    elif points < 14:
        print("your ten year risk is 12%")
    elif points < 15:
        print("your ten year risk is 16%")
    elif points < 16:
        print("your ten year risk is 20%")
    elif points < 17:
        print("your ten year risk is 25%")
    elif points >= 17:
        print("your ten year risk is greater than 30%")


#=================================================================================================
#=================================================================================================
#========================================= WOMEN =================================================
#=================================================================================================
#=================================================================================================
if gender == "F":

    # HDL
    if HDL < 40:
        points += 2
    elif HDL < 50:
        points += 1
    elif HDL < 60:
        points += 0
    else:
        points -= 1
    # HDL

    # systolic BP
    if sys_treat == True:
        if sys_BP < 120:
            points += 0
        elif sys_BP < 130:
            points += 3
        elif sys_BP < 140:
            points += 4
        elif sys_BP < 160:
            points += 5
        else:
            points += 6
    elif sys_treat == False:
        if sys_BP < 120:
            points += 0
        elif sys_BP < 130:
            points += 1
        elif sys_BP < 140:
            points += 2
        elif sys_BP < 160:
            points += 3
        else:
            points += 4
        # systolic BP end


    if age < 35:
        points -= 7
        # cholesterol
        if tot_chol < 160:
            points += 0
        elif tot_chol < 200:
            points += 4
        elif tot_chol < 240:
            points += 8
        elif tot_chol < 280:
            points += 11
        else:
            points += 13
        # cholesterol

        if smoke:
            points += 9

    elif age < 40:
        points -= 3
        # cholesterol
        if tot_chol < 160:
            points += 0
        elif tot_chol < 200:
            points += 4
        elif tot_chol < 240:
            points += 8
        elif tot_chol < 280:
            points += 11
        else:
            points += 13
            # cholesterol

            if smoke:
                points += 9


    elif age < 45:
        points += 0
        # cholesterol
        if tot_chol < 160:
            points += 0
        elif tot_chol < 200:
            points += 3
        elif tot_chol < 240:
            points += 6
        elif tot_chol < 280:
            points += 8
        else:
            points += 10
            # cholesterol

            if smoke:
                points += 7

    elif age < 50:
        points += 3
        # cholesterol
        if tot_chol < 160:
            points += 0
        elif tot_chol < 200:
            points += 3
        elif tot_chol < 240:
            points += 6
        elif tot_chol < 280:
            points += 8
        else:
            points += 10
            # cholesterol

            if smoke:
                points += 7

    elif age < 55:
        points += 6
        # cholesterol
        if tot_chol < 160:
            points += 0
        elif tot_chol < 200:
            points += 2
        elif tot_chol < 240:
            points += 4
        elif tot_chol < 280:
            points += 5
        else:
            points += 7
            # cholesterol

            if smoke:
                points += 4


    elif age < 60:
        points += 8
        # cholesterol
        if tot_chol < 160:
            points += 0
        elif tot_chol < 200:
            points += 2
        elif tot_chol < 240:
            points += 4
        elif tot_chol < 280:
            points += 5
        else:
            points += 7
            # cholesterol

            if smoke:
                points += 4


    elif age < 65:
        points += 10
        # cholesterol
        if tot_chol < 160:
            points += 0
        elif tot_chol < 200:
            points += 1
        elif tot_chol < 240:
            points += 2
        elif tot_chol < 280:
            points += 3
        else:
            points += 4
            # cholesterol

            # smoking
            if smoke is False:
                points += 0
            else:
                points += 2
            # smoking


    elif age < 70:
        points += 12
        # cholesterol
        if tot_chol < 160:
            points += 0
        elif tot_chol < 200:
            points += 1
        elif tot_chol < 240:
            points += 2
        elif tot_chol < 280:
            points += 3
        else:
            points += 4
            # cholesterol

            # smoking
            if smoke is False:
                points += 0
            else:
                points += 2
            # smoking


    elif age < 75:
        points += 14
        # cholesterol
        if tot_chol < 160:
            points += 0
        elif tot_chol < 200:
            points += 1
        elif tot_chol < 240:
            points += 1
        elif tot_chol < 280:
            points += 2
        else:
            points += 2
            # cholesterol

            # smoking
            if smoke is False:
                points += 0
            else:
                points += 1
            # smoking


    else:
        points += 16
        # cholesterol
        if tot_chol < 160:
            points += 0
        elif tot_chol < 200:
            points += 1
        elif tot_chol < 240:
            points += 1
        elif tot_chol < 280:
            points += 2
        else:
            points += 2
            # cholesterol

            # smoking
            if smoke is False:
                points += 0
            else:
                points += 1
            # smoking

    #point calculation
    if points < 9:
        print("your ten year risk is less than 1%")
    elif points < 13:
        print("your ten year risk is 1%")
    elif points < 15:
        print("your ten year risk is 2%")
    elif points < 16:
        print("your ten year risk is 3%")
    elif points < 17:
        print("your ten year risk is 4%")
    elif points < 18:
        print("your ten year risk is 5%")
    elif points < 19:
        print("your ten year risk is 6%")
    elif points < 20:
        print("your ten year risk is 8%")
    elif points < 21:
        print("your ten year risk is 11%")
    elif points < 22:
        print("your ten year risk is 14%")
    elif points < 23:
        print("your ten year risk is 17%")
    elif points < 24:
        print("your ten year risk is 22%")
    elif points < 25:
        print("your ten year risk is 27%")
    elif points >= 25:
        print("your ten year risk is greater than 30%")