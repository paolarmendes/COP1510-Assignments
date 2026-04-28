#Paola Ramos Mendes
class Car():
    #It initializes the car's year, make and sets speed to 0
    def __init__(self, year_model, make):
        self._year_model = year_model
        self._make = make
        self._speed = 0

    #The accelerate method increases the car's speed by 5
    def accelerate(self):
        self._speed += 5
    
    #The brake method decreases the car's speed by 5
    def brake(self):
        self._speed -= 5

    #The get_speed method returns the current speed of the car
    def get_speed(self):
        return self._speed
    
def main():
    #Ask the user to enter the car's year and make
    year = int(input("Enter the car's year model: "))
    make = input("Enter the car's make: ")

    #Create a Car object using the user's input
    my_car = Car(year, make)

    print("\nAccelerating...")
    
    #Call accelerate 5 times and display the speed each time
    for i in range(5):
        my_car.accelerate()
        print("Current speed:", my_car.get_speed())

    print("\nBraking...")

    #Call brake 5 times and display the speed each time
    for i in range(5):
        my_car.brake()
        print("Current speed:", my_car.get_speed())

#Call the main function to start the program
main()