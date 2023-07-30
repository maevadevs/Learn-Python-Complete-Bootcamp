#!/usr/bin/env python
# coding: utf-8

from typing import Any, Final, List, Optional


x: set[int] = set()
x.add(1)
print(x)


# Add a different element
x.add(2)
print(x)


# Try to add the same element
x.add(1)
print(x)


# Create a list with multiple duplicate elements
MY_LIST: Final[List[Any]] = [1, 1, 2, 2, 3, 4, 5, 6, 1, 1, True, False, 0, 0, True, "hello"]

# Cast as set() to get unique values: Get a set out of a list
MY_SET: Final[set[Any]] = set(MY_LIST)
print(MY_SET)


print(True == 1)


print(False == 0)


# Set object to be a boolean
A: bool = True
print(A)


# We can also use comparison operators to create booleans
print(1 > 2)


# We can use `None` as a placeholder for an object that we do not want to reassign yet (null):
# None placeholder: similar to null and nil in other languages
b: Optional[int] = None
print(b)


