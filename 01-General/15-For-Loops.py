#!/usr/bin/env python
# coding: utf-8

from typing import (
    Final, 
    ItemsView,
    KeysView,
    List, 
    Tuple, 
    ValuesView
)


LST: Final[List[int]] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in LST:
    print("num in lst:", num)


for num in LST:
    if num % 2 == 0:
        print(num, "-- even")
    else:
        print(num, "-- odd")


num_sum: int = 0

for num in LST:
    num_sum += num
    
print("sum of lst numbers:", num_sum)


for letter in "Hello, Earth!".upper():
    print("letter in string:", letter)


TUP: Final[Tuple[int,...]] = (1, 2, 3, 4, 5)

for t in TUP:
    print("el in tuple:", t)


LS: List[Tuple[int, int]] = [(2, 4), (6, 8), (10, 12)]

# Without tuple unpacking
for tup in LS:
    print("tuple in ls:", tup)


# Now with tuple unpacking!
for (el1, el2) in LS:
    print(f"tuple in ls contains: {el1} {el2}")


D: Final[dict[str, int]] = {
    "k1": 1,
    "k2": 2,
    "k3": 3
}

# Returns keys only
for eld in D:
    print("Key in dict:", eld)


# Accessing the Keys
W: Final[KeysView[str]] = D.keys()

for elk in W:
    print("Value in dict:", elk)


# Accessing the Values
X: Final[ValuesView[int]] = D.values()

for elv in X:
    print("Value in dict:", elv)


# Accessing the Key-value pair: Generator returning tuples
Y: Final[ItemsView[str, int]] = D.items()

print("item in dict:", Y)
for k,v in Y:
    print(f"{k} : {v}")


