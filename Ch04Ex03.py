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

