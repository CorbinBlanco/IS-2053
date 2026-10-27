def main():
    user = int(input("Enter a sequence of digits with nothing separating them: "))

    newlist = list(str(user))
    final_list = []


    for num in newlist:
        final_list.append(int(num))

    return sum(final_list)


if __name__ == "__main__":
    print(f"The total of the digits in the string you entered is {main()}")


