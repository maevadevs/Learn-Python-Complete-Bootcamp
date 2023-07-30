#!/usr/bin/env python
# coding: utf-8

from typing import Final


if True:
    print("It was true!")


X: Final[bool] = True

if X:
    print("x was True!")
else:
    print("I will be printed in any case where x is not true")


LOCATION: Final[str] = "Bank"

if LOCATION == "Auto Shop":
    print("Welcome to the Auto Shop!")
elif LOCATION == "Bank":
    print("Welcome to the bank!")
else:
    print("Where are you?")


PERSON: Final[str] = "Sammy"

if PERSON == "Sammy":
    print("Welcome Sammy!")
elif PERSON == "George":
    print("Welcome George!")
elif PERSON == "John":
    print("Welcome John!")
elif PERSON == "John":
    print("Welcome Mary!")
else:
    print("Welcome, what's your name?" )


