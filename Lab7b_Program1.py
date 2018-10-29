# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Jackson Sanders
# Section:		211
# Assignment:	Lab 7b
# Date:		    10 13 2018

# Design a program that will intake values and analyze the average, max and min.
# Make it to where entering a negative value discontinues the loop

file = open(r"igpay.txt")
file.readline()

word = str(input("Please enter the word you would like to be translated; enter stop to stop the program. "))
vowels = ['a', 'e', 'i', 'o', 'u', 'y']                                                                                 # Assigns values
is_vowel = False                                                                                                        # Pretty much a boolean trigger to let you know it's not a vowel


while word != "stop" :                                                                                                  # 'Stop' stops the program
    first_letter = word[0:1]                                                                                            # Assigns the first character from the word string to variable
    for i in vowels :
        if first_letter == i :                                                                                          # If the first letter is a vowel
            print(word+'yay')
            is_vowel = True                                                                                             # Redefines the boolean and stops the program
            break

    while not is_vowel :                                                                                                # Starts with consonant
        print(word[1:]+first_letter+"ay")
        break
    word = str(input("Please enter the word you would like to be translated; enter stop to stop the program. "))        # Runs infinite loop if this line isn't included
