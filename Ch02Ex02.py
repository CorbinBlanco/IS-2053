"""
Exercise: 02 - Distance Traveled
Assuming there are no accidents or delays, the distance that a car travels down the interstate can be calculated with the following formula:

Distance = Speed x Time

The car speed will be entered by the user

Write a program that displays the following:
The distance the car will travel in 5 hours
The distance the car will travel in 10 hours
The distance the car will travel in 15 hours
"""


user = (int(input("Enter the speed the car is traveling:")))
print(f""" The car will travel the following distances:
{user * 5:,} miles in 5 hours.
{user * 10:,} miles in 10 hours.
{user * 15:,} miles in 15 hours.""")