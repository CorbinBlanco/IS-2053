"""
Exercise: 01 - Unique Words
Write a program that opens a specified text file then displays a list of all the unique words found in the file in ascending order.
"""

def main():
    filename = input("Enter the name of the input file: ")

    with open(filename) as file:
        mySet = set()
        for line in file:
            for word in line.split():
                mySet.add(word.lower())
        wordList = (sorted(list(mySet)))

        print(f"These are the unique words in the text:")
        for word in wordList:
            print(word)







if __name__ == "__main__":
    main()
