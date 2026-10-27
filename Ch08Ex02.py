"""
Exercise: 02 - Date Printer
Write a program that reads a date in the form mm/dd/yyyy and converts it to a string of Month, Day, and Year.
"""


def main():

    birthday = input("Enter the short date format (mm/dd/yyyy) for this famous person's birthday: ")

    monthNames = [
        'January', 'February', 'March', 'April', 'May',
        'June', 'July', 'August', 'September',
        'October', 'November', 'December'
    ]


    new = birthday.replace('0','',1)

    new = new.split('/')

    listInt = [int(i) for i in new]


    print(f"The long version of this person's birthday is {monthNames[listInt[0] - 1]} {listInt[1]}, {listInt[2]}.")

if __name__ == "__main__":
    main()


