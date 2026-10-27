"""
Exercise: 01 - Property Tax
A county collects property taxes on the assessment value of property, which is 75 percent of the property’s actual value.
For example, if an acre of land is valued at $13,333.33, its assessment value is $10,000. The property tax is then $1.11
for each $100 of the assessment value. The tax for the acre assessed at $10,000 will be $111.00. Write a program that
asks for the actual value of a piece of property and displays the assessment value and property tax.
"""



def main():
    actual_value = float(input("Enter the actual property value: "))
    assess_value = actual_value * 0.75
    per100 = int(assess_value / 100)
    property_tax = per100 * 1.11
    show_results(property_tax, assess_value)

def show_results(property_tax, assess_value):
    print(f"The assessed value is ${assess_value:,.2f}")
    print(f"The property tax is ${property_tax:,.2f}")


if __name__ == '__main__':
    main()


