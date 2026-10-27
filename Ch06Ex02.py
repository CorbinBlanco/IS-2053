def main():
    with open("numbers.txt") as file:
        total = 0
        for line in file:
            total += int(line.strip())
    print(f"The total of all the numbers in the file is {total:,.1f}")

if __name__ == "__main__":
    main()