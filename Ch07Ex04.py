"""
Exercise: 04 - Name Search
file: popular_names.txt

This file contains a list of 400 of the most popular names given to children born in the United States from the years
2000 through 2009.

Write a program that reads the contents of file into a list. The user should be able to enter a name and the program
will display a message indicating whether the name was among the list of popular names.
"""

def main():
    user = input("Enter a name to check if it was a popular name: ")
    names = []

    with open("popular_names.txt","r") as file:
        for line in file:
            names.append(file.readline().strip('\n'))

    if user in names:
        print(f"{user} was a popular name between 2000 and 2009.")
    else:
        print(f"{user} was not a popular name between 2000 and 2009.")

if __name__ == "__main__":
    main()

