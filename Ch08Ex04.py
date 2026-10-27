"""
Exercise: 04 - Word Separator
Write a program that accepts as input a sentence in which all of the words are run together, but the first character
of each word is uppercase. Convert the sentence to a string in which the words are separated by spaces, and only
the first word of the sentence starts with an uppercase letter. For example the string “StopAndSmellTheRoses.”
would be converted to “Stop and smell the roses.”
"""

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


