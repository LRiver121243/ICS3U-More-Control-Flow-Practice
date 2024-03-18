"""
File: prime.py
Author: Lorenzo Rivera
Date: 2024-03-09
Description: Determines whether a program is a prime number or not.
"""

#Gets a number from user
user_number = int(input(""))

#Sets up prime number tracker
prime_counter = 0

#Determines if the number is prime
for i in range(2, user_number):
    if user_number % i != 0:
        prime_counter += 1

#Tells the user if the number is prime or not
if prime_counter == user_number - 2:
    print("Prime.")
else:
    print("Not Prime.")