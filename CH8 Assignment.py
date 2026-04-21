#Your assignment for chapter 8 is to modify a provided password verification program to include additional requirements. In the provided starting program, 
#the user is prompted to enter a password and the password is considered valid if the length is at least 8 characters, contains a digit, and contains an uppercase character.
#Make the following changes:
#1) Add the following additional requirement for a valid password: it must contain at least one of these special characters: !, @, #, or $
#2) Edit the program in the appropriate place to use a loop so if the user enters an invalid password, the program will ask them to enter a new password until they have entered a valid password.
#04/18/2026

def hasUpperCase(pw):
    upperFound = False

    # Test each character in the password and see if we find an uppercase character. Set the flag to true if we find one
    for ch in pw:
        if ch.isupper() == True:
            upperFound = True

    return upperFound

def hasDigit(pw):
    digitFound = False

    # Test each character and see if we find a digit
    for ch in pw:
        if ch.isdigit() == True:
            digitFound = True

    return digitFound

#Created a function for special characters
def hasSpecialChar(pw):
    has_special = False
    characters = "!@#$"
    #Loop through each character in the password
    for ch in pw:
        #Check if the current character is one of the special characters
        if ch in characters:
            has_special = True
    return has_special
        
def isPasswordValid(pw):
    pwValid = True

    if len(pw) < 8:
        print("Your password must be at least 8 characters long")
        pwValid = False

    if hasUpperCase(pw) == False:
        print("Your password must contain at least one uppercase character")
        pwValid = False

    if hasDigit(pw) == False:
        print("Your password must contain at least one digit")
        pwValid = False
    
    #Check if the password does NOT contain a special character
    if hasSpecialChar(pw) == False:
        print("Your Password must contain at least one special character (!, @, #, $)")
        pwValid = False

    return pwValid

def main():
    #Ask the user to enter a password
    pw = input("Please enter your password: ")
    #Keep asking for a new password while it is NOT valid
    while not isPasswordValid(pw):
        print("Your password did not meet the minimum requirements. Try again.\n")
        pw = input("Please enter your new password: ")
    print("Thank you for entering a valid password")

main()
