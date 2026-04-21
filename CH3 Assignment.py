#Your assignment for chapter 3 is to complete a Roulette Wheel Color program. I have created a template for the program and placed a total of 4 TODO notes in the program for you to fill in. For each TODO note, read the instructions and 
#insert the statement(s) needed to complete the program. For reference, here is the full Roulette Wheel Color program description:
#On a roulette wheel, the pockets are numbered from 0 to 36. The colors of the pockets are as follows:
#Pocket 0 is green
#For pockets 1 through 10, the odd-numbered pockets are red and the even-numbered pockets are black
#For pockets 11 through 18, the odd-numbered pockets are black and the even-numbered pockets are red
#For pockets 19 through 28, the odd-numbered pockets are red and the even-numbered pockets are black
#For pockets 29 through 36, the odd-numbered pockets are black and the even-numbered pockets are red
#Write a program that asks the user to enter a pocket number and displays whether the pocket is green, red or black. The program should display an error message if the user enters a number 
#that is outside the range of 0 through 36.
#02/07/2026

#input statement that asks the user to input a number between 0 and 36 and store the input as an integer in a variable named pocketNum
pocketNum = int(input("Enter a number between 0 and 36: "))
#if statement that shows an error message if the number is less than 0 or more than 36
if pocketNum < 0  or pocketNum > 36:
    print("You entered an invalid pocket number, please run the program again to enter a valid number.")
#else statement that will determine the colors 
else:
    #if pocketNum is 0, pocketNum is green
    if pocketNum == 0:
        print("Pocket is green.")
    elif pocketNum >= 1 and pocketNum <= 10:
        if pocketNum % 2 == 0:  # if true, it is an even pocket number
            print("Pocket is black")
        else:
            print("Pocket is red")
    elif pocketNum >= 11 and pocketNum <= 18:
        if pocketNum % 2 == 0:  # if true, it is an even pocket number
            print("Pocket is red")
        else:
            print("Pocket is black")
    elif pocketNum >= 19 and pocketNum <= 28:
        if pocketNum % 2 == 0: # if true, it is an even pocket number
            print("Pocket is black")
        else:
            print("Pocket is red")
    elif pocketNum >= 29 and pocketNum <= 36:
        if pocketNum % 2 == 0:  # if true, it is an even pocket number
            print("Pocket is red")
        else:
            print("Pocket is black")
