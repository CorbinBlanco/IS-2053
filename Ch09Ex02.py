"""
Exercise: 02 - Word Frequency
Write a program that asks for the name of the file to read then reads the contents of a text file. The program
should create a dictionary in which the keys are the individual words found in the file and the values are the
number of times each word appears. For example, if the word “when” appears 4 times (regardless of case),
the dictionary would contain an element with 'when' as the key and 4 as the value. The program should then
display the frequency of each word (ascending order) from the dictionary.
"""

def main():
    filename = input("Enter the name of the input file: ")

    with open(filename) as file:

        myDict = {}

        mystr = file.read().lower()
        words = mystr.split()
        for word in words:
            myDict[word] = words.count(word)

        sortedList = [(key,value) for key, value in myDict.items()]
        sortedListfinal = sorted(sortedList)

        print(f"{'Word':<15}\t{'Occurrences':<15}")
        print("----------------------------------------------")

        for key, value in sortedListfinal:
            print(f"{key:<15}{value:<15}")

if __name__ == "__main__":
    main()