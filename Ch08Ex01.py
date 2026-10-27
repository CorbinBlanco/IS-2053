"""
Exercise: 01 - Sum of Digits in a String
Write a program that asks the user to enter a series of single-digit numbers with nothing separating them. The
program should display the sum of all the single digit numbers in the string. For example, if the user enters 2514,
the method should return 12, which is the sum of 2, 5, 1, and 4.
"""

def main():
    user = int(input("Enter a sequence of digits with nothing separating them: "))

    newlist = list(str(user))
    final_list = []


    for num in newlist:
        final_list.append(int(num))

    return sum(final_list)


if __name__ == "__main__":
    print(f"The total of the digits in the string you entered is {main()}")


