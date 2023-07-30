#!/usr/bin/env python
# coding: utf-8

from typing import Generator, Iterator, List


def gen_squares(N: int) -> Generator[int, None, None]:
    for n in range(N):
        yield n**2

for x in gen_squares(12):
    print(x, end=" ")


import random

def rand_num(low: int, high: int, n: int) -> Generator[int, None, None]:
    for _ in range(n):
        yield random.randint(low, high)


for num in rand_num(low=1, high=100, n=12):
    print(num, end=" ")


st: str = "hello"

# Convert a string into an iterator
st_iter: Iterator[str] = iter(st)

# Now using next() to got through the string
for _ in st:
    print(next(st_iter), end=" ")


my_list: List[int] = [1, 2, 3, 4, 5,6, 7, 8, 9]

# gen_comp is a generator of item, using a generator comprehension format
gen_comp: Generator[int, None, None] = (item for item in my_list if item > 3)

for item in gen_comp:
    print(item, end=" ")


