

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