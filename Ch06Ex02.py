"""
Write a program that reads all of the numbers stored in the file(numbers.txt) and then displays the calculated total
of all the numbers.
"""

def main():
    with open("numbers.txt") as file:
        total = 0
        for line in file:
            total += int(line.strip())
    print(f"The total of all the numbers in the file is {total:,.1f}")

if __name__ == "__main__":
    main()