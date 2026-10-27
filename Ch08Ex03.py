def main():
    use = []
    user = input("Enter a string: ").upper()
    string = list(user.replace(" ",""))

    max = 0
    letter = None

    for char in string:
        if string.count(char) >= max:
            max = string.count(char)
            letter = char

    print(f"The character that appears most frequently in the string is {letter}.")


if __name__ == "__main__":
    main()

