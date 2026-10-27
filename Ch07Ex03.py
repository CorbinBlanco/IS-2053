def main():
    nums = []
    for i in range(1,21):
        nums.append(int(input(f"Enter number {i} of 20: ")))
    average = sum(nums)/len(nums)

    print("-------------------------------")
    print()

    print(f"The lowest number in the list is {min(nums):.1f}")
    print(f"The highest number in the list is {max(nums):.1f}")
    print(f"The average of all the numbers in the list is {average:.1f}")
    print(f"The sum of all the numbers in the list is {sum(nums):,.1f}")
    print("-------------------------------")
    print()

    print("The numbers in the list sorted from smallest to largest is as follows:")
    nums.sort()
    for num in nums:
        print(f"{num:.1f}")
    print("-------------------------------")
    print()

    print("The numbers in the list sorted from largest to smallest is as follows:")
    nums.reverse()
    for num in nums:
        print(f"{num:.1f}")
    print("-------------------------------")

if __name__ == "__main__":
    main()
