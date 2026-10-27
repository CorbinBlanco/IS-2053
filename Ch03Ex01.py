"""
Exercise: 01 - Areas of Rectangles
The area of a rectangle is the rectangle’s length times its width. Write a program that asks for the length and
width of two rectangles. The program should tell the user which rectangle has the greater area, or if the areas
are the same.
"""

rectl1 = int(input("Enter length of rectangle A: "))
rectw1 = int(input("Enter width of rectangle A: "))

rectl2 = int(input("Enter length of rectangle B: "))
rectw2 = int(input("Enter width of rectangle B: "))

areaA = rectl1*rectw1
print(f"The Area of A is {areaA:.1f}")
areaB = rectl2*rectw2
print(f"The Area of B is {areaB:.1f}")

if areaA > areaB:
    print("Area A is greater than Area B.")

elif areaB > areaA:
    print("Area B is greater than Area A.")

elif areaA == areaB:
    print("Area A is equal to Area B.")
