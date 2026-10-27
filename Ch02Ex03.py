"""
Exercise: 03 - Miles-Per-Gallon
A car’s miles-per-gallon (MPG) can be calculated with the following formula:
MPG = Miles driven / Gallons of gas used

Write a program that asks the user for the number of miles driven and the gallons of gas used.

It should calculate the car's MPG and display the following results.
"""


user = float(input(("Enter the miles driven: ")))
gal = float(input(("Enter the gallons of fuel used: ")))
print()
print(f"Your Miles Per Gallon is {user / gal:.1f}.")