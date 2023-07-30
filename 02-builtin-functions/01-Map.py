#!/usr/bin/env python
# coding: utf-8

from typing import List

def cels_to_fahr(T: float) -> float:
    return T * (9 / 5) + 32

def fahr_to_cels(T: float) -> float:
    return (T - 32) * (5 / 9)

temps: List[float] = [0, 22.5, 40, 100]
temps_fahr: List[float] = list(map(cels_to_fahr, temps))
temps_cels: List[float] = list(map(fahr_to_cels, temps_fahr))

print("Fahrs:", temps_fahr)
print("Cels:", temps_cels)


print("Cels:", list(map(lambda T: (T - 32) * (5 / 9), temps_fahr)))
print("Fahrs:", list(map(lambda T: T * (9 / 5) + 32, temps_cels)))


# The lists must have the same length
list_a: List[int] = [1, 2, 3, 4]
list_b: List[int] = [5, 6, 7, 8]
list_c: List[int] = [9, 10, 11, 12]

list(map(lambda a, b: a + b, list_a, list_b))


# Now all three lists
list(map(lambda a, b, c: a + b + c, list_a, list_b, list_c))


