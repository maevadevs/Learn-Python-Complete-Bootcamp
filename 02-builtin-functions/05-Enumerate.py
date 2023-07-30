#!/usr/bin/env python
# coding: utf-8

from typing import List


lst: List[str] = ["a", "b", "c"]

for i, el in enumerate(lst):
    print(i, el)


for index, item in enumerate(lst):
    if index >= 2:
        break
    else:
        print(index, item)


sample_list: List[str] = ["zero", "one", "two", "three", "four"]
sample_dict: dict[str, int] = { v: k for k, v in enumerate(sample_list) }

print("Original List:", sample_list)
print("Enumerated Dict:", sample_dict)
print("")


# NOTE: Mapping two lists into a single dictionary uses zip instead

list1: List[str] = ["first", "second", "third", "fourth"]
list2: List[str] = ["bacon", "lettuce", "tomato", "egg"]

dictionary: dict[str, str] = { k: v for k, v in zip(list1, list2) }

print("List 1:", list1)
print("List 2:", list2)
print("Mapping 2 List with zip():", dictionary)


