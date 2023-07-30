#!/usr/bin/env python
# coding: utf-8

from typing import List


# A simple list
ls: List[int] = [x + 1 for x in range(9)]
print(ls)


ls.append(10)
print(ls)


ls.append(2)
ls.append(2)
ls.append(2)
print(ls.count(2))


help(ls.count)


help(ls.append)


