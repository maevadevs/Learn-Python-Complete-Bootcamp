#!/usr/bin/env python
# coding: utf-8

x: int = 0
while x < 5:
    print(f"x = {x}:")
    print("\tx is less than 5, x += 1")
    x += 1
else:
    print("x is no longer less than 5")


# Using Continue
x = 0
while x < 5:
    print(f"x = {x}:")
    print("\tx is less than 5, x += 1")
    x += 1
    
    if x == 3:
        print(f"\tAlert!!! x = {x}")
    else:
        print("\tContinuing...")
        continue
else:
    print("x is no longer less than 5")


# Using Break
x = 0
while x < 5:
    print(f"x = {x}:")
    print("\tx is less than 5, x += 1")
    x += 1
    
    if x == 3:
        print(f"\tBreaking because x is {x}!")
        break
    else:
        print("\tContinuing...")
        continue
else:
    print("x is no longer less than 5")


# DO NOT RUN THIS CODE!!!! 
# while True:
#   print("Uh Oh infinite Loop!")


n: int = 0
while True:
    if n < 5:
        print("Wrong password. Please try again.")
        n += 1
    else:
        print("That was the last try. Resetting password.")
        break


