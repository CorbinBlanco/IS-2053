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