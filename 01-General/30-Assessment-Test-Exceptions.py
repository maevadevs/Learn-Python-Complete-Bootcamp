#!/usr/bin/env python
# coding: utf-8

try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError as e:
    print(f"Oops! TypeError: {str(e)}")


try:
    x: int = 5
    y: int = 0
    z: float = x / y
except ZeroDivisionError as e:
    print(f"ZeroDivisionError Error: {str(e)}")
finally:
    print("All done!")


def ask() -> None:
    while True:
        try:
            userInput: str = input("Enter an integer: ")
            print(f"The square of {userInput} is: {str(int(userInput) ** 2)}")
            break
        except Exception as e:
            print("Error: " + str(e))


ask()


