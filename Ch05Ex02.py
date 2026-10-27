"""
Exercise: 02 - Paint Job Estimator
A painting company has determined that for every 90 square feet of wall space, one gallon of paint and seven
hours of labor will be required. The company charges $45.00 per hour for labor. Write a program that asks the
user to enter the square feet of wall space to be painted and the price of the paint per gallon.

The program should display the following data:
• The number of gallons of paint required
• The hours of labor required
• The cost of the paint
• The labor charges
• The total cost of the paint job
"""

print("***********************")
print("* PAINT JOB ESTIMATOR *")
print("***********************")

def main():
    wall_space = float(input("Enter wall space in square feet: "))
    paint_price = float(input("Enter paint price per gallon: "))

    total_gallons = int(wall_space/ 90) + 1
    total_hours = total_gallons * 7
    total_paint_cost = total_gallons * paint_price
    total_labor_cost = total_hours * 45
    show_results(total_gallons, total_hours, total_paint_cost, total_labor_cost)


def show_results(total_gallons, total_hours, total_paint_cost,total_labor_cost):
    print()
    print(f"The total gallons of paint needed for the job is {total_gallons}")
    print(f"The total of hours of labor required for the job is {total_hours}")
    print(f"The total paint cost for the job is ${total_paint_cost:,.2f}")
    print(f"The total labor cost for the job is ${total_labor_cost:,.2f}")
    print("**********************************************************")
    print(f"Total estimate for the paint job totals to ${total_paint_cost + total_labor_cost:,.2f}")



if __name__ == "__main__":
    main()