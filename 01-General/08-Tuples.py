#!/usr/bin/env python
# coding: utf-8

from typing import Any, Tuple

# We can create a tuple with mixed types
TUP_1: Tuple[Any,...] = (1, 2, 3, "hello", False)
TUP_2: Tuple[Any,...] = 1, 2, 3, "hello", False

# Check length just like a list
print(len(TUP_1))
print(len(TUP_2))


# Can also mix object types
T: Tuple[Any,...] = ("one", 2, [1, 2, 3], {"greeting":"hello"})
print(T)


# Use indexing just like we did in lists
print(T[0])


# Slicing just like a list
print(T[-1])


# But changing the value is not permissible
# This is an error: "tuple" object does not support item assignment
# T[1] = 100


print(T.index("one"))


print(T.count("one"))


