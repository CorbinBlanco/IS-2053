"""
Exercise: 04 - Color Mixer
The colors red, blue, and yellow are known as the primary colors because they cannot be made by mixing other colors.
When you mix two primary colors, you get a secondary color, as shown here:
          When you mix red and blue, you get purple.
          When you mix red and yellow, you get orange.
          When you mix blue and yellow, you get green.

Design a program that prompts the user to enter the names of two primary colors to mix. If the user enters anything
other than “red,” “blue,” or “yellow,” the program should display an error message.
Otherwise, the program should display the name of the secondary color that results.
"""

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