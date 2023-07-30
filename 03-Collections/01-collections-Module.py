#!/usr/bin/env python
# coding: utf-8

from collections import Counter

# From list to Counter
ls: list[int] = [1, 2, 2, 2, 2, 3, 3, 3, 1, 2, 1, 12, 3, 2, 32, 1, 21, 1, 223, 1]
print(Counter(ls))


# From string to Counter
sentence: str = "Hello world! This is a simple test for Counter with strings!"
words_in_sentence = Counter(sentence)
print(words_in_sentence)


# We cannot iterate through Counter() object result directly
# But we can iterate through Counter().most_common()
for k, v in words_in_sentence.most_common():
    print(f"{str(k)}: {str(v)}", end=" | ")


# `Counter` with words in a sentence
sentence = "How many times does each word show up in this sentence word times each each word"
list_words_in_sentence: list[str] = sentence.split() # Produces a list
print(Counter(list_words_in_sentence))


l: list[int] = [1, 2, 2, 2, 2, 3, 3, 3, 1, 2, 1, 12, 3, 2, 32, 1, 21, 1, 223, 1]
c = Counter(l)

print("sum(c.values()):", sum(c.values()))      # total of all counts
c.clear()                                       # reset all counts

c = Counter(l)
print("list(c):", list(c))                      # convert the keys to a list
print("set(c):", set(c))                        # convert to a set (uniques): Would result in the same as list(c)
print("dict(c):", dict(c))                      # convert to a regular dictionary: {k: v}
print("c.items():", c.items())                  # convert to a list of (elem, cnt) pairs


from collections import defaultdict
from typing import Any

d: dict = {}
# d["one"] # => Error: There is no key "one" in d

dd: defaultdict[str, str] = defaultdict(lambda: "Default value") # Default: () => 0
print(dd["one"]) # Not Error: Default value returned
dd["two"] = "Hello"

for item in dd:
    print(f"{str(item)} - {str(dd[item])}")

# Can also initialize with default values:
dd2: defaultdict[Any, int] = defaultdict(lambda: 0)
print(dd2["one"])


# Normal Dictionary
print("Normal dictionary:")
di: dict[str, str] = {}
di["a"] = "A"
di["c"] = "c"
di["b"] = "B"
di["e"] = "E"
di["d"] = "D"

for k1, v1 in di.items():
    print(k, v)


# An Ordered Dictionary
from collections import OrderedDict

print("OrderedDict:")
od: OrderedDict[str, str] = OrderedDict()
od["a"] = "A"
od["b"] = "B"
od["c"] = "C"
od["d"] = "D"
od["e"] = "E"

for k1, v1 in od.items():
    print(k, v)


# A normal Dictionary
print("Dictionaries are equal? ")

d1: dict[str, str] = {}
d1["a"] = "A"
d1["b"] = "B"

d2: dict[str, str] = {}
d2["b"] = "B"
d2["a"] = "A"

print(d1 == d2)


# An Ordered Dictionary:
print("Ordered Dictionaries are equal? ")

od1: OrderedDict[str, str] = OrderedDict()
od1["a"] = "A"
od1["b"] = "B"

od2: OrderedDict[str, str] = OrderedDict()
od2["b"] = "B"
od2["a"] = "A"

print(od1 == od2)


from collections import namedtuple

# Construction: namedtuple("ObjectName", "attr1 attr2 attr3...")
Dog: namedtuple = namedtuple("Dog", "age breed name")

sam: Dog = Dog(age=2, breed="Lab", name="Sammy")
frank: Dog = Dog(age=3, breed="Shepard", name="Frankie")

print(sam)
print(sam.age)
print(sam.breed)
print(sam[0])


