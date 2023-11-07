#!/bin/bash
# Date:  11/6/2023
# Author:  Andrew Racic
# This program will calculate an employees weekly wage based on the amount of hours worked in a single week.
# C:\Users\andre\PycharmProjects\pythonProject7

# Define the variables
regular_pay = 0.0
overtime_pay = 0.0
total_pay = 0.0

# Assign known values
pay_rate = 20
overtime_rate = 30

# Input hours from user

hours = float(input('Enter the number of hours worked: '))

# Calculate pay according to total hours worked
if hours <= 40:
    # No overtime
    regular_pay = hours * pay_rate
    overtime_pay = 0
else:
    # Overtime calculation
    regular_pay = 40 * pay_rate
    overtime_pay = (hours - 40) * overtime_rate

# Calculate the total weekly pay
total_pay = regular_pay + overtime_pay

# Output the total pay
print('The total pay is: $' + str(total_pay))
