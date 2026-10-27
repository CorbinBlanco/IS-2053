def main():


    birthday = input("Enter the short date format (mm/dd/yyyy) for this famous person's birthday: ")

    monthNames = [
        'January', 'February', 'March', 'April', 'May',
        'June', 'July', 'August', 'September',
        'October', 'November', 'December'
    ]


    new = birthday.replace('0','',1)

    newer = new.split('/')

    listInt = [int(i) for i in newer]


    print(f"The long version of this person's birthday is {monthNames[listInt[0] - 1]} {listInt[1]}, {listInt[2]}.")

if __name__ == "__main__":
    main()


