
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