"""
Exercise: 01 - Bug Collector
A bug collector collects bugs every day for seven days. Write a program that keeps a running total of the number
of bugs collected during the seven days. The loop should ask for the number of bugs collected for each day, and
when the loop is finished, the program should display the total number of bugs collected.
"""



total = 0

for i in range(1,8):
    user = (int(input(f"Enter the number of bugs collected on day {i}: ")))
    total += user

print(f"You collected a total of {total} bugs.")



