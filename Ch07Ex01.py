def main():
    sales = []
    total = 0


    print("Welcome to the Daily Sales Accumulator")
    print("ENTER THE SALES FOR THE WEEK")
    print("------------------------------------------")


    sales.append((int(input("Enter the sales for Sunday: "))))
    sales.append((int(input("Enter the sales for Monday: "))))
    sales.append((int(input("Enter the sales for Tuesday: "))))
    sales.append((int(input("Enter the sales for Wednesday: "))))
    sales.append((int(input("Enter the sales for Thursday: "))))
    sales.append((int(input("Enter the sales for Friday: "))))
    sales.append((int(input("Enter the sales for Saturday: "))))

    print("------------------------------------------")

    for sale in sales:
        total += sale

    print(f"Total sales for the week was ${total:,.2f}")

    print()
    detailed = input("Would you like to view a detailed summary? (N/Y) : ")

    if detailed == "Y":
        print()
        print("DETAILED WEEK SUMMARY")
        print("------------------------------------------")

        print(f"Sunday's sales were ${sales[0]:,.2f}")
        print(f"Monday's sales were ${sales[1]:,.2f}")
        print(f"Tuesday's sales were ${sales[2]:,.2f}")
        print(f"Wednesday's sales were ${sales[3]:,.2f}")
        print(f"Thursday's sales were ${sales[4]:,.2f}")
        print(f"Friday's sales were ${sales[5]:,.2f}")
        print(f"Saturday's sales were ${sales[6]:,.2f}")

        print("------------------------------------------")

        print(f"Total sales for the week was ${total:,.2f}")

    print()
    print("Thank you for using Daily Sales Accumulator")
    print("Program ended....")

if __name__ == "__main__":
    main()
