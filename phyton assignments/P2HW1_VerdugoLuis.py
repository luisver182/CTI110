# Verdugo Luis
# 04/23/2025
# P2HW1
# TRAVEL EXPENSES
# FLOAT, DECIMAL & $ SIGN
import math
print('This program calculates and displays travel expenses')
print('enter budget:', end=' ')
budget = float(input())
print('Enter your travel destination:', end=' ')
trip_destination = input()
print('How much do you think you will spend on gas?:', end=' ')
gas = float(input())
print('Approximately, how much will you need for accomodation/hotel?:', end=' ')
hotel = float(input())
print('Last, how much do you need for food?:', end=' ')
food = float(input())
budget2 = budget - (gas + hotel + food)
print('--------Travel Expenses--------')
print(f"{'location:':<21}{trip_destination}")
print(f"{'Initial Budget:':<20} ${budget:.2f}")
print(f"{'fuel:':<20} ${gas:.2f}")
print(f"{'accomodation:':<20} ${hotel:.2f}"),
print(f"{'food:':<20} ${food:.2f}")
print("--------------------------------")
print(f"{'Remaining Balance:':<20} ${budget2:.2f}")
