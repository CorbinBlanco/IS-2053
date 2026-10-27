
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


