"""
Write a program that calculates the average of all the numbers stored in the file.
"""


def main():
    with open("numbers.txt") as file:
        total = 0
        count = 0
        for line in file:
            count += 1
            total += int(line.strip())
    print(f"The average of all the numbers in the file is {total / count:.1f}")
if __name__ == "__main__":
    main()