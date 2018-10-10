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
# Assignment: Lab 7a- Activity 3
# Date: October 10 2018

board = [["R","N","B","Q","K","B","N","R"],
         ["P","P","P","P","P","P","P","P"],
         [".",".",".",".",".",".",'.','.'],
         [".",".",".",".",".",".",'.','.'],
         [".",".",".",".",".",".",'.','.'],
         [".",".",".",".",".",".",'.','.'],
         ['p','p','p','p','p','p','p','p'],
         ['r','n','b','q','k','b','n','r']]
while True:  # current_row<=8 and final_row<=8 and current_column<=8 and final_column<=8:
    # display board
    for row in board:
        for val in row:
            print(val, end= " ")  # prints letters next to each other
        print('')  # starts on next line
    # take input
    print("Enter positions zero-indexed, where top-left corner is (0,0)")
    current_row = int(input("what row are you moving from? "))
    current_column = int(input("what column are you moving from? "))
    final_row = int(input("what row are you moving to? "))
    final_column = int(input("what column are you moving to? "))
    index = 0
    # check move is valid / make move
    if board[current_row][current_column] == ".":
        print("invalid move")
        break
    if board[final_row][final_column] == ".":
        pass  # TODO
    else:
        if board[final_row][final_column].isupper() != board[current_row][current_column].isupper() and board[final_row][final_column] == ".":
            store_row = final_row
            store_column = final_column
            final_row = current_row
            final_column = current_column
            current_row = store_row
        
        elif board[final_row][final_column].isupper() != board[current_row][current_column].isupper() and board[final_row][final_column] != ".":
            board[final_row][final_column] = board[current_row][current_column]
            board[current_row][current_column] = '.'
            
        else:
            print("invalid move")
            break