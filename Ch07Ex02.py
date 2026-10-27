"""
Exercise: 02 - Rainfall Statistics
Design a program that lets the user enter the total rainfall for each of 12 months into a list. The program
should calculate and display the total rainfall for the year, the average monthly rainfall, the months with
the highest and lowest amounts.
"""

def main():

    rainfall = []

    print("***************************")
    print("*** Rainfall Statistics ***")
    print("***************************")

    rainfall.append(["January",(float(input("Enter the rainfall for January: ")))])
    rainfall.append(["February",(float(input("Enter the rainfall for February: ")))])
    rainfall.append(["March",(float(input("Enter the rainfall for March: ")))])
    rainfall.append(["April",(float(input("Enter the rainfall for April: ")))])
    rainfall.append(["May",(float(input("Enter the rainfall for May: ")))])
    rainfall.append(["June",(float(input("Enter the rainfall for June: ")))])
    rainfall.append(["July",(float(input("Enter the rainfall for July: ")))])
    rainfall.append(["August",(float(input("Enter the rainfall for August: ")))])
    rainfall.append(["September",(float(input("Enter the rainfall for September: ")))])
    rainfall.append(["October",(float(input("Enter the rainfall for October: ")))])
    rainfall.append(["November",(float(input("Enter the rainfall for November: ")))])
    rainfall.append(["December",(float(input("Enter the rainfall for December: ")))])

    print("--------------------------------------")

    total = 0
    i = 0

    for i in range (len(rainfall)):
        total += rainfall[i][1]

    average = total / len(rainfall)

    print()
    print(f"The total rainfall for the year was {total:.1f}")
    print(f"The average rainfall for the year was {average:.1f}")
    print(f"The month with the highest rainfall was {max(rainfall, key=lambda x: x[1])[0]}")
    print(f"The month with the lowest rainfall was {min(rainfall, key=lambda x: x[1])[0]}")

    detailed = input("Would you like a detailed summary? (Y/N): ")
    if detailed == "Y":
        print()
        print("Rainfall Statistics Detailed Summary")
        print("--------------------------------------")

        for f in range(len(rainfall)):
            print(f"The rainfall for {rainfall[f][0]} was {rainfall[f][1]}")
        print("--------------------------------------")

        print(f"The total rainfall for the year was {total:.1f}")
        print(f"The average rainfall for the year was {average:.1f}")
        print(f"The month with the highest rainfall was {max(rainfall, key=lambda x: x[1])[0]}")
        print(f"The month with the lowest rainfall was {min(rainfall, key=lambda x: x[1])[0]}")

    print()
    print("Have a good day!")
    print("Program stopped...")

if __name__ == "__main__":
    main()
