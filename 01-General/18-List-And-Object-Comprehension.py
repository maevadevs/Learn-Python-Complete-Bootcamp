#!/usr/bin/env python
# coding: utf-8

from typing import (
    Final,
    Literal,
    List,
    TypeAlias
)
# ENUM-TYPES
EvenOddEnum: TypeAlias = Literal["ODD", "EVEN"]


# Grab every letter in string
LETTERS: Final[List[str]] = [letter for letter in "Word".lower()]
print(LETTERS)


# Equivalent in for-loop: Grab every letter in string
letters: List[str] = []

for ltr in "Word".lower():
    letters.append(ltr)

print(letters)


# Square numbers in range and turn into list
SQUARED: Final[List[int]] = [x**2 for x in range(0,11)]
print(SQUARED)


# Equivalent for loop: Square numbers in range and turn into list
squared: List[int] = []

for x in range(0,11):
    squared.append(x**2)

print(squared)


# Get even numbers from 0 up to 56, inclusive
EVEN_UPTO_56: Final[List[int]] = [x for x in range(57) if x % 2 == 0]
print(EVEN_UPTO_56)


# Equivalent for loop: Get even numbers from 0 up to 56, inclusive
even_upto_56: List[int] = []

for x in range(57):
    if x % 2 == 0:
        even_upto_56.append(x)

print(even_upto_56)


# List comprehension with if-else: Order is reversed
EVEN_ODDS: Final[List[EvenOddEnum]] = ["EVEN" if x % 2 == 0 else "ODD" for x in range(10)]
print(EVEN_ODDS)


# Equivalent in for loop: List comprehension with if-else
even_odds: List[EvenOddEnum] = []

for x in range(10):
    if x % 2 == 0:
        even_odds.append("EVEN")
    else:
        even_odds.append("ODD")

print(even_odds)


# Convert Celsius to Fahrenheit
CELSIUS: Final[List[float]] = [0, 10, 20.1, 34.5]
FAHRENHEITS: Final[List[float]] = [((float(9)/float(5)) * temp + 32) for temp in CELSIUS]
print(FAHRENHEITS)


# Equivalent in for loop: Convert Celsius to Fahrenheit
cels: List[float] = [0, 10, 20.1, 34.5]
fahrs: List[float] = []

for cel in cels:
    fahr = (float(9)/float(5)) * cel + 32
    fahrs.append(fahr)

print(fahrs)


# (x^2)^2
DOUBLE_SQUARED: Final[List[int]] = [n**2 for n in [m**2 for m in range(11)]]
print(DOUBLE_SQUARED)


# (x^2)
SQUARED_LS: Final[List[int]] = [m**2 for m in range(11)]
# (x^2)^2
DOUBLE_SQUARED_VW: Final[List[int]] = [n**2 for n in SQUARED_LS]
print(DOUBLE_SQUARED_VW)


# Equivalent in for-loop:
squared_ls: List[int] = []
double_squared: List[int] = []

# [y**2 for y in range(11)]
for y in range(11):
    squared_ls.append(y**2)

# x**2 for x in [y**2 for y in xrange(11)]
for x in squared_ls:
    double_squared.append(x**2)

print(double_squared)


# Mapping a list into a dictionary: Using enumerate()
SAMPLE_LST: Final[List[str]] = ["zero", "one", "two", "three", "four"]
SAMPLE_DICT: Final[dict[str, int]] = { value:index for (index, value) in enumerate(SAMPLE_LST) }
print(SAMPLE_DICT)


# Mapping 2 lists into a single dictionary: Using zip()
LIST_1: Final[List[str]] = ["first", "second", "third", "fourth"]
LIST_2: Final[List[str]] = ["bacon", "lettuce", "tomato", "egg"]
DICT: Final[dict[str, str]] = {k: v for (k, v) in zip(LIST_1, LIST_2)}
print(DICT)


