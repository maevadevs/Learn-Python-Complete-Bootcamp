#!/usr/bin/env python
# coding: utf-8

print(123, type(123))
print(-456, type(-456))


# 4 * 10^2 = 400.0
print(4e2, type(4e2))
# -2 * 10^5 = 200000.0
print(-2e5, type(2e5))


# Addition
print(2 + 1)


# Subtraction
print(2 - 1)


# Multiplication
print(2 * 2)


# Real Division
print(3 / 2)


# Floor Division
print(3 // 2)


# Modulo
print(7 % 4)


# Exponent
print(2**3)


# Square Root of 4
print(4**(1 / 2))


# Cubic Root of 27
print(27**(1 / 3))


# Fourth Root of 625
print(625**(1 / 4))


# Order of Operations: PEMDAS - Standard Math
print(2 + 10 * 10 + 3)


# Use parenthesis to specify priority: PEMDAS - Standard Math
print((2 + 10) * (10 + 3))


x = 0.1 + 0.2 - 0.3
print(x)


print(x == 0)


print(float("3.14"), type(float("3.14")))
print(int("3"), type(int("3")))
print(str(3.14), type(str(3.14)))


a: int = 5
print(a + a)


# Re-assignement
a = 50
print(a)


# Declare with types without errors
user_age: int
user_name: str

# Tuple variable assignment
user_age, user_name = 30, "john.test"

print(user_age)
print(user_name)


# Re-assignement using self
a = a + a
print(a)


# There is a shortcut for add-and-assign as well
a += a
print(a)


from typing import Final

AN_INT: Final[int] = 1
A_FLOAT: Final[float] = 1.2
A_BOOL: Final[bool] = True

print("type(a):", type(AN_INT))
print("type(b):", type(A_FLOAT))
print("type(c):", type(A_BOOL))


# Import needed modules
from keyword import kwlist
from platform import python_version
from typing import Final, List, Tuple

# Build the list
LOWERED_KWS: Final[List[Tuple[str, str]]] = list(map(lambda kw: (kw, kw.lower()), kwlist))
SORTED_LOWERED_KWS: Final[List[Tuple[str, str]]] = sorted(LOWERED_KWS, key=lambda tup: tup[1])
SORTED_KWS: Final[List[str]] = [kw for (kw, _) in SORTED_LOWERED_KWS]

# Print the summary
print(f"There are {len(SORTED_KWS)} Keywords in Python {python_version()}:")

# Print the list of keywords
print(" // ".join(SORTED_KWS))


from typing import Final

MY_INCOME: Final[int] = 100
TAX_RATE: Final[float] = 0.1
MY_TAX: Final[float] = MY_INCOME * TAX_RATE

print(f"My Taxes are ${MY_TAX:0.2f}")


