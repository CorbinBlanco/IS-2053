"""
Exercise: 03 - Minimum Value - Maximum Value - Same Value
Write functions for minimum value, maximum value and same value that accepts three integer values as arguments
and returns if they are the same. If not it will return the value that is the minimum value of the three and also the
value that is the maximum of the three values. For example, if 3, 3, 3 are passed as arguments, the program will
display that all three numbers are the same. If 1, 2, 3 are passed as arguments, the program will display which value
is the minimum and which value is the maximum.
"""

def find_status(num1, num2, num3):
    minimum = num1
    maximum = num1

    if num2 < minimum:
        minimum = num2
    if num3 < minimum:
        minimum = num3

    if num2 > maximum:
        maximum = num2
    if num3 > maximum:
        maximum = num3

    total = num1 + num2 + num3
    average = total / 3

    return minimum, maximum, total, average

def results(num1, num2, num3):
    minimum, maximum, total, average = find_status(num1, num2, num3)


    if minimum == maximum:
        print("All numbers are the same")
    else:
        print(f"The minimum number is: {minimum:.1f}")
        print(f"The maximum number is: {maximum:.1f}")
        print(f"The average of the numbers is: {total / 3:.1f}")
        print(f"The total of the numbers is: {total:.1f}")



num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
print()
results(num1, num2, num3)