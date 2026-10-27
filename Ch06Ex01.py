"""
Exercise: 01 - Sum of Numbers
Use the attached file numbers.txt that contains a series of integers to complete the program.

Write a program that displays all of the numbers in the file.
"""

def main():
    with open("numbers.txt") as file:
        for line in file:
            print(line.strip())

if __name__ == "__main__":
    main()