min = float(0)
max = float(0)
total = float(0)
user = float(1)
amt = 0



while user > 0:
    user = float(input(f"Enter a positive number to add and negative number to quit - Number {amt + 1:02}: "))

    if user > 0:
        if amt == 0:
            min = user
            max = user

        else:
            if user < min:
                min = user
            if user > max:
                max = user


        amt += 1
        total += user






print()


print(f"The minimum of all {amt} numbers is {min:.1f}")
print(f"The maximum of all {amt} numbers is {max:.1f}")
print(f"The average of all {amt} numbers is {total / amt:.1f}")
print(f"The total of all {amt} numbers is {total:.1f}")