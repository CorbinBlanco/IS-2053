color1 = input("Enter the first primary color (in lower case letters): ")
color2 = input("Enter the second primary color (in lower case letters): ")

if color1 != "red" and color1 != "blue" and color1 != "yellow":
    print("Error: The first color you entered is invalid.")
elif color2 != "red" and color2 != "blue" and color2 != "yellow":
    print("Error: The second color you entered is invalid.")
elif (color1 == "red" and color2 == "blue") or (color1 == "blue" and color2 == "red"):
    print("purple")
elif (color1 == "red" and color2 == "yellow") or (color1 == "yellow" and color2 == "red"):
    print("orange")
elif (color1 == "blue" and color2 == "yellow") or (color1 == "yellow" and color2 == "blue"):
    print("green")