"""Exercise: 02 - Average Rainfall
Write a program that uses nested loops to collect data and calculate the average rainfall over a period of years.
The program should first ask for the number of years. The outer loop will iterate once for each year. The inner
loop will iterate twelve times, once for each month. Each iteration of the inner loop will ask the user for the
inches of rainfall for that month.
After all iterations, the program should display the number of months, the total inches of rainfall, and the
average rainfall per month for the entire period.
"""

total = 0

years = int(input("Enter the number of rainfall years to record: "))



for i in range(1, years + 1):
    print(f"""
**************
*** Year {i} ***
**************""")
    for j in range(1, 13):
        userR = float(input(f"Enter the rainfall amount for (year {i}/month {j}): "))
        total += userR

print()


print(f"For {years * 12} months, there was a total rainfall of {total:.1f} inches with an average monthly rainfall of {total / (years * 12):.1f} inches.")