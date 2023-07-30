#!/usr/bin/env python
# coding: utf-8

print((((3 * 10 ** 2) - 100) / 2) + 0.25)


print(4 ** (0.5))
print(4 ** 2)


# Given the string "hello", give an index command that returns "e"
# Use the code below:
ST: str = "hello"


# Print out "e" using indexing
print(ST[1])


# Reverse the string "hello" using indexing:
print(ST[::-1])


# Given the string hello, give two methods of producing the letter "o" 
# using indexing.
# Print out the result
print(ST[4])
print(ST[-1])


from typing import Final, List

LIST_1: Final[List[int]] = [0, 0, 0] # initiated
print(LIST_1)


list_2: List[int] = [] # multiple appends
list_2.append(0)
list_2.append(0)
list_2.append(0)
print(list_2)


list_3: List[int] = [0] * 3 # repeat the elements
print(list_3)


from typing import Any, List

ls: List[Any] = [1, 2, [3, 4, "hello"]]


# Reassigning
ls[2][2] = "goodbye"
print(ls)


ls = [6, 4, 5, 5, 3, 1]


ls.sort() # permanent
print(ls)
sorted(ls)
ls.reverse() # permanent
print(ls)


from typing import Any

d: dict[str, Any] = {
  "simple_key":"hello"
}


# Grab "hello"
print(d["simple_key"])


d = {
  "k1": {
    "k2":"hello"
  }
}


# Grab "hello"
print(d["k1"]["k2"])


# Getting a little tricker
d = {
  "k1":[{
    "nest_key": ["this is deep", ["hello"]]
  }]
}


# Grab hello
print(d["k1"][0]["nest_key"][1][0])


# This will be hard and annoying!
d = {
  "k1":[1, 2, {
    "k2":["this is tricky", {
      "toughie":[1, 2, ["hello"]]
    }]
  }]
}


# Grabbing hello
print(d["k1"][2]["k2"][1]["toughie"][2][0])


from typing import Final, Tuple

TUPLE_1: Final[Tuple[int,...]] = (1, 2, 2, 3)
print(TUPLE_1)


# tuple1[0] = 4 # error. immutable


from typing import List

ls_2: List[int] = [1, 2, 2, 33, 4, 4, 11, 22, 3, 3, 2]
myset: set[int] = set(ls_2) # cast a list into a set
print(myset)


# What will be the resulting Boolean of the following pieces of code 
# (answer fist then check by typing it in!)


# Answer before running cell: False
print(2 > 3)


# Answer before running cell: False
print(3 <= 2)


# Answer before running cell: False
print(3 == 2.0)


# Answer before running cell: True
print(3.0 == 3)


# Answer before running cell: False
print(4 ** 0.5 != 2)


# two nested lists
l_one: List[Any] = [1, 2, [3, 4]]
l_two: List[Any] = [1, 2, {"k1": 4}]


# True or False? 3 >= 4 False
print(l_one[2][0] >= l_two[2]["k1"])


