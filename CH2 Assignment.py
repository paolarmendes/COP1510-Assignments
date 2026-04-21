#Your programming assignment for chapter 2 is to create a simple Python program that will calculate the tax, tip, and total of a restaurant bill. The primary purpose of this program is to make sure you have your Python environment setup and you can create a basic program.
#The program should ask the user to input the cost of the meal. Then, you will calculate the tax as 7% of the meal charge. Next, calculate the tip as 20% of the meal charge. Finally, find the total for the meal by adding the meal charge, tax, and tip. Display the output, including the amount for the tax, tip, and total.
mealCharge = float(input("Enter the cost of the meal: "))

taxAmt = mealCharge * .07

tipAmt = mealCharge * .2

totalMeal = mealCharge + taxAmt + tipAmt

print(f"For a meal charge of ${mealCharge} the tax will be ${taxAmt:.1f} and the tip amount will be ${tipAmt} for a total bill of ${totalMeal}")
