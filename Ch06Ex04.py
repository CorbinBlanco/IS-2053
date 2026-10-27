def main():
    jan = 31
    feb = 28
    mar = 31
    apr = 30
    may = 31
    jun = 30
    jul = 31
    aug = 31
    sep = 30
    oct = 31
    nov = 30
    dec = 31

    with open("steps.txt", "r") as file:
        total = 0
        count = 0
        for i in range(jan):
            total += int(file.readline())
            count += 1
        print(f"The average steps taken in January was {total/count:,.1f}")

        total = 0
        count = 0
        for i in range(feb):
            total += int(file.readline())
            count += 1
        print(f"The average steps taken in February was {total / count:,.1f}")

        total = 0
        count = 0
        for i in range(mar):
            total += int(file.readline())
            count += 1
        print(f"The average steps taken in March was {total / count:,.1f}")

        total = 0
        count = 0
        for i in range(apr):
            total += int(file.readline())
            count += 1
        print(f"The average steps taken in April was {total / count:,.1f}")

        total = 0
        count = 0
        for i in range(may):
            total += int(file.readline())
            count += 1
        print(f"The average steps taken in May was {total / count:,.1f}")

        total = 0
        count = 0
        for i in range(jun):
            total += int(file.readline())
            count += 1
        print(f"The average steps taken in June was {total / count:,.1f}")

        total = 0
        count = 0
        for i in range(jul):
            total += int(file.readline())
            count += 1
        print(f"The average steps taken in July was {total / count:,.1f}")

        total = 0
        count = 0
        for i in range(aug):
            total += int(file.readline())
            count += 1
        print(f"The average steps taken in August was {total / count:,.1f}")

        total = 0
        count = 0
        for i in range(sep):
            total += int(file.readline())
            count += 1
        print(f"The average steps taken in September was {total / count:,.1f}")

        total = 0
        count = 0
        for i in range(oct):
            total += int(file.readline())
            count += 1
        print(f"The average steps taken in October was {total / count:,.1f}")

        total = 0
        count = 0
        for i in range(nov):
            total += int(file.readline())
            count += 1
        print(f"The average steps taken in November was {total / count:,.1f}")

        total = 0
        count = 0
        for i in range(dec):
            total += int(file.readline())
            count += 1
        print(f"The average steps taken in December was {total / count:,.1f}")

if __name__ == "__main__":
    main()
