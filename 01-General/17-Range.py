#!/usr/bin/env python
# coding: utf-8

from typing import Iterable


SHORT_RANGE: Iterable = range(0, 10)
print(SHORT_RANGE)


# The type of range() is a 'range object'
print(type(SHORT_RANGE))


START: int = 1 # Default is 0
STOP: int = 20 
x: Iterable = range(START, STOP)
print(x)


STEP: int = 5 # Default is 1
x = range(START, STOP, STEP)
print(x)


# Casting range to list
print(list(x))


# Casting range to set
print(set(x))


# Casting range to tuple
print(tuple(x))


for n in range(5):
    print(n, end=" ")


x = range(START, STOP, 2)
print(list(x))

x = range(START, STOP, 5)
print(list(x))


