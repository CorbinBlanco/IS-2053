"""
Exercise: 01 - Pet Class
Write a class named Pet, which should have the following data attributes:

_ _name (for the name of a pet)
_ _animal_type (for the type of animal that a pet is. Example values are ‘Dog’, ‘Cat’, and ‘Bird’)
_ _age (for the pet’s age)
The Pet class should have an _ _init_ _ method that creates these attributes.



It should also have the following methods:

set_name
This method assigns a value to the _ _name field.

set_animal_type
This method assigns a value to the _ _animal_type field.

set_age
This method assigns a value to the _ _age field.

get_name

This method returns the value of the _ _ name field.

get_animal_type

This method returns the value of the _ _animal_type field.

get_age
This method returns the value of the _ _age field.

Once you have written the class, write a program that creates an object of the class and prompts the user to
enter the name, type, and age of his or her pet.

This data should be stored as the object’s attributes.

Use the object’s accessor methods to retrieve the pet’s name, type, and age and display this data on the screen.
"""

from pet import Pet

pet1 = Pet(input("Enter the name of the pet: "),
           input("Enter the type of animal: "),
           input("Enter the age of the pet: "))

print("Here is the data that you entered: ")
print(f"Pet name: {pet1.get_name()}")
print(f"Animal type: {pet1.get_animal_type()}")
print(f"Age of pet: {pet1.get_age()}")