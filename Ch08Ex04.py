def main():
    string = input("Enter a string: ")
    newString = ""
    stringList = []

    for i, char in enumerate(string):
        if char.isupper() and i > 0:
            stringList.append(' ')
        stringList.append(char)

    for char in stringList:
        newString = newString + char

    lowered = newString.lower()
    final = lowered.replace(lowered[0],lowered[0].upper(),1)

    print(final)

if __name__ == "__main__":
    main()


