"""
Exercise: 02 - Age Classifier
Write a program that asks the user to enter a person’s age (in months). The program should display a message
indicating whether the person is an infant, a child, a teenager, or an adult.

The following are the guidelines:
• If the person is 12 months old or less, he or she is an infant.
• If the person is older than 12 months, but younger than 156 months, he or she is a child.
• If the person is at least 156 months old, but less than 240 months old, he or she is a teenager.
• If the person is at least 240 month old, he or she is an adult.
"""

user = int(input("Enter the age of the individual (in months) to classify them: "))

if user <= 12:
    print(f"This person at {user} months is an infant")
elif 12 < user < 156:
    print(f"This person at {user} months is a child")
elif 156 <= user < 240:
    print(f"This person at {user} months is a teenager")
else:
    print(f"This person at {user} months is an adult")