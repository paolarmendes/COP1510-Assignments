#Paola Ramos Mendes
#CH4 Assignment 
#02/20/2026
speed=int(input("What is the speed of the vehicle in mph? ")) #Here I asked the user for the speed of a vehicle in miles per hour
while speed < 1: #confirms that speed must be at least 1
    print("Speed must be 1 or greater") #if its less than one, this will be printed 
    speed = int(input("What is the speed of the vehicle in mph? ")) #then this 

hours = int(input("How many hours has it traveled? ")) #Here I asked how many hours has it traveled
while hours < 1: #confirms that hours must be at least 1
    print("Hours must be 1 or greater") #if its less than 1, this will be printed
    hours = int(input("How many hours has it traveled? ")) #then this

print() #it will print a blank space 
print("Hour\tDistance Traveled") #it will print Hour and Distance Traveled side by side with a space between
print("--------------------------") #it will print dashes 

for number in range (1, hours +1): #loops through each hour from 1 up to the total number of hours
    distanceTraveled = speed*number #calculates the distance traveled by multiplying speed by time
    print(f'{number}\t{distanceTraveled}') #displays the hour and distance traveled in a table format