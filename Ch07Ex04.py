def main():
    user = input("Enter a name to check if it was a popular name: ")
    names = []

    with open("popular_names.txt","r") as file:
        for line in file:
            names.append(file.readline().strip('\n'))

    if user in names:
        print(f"{user} was a popular name between 2000 and 2009.")
    else:
        print(f"{user} was not a popular name between 2000 and 2009.")

if __name__ == "__main__":
    main()

