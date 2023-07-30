#!/usr/bin/env python
# coding: utf-8

# Check the definition of the CONST module
from const import CONST


CONST.GREETINGS: str = "Hello"
print(CONST.GREETINGS)


# Attempting to re-set an already defined constant with a different will result in an error
try:
    CONST.GREETINGS = "Hello again"
except Exception as e:
    print(f"{e}")

# Constant has not changed
print(CONST.GREETINGS)


# Once it has been defined, it cannot be changed again
# Evem re-assigning the same value is not acceptable

try:
    CONST.GREETINGS = "Hello"
except Exception as e:
    print(f"{e}")

# Constant has not changed
print(CONST.GREETINGS)


from typing import Final

PI: Final[float] = 3.14
print(PI)

PI = 3.1416 # This will create an error when using mypy
print(PI)   # Re-assignment is still possible


