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

vowels = ['a', 'e', 'i', 'o', 'u', 'y']                                                                                 # Assigns values
with open(input_path, 'r') as fileName:
    english_lines = fileName.readlines()
for line in english_lines:
    #print(line.split())
    for word in line.split():
        first_letter = word[0:1]                                                                                            # Assigns the first character from the word string to variable
        is_vowel = False                                                                                                        # Pretty much a boolean trigger to let you know it's not a vowel
        for i in vowels :
            if first_letter == i :                                                                                          # If the first letter is a vowel
                print(word+'yay', end=' ')
                is_vowel = True                                                                                             # Redefines the boolean and stops the program
                break

        while not is_vowel :                                                                                                # Starts with consonant
            print(word[1:]+first_letter+"ay", end=' ')
            break
    print()

