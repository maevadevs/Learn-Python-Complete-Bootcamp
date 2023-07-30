#!/usr/bin/env python
# coding: utf-8

# Print the Python version from within Jupyter
from platform import python_version
from typing import Final

# Get the version
VERSION: Final[str] = python_version()
print(f"Python version: {VERSION}")


# Executing in Interactive: Can only run one line at a time
print("Hello World!")


# Executing in Script: Can run multiple lines at once
total: int = 0
i: int = 1

while i <= 100:
    total += i
    i += 1

print(f"The sum of the first 100 integers is {total}")


# This is a Python comment
# Python has mainly line comments


"""
This is a mulitple line Documentation String spanning multiple lines.
It acts like a comment for functions, classes, and modules for documentation purposes.
Outside of those, it acts as a pre-formatted string of text.
"""


# Import needed modules
from keyword import kwlist
from platform import python_version
from typing import Final, List, Tuple

# Build the list
LOWERED_KWS: Final[List[Tuple[str, str]]] = list(
    map(lambda kw: (kw, kw.lower()), kwlist)
)
SORTED_LOWERED_KWS: Final[List[Tuple[str, str]]] = sorted(
    LOWERED_KWS, key=lambda tup: tup[1]
)
SORTED_KWS: Final[List[str]] = [kw for (kw, _) in SORTED_LOWERED_KWS]

# Print the summary
print(f"There are {len(SORTED_KWS)} Keywords in Python {python_version()}:")

# Print the list of keywords
print(" / ".join(SORTED_KWS))


# Getting help on `help` function
help("help")
