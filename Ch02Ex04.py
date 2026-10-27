"""
Exercise: 04 - Tip, Tax, and Total
Write a program that calculates the total amount of a meal purchased at a restaurant. The program should ask
the user to enter the charge for the food, then calculate the amounts of a 18 percent tip and 7 percent sales tax.
Display each of these amounts and the total.
"""

user = float(input("Enter the charge for food: "))
print()
print(f"The Tip (18%) on the food charge of ${user:.2f} is ${user * 0.18:.2f}")
print(f"The Tax (7%) on the food charge of ${user:.2f} is ${user * 0.07:.2f}")
print(f"The Total amount, including Tax and Tip, is ${user + user * 0.18 + user * 0.07:.2f}")