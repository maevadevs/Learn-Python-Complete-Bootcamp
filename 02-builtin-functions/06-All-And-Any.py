#!/usr/bin/env python
# coding: utf-8

from typing import List, Iterable


lst_1: List[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(all(lst_1)) # 0 == False


lst_2: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(all(lst_2))


# Custom implementation
def all_f(iterable: Iterable) -> bool:
    for el in iterable:
        if not el:
            return False
    return True


print(all_f(lst_1))
print(all_f(lst_2))


lst_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(any(lst_1))


lst_2 = [000, 00, 0, 0, 0, 0, 0, 0, 0]
print(any(lst_2))


# Custom implementation
def any_f(iterable: Iterable) -> bool:
    for el in iterable:
        if el:
            return False
    return True


print(any_f(lst_1))
print(any_f(lst_2))


