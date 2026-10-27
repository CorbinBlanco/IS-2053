"""
Exercise: 03 - Penny Pay
Write a program that calculates the amount of money a person would earn over a period of time if his or
her salary is one penny the first day, two pennies the second day, and continues to double each day.
The program should ask the user for the number of days. Display a table showing what the salary was for
each day, then show the total pay at the end of the period. The output should be displayed in a dollar
amount, not the number of pennies.
"""

days = int(input("Enter the number of days: "))
pay = 0.01
balance = 0


print("""
Day:\tPay\t\tBalance
--------------------------------------------""")

for i in range(1, days + 1):
    balance += pay

    print(f"{i:<10}{f'${pay:,.2f}':<11}{f'${balance:<10,.2f}'}")


    pay *=2
print("--------------------------------------------")

print(f"The total salary for {days} days is: ${balance:,.2f}")

