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
outputlines = []
# Reads in the file
with open(input_path, 'r') as fileName:
    english_lines = fileName.readlines()

# Converting to pig-latin
for line in english_lines:
    #print(line.split())
    next_out_line = ""
    for word in line.split():
        first_letter = word[0:1]                                                                                            # Assigns the first character from the word string to variable
        is_vowel = False                                                                                                        # Pretty much a boolean trigger to let you know it's not a vowel
        for i in vowels :
            if first_letter == i :                                                                                          # If the first letter is a vowel
                next_out_line += word+'yay '
                is_vowel = True                                                                                             # Redefines the boolean and stops the program
                break

        if not is_vowel :                                                                                                # Starts with consonant
            next_out_line += word[1:]+first_letter+"ay "
    outputlines.append(next_out_line +"\n")

# output the file
with open(output_path, 'w') as fileName:
    fileName.writelines(outputlines)
