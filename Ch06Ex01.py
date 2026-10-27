def main():
    with open("numbers.txt") as file:
        for line in file:
            print(line.strip())

if __name__ == "__main__":
    main()