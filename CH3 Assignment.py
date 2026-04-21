#Paola Ramos Mendes
#CH3 Assignment

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