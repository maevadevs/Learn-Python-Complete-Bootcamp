#!/usr/bin/env python
# coding: utf-8

from typing import List


row0: List[int] = [1, 2, 3]
row1: List[int] = [4, 5, 6]
row2: List[int] = [7, 8, 9]

print("Matrix:")
print(row0)
print(row1)
print(row2)
print("")
print("col0:", list(zip(row0, row1, row2))[0])
print("col1:", list(zip(row0, row1, row2))[1])
print("col2:", list(zip(row0, row1, row2))[2])
print("")
print(list(zip(row0, row1, row2)))


x: List[int] = [1, 2, 3]
y: List[int] = [4, 5, 6]

print(list(zip(x, y)))


a: List[str] = ["A", "B", "C"]
b: List[int] = [4, 5, 6, 7, 8, 9]

print(list(zip(a, b)))


# What if we want to zip more than two lists?
i: List[int] = [1, 2, 3]
j: List[int] = [4, 5, 6, 7, 8]
k: List[int] = [9, 10]

print(list(zip(i, j, k)))


d1: dict[str, int] = {"a": 1, "b": 2}
d2: dict[str, int] = {"c": 4, "d": 5}

print(list(zip(d1, d2)))


print(list(zip(d1, d2)) + list(zip(d1.values(), d2.values())))


def switch_around(d1: dict, d2: dict) -> dict:
    d_out: dict = {}
    
    for d1_key, d2_val in zip(d1, d2.values()):
        d_out[d1_key] = d2_val
    
    return d_out


print("d1 =", d1)
print("d2 =", d2)
print("Switched =", switch_around(d1, d2))


