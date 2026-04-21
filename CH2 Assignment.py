#Paola Ramos Mendes
#Chapter 2 assignment
mealCharge = float(input("Enter the cost of the meal: "))

taxAmt = mealCharge * .07

tipAmt = mealCharge * .2

totalMeal = mealCharge + taxAmt + tipAmt

print(f"For a meal charge of ${mealCharge} the tax will be ${taxAmt:.1f} and the tip amount will be ${tipAmt} for a total bill of ${totalMeal}")