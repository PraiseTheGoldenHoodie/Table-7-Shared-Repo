points = 0
gender = input("what is your gender? (M/F)").upper()
if gender!="M" and gender!="F":
    gender = input("not a valid gender, please enter again (M/F) ").upper()
    if gender != "M" and gender != "F":
        print("you suck")

age = input("what is your age? ")
age = float(age)

smoke = input("do you smoke? (y/n) ").upper()
if smoke !="Y" or smoke !="N":
        print("not valid, you don't smoke")
        smoke = False

HDL = input("what is your HDL? ")
HDL = float(HDL)

sys_BP = input("what is your systolic BP? ")
sys_BP = float(sys_BP)

if gender=="M":

    if age<35:
        points-=9
        # cholesterol
        tot_chol = input("what is your total cholesterol? ")
        tot_chol = float(tot_chol)
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

    elif age<40:
        points-=4
        # cholesterol
        tot_chol = input("what is your total cholesterol? ")
        tot_chol = float(tot_chol)
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


    elif age<45:
        points+=0
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

    elif age<50:
        points+=3
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


    elif age<55:
        points+=6
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


    elif age<60:
        points+=8
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


    elif age<65:
        points+=10
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


    elif age<70:
        points+=11
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


    elif age<75:
        points+=12
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
        points+=13
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







