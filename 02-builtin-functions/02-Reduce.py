#!/usr/bin/env python
# coding: utf-8

from functools import reduce
from typing import List

lst_1: List[int] = [47, 11, 42, 13]
lst_sum: int = reduce(lambda agg, el: agg + el, lst_1)

print(lst_sum)


lst_2: List[str] = ["h", "e", "l", "l", "o"]
st: str = reduce(lambda agg, el: agg + el, lst_2)
print(st)


lst_3: List[int] = [47, 11, 42, 13]
lst_max: int = reduce(lambda a, b: a if (a > b) else b, lst_3)
print(lst_max)


