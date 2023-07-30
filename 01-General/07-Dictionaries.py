#!/usr/bin/env python
# coding: utf-8

from typing import Final

MY_DICT: Final[dict[str, str]] = {
  "key1":"value1",
  "key2":"value2"
}

# Call values by their key
print(MY_DICT["key2"])


from typing import Any

# Dictionaries can contain any data types (dynamic)
my_dict: dict[str, Any] = {
  "key1": 123,
  "key2": [12, 23, 33],
  "key3": ("item0", "item1", "item2")
}

# Lets call items from the dictionary
print(my_dict["key3"])


# Can call an index on that value
print(my_dict["key3"][0])


# Can then even call methods on that value
print(my_dict["key3"][0].upper())


# We can affect the values of a key as well. For instance:
print(my_dict["key1"])


# Subtract 120 from the value
my_dict["key1"] -= 120
print(my_dict["key1"])


from typing import Any

# Create a new dictionary
d: dict[str, Any] = {}

# Create a new key through assignment
d["animal"] = "Dog"

# Can do this with any object
d["answer"] = 42

# Show
print(d)


d = {
  "key1": {
    "nestkey": {
      "subnestkey":"thisvalue"
    }
  }
}

# Keep calling the keys
print(d["key1"]["nestkey"]["subnestkey"])


from typing import Final

# Create a typical dictionary
DICTO: Final[dict[str, int]] = {
  "key1": 1,
  "key2": 2,
  "key3": 3
}


print(DICTO.keys())


print(DICTO.values())


print(DICTO.items())


from typing import List

SLIST: Final[List[str]] = ["zero", "one", "two", "three", "four"]
SDICT: Final[dict[str, int]] = { v: k for k, v in enumerate(SLIST) }

print("Original List:", SLIST)
print("Enumerated Dict:", SDICT)
print("")


from typing import Final, List

# NOTE: Mapping two lists into a single dictionary uses zip instead

LIST_1: Final[List[str]] = ["first", "second", "third", "fourth"]
LIST_2: Final[List[str]] = ["bacon", "lettuce", "tomato", "egg"]

DICT: Final[dict[str, str]] = { k: v for k, v in zip(LIST_1, LIST_2) }

print("List 1:", LIST_1)
print("List 2:", LIST_2)
print("Mapping 2 List with zip():", DICT)


