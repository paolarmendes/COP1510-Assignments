#The following code contains a total of 5 errors that are identified as Error #1 - 5
#Edit the code to correct the 5 errors and include a comment briefly explaining what you changed for each error
#is_prime function: A number is prime if it is only evenly divisible by 1 and itself. Create a loop that tests to see if the number is evenly divisible by any number from 2 through number - 1. Use the
#modulus operator to determine if the remainder from division is 0
#03/14/2026

def is_prime(num):
    isPrime = True
    #Error #1 - Logic Error: Correct the range function call so the range function will generate numbers from 2 through num - 1
    #Correction: changed range (0, num) to range (2, num) so the loop checks numbers from 2 to -1
    for i in range(2, num):
        #Error #2 - Syntax Error: There is a syntax error in the following if expression, correct it
        #Correction: changed = to == for comparison
        if num % i == 0:
            isPrime = False
    return isPrime

def main():
    #Error #3 - Syntax Error: There is a syntax error with the following for loop header, correct it
    #correction: added the : at the end of the for loop
    for i in range(1, 101):
    #Error #4 - Syntax Error: There is a syntax error with the following if expression, correct it
    #Correction: changed isPrime(i) to is_prime(i) to match the function name
        if is_prime(i) == True:
            print(i, "is a prime number")
#Error #5 - Syntax Error: The following call to the main function does not work, correct it
#Correction: I decreased the indent 
main()
