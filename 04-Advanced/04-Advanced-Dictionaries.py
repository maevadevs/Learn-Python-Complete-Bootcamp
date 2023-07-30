#!/usr/bin/env python
# coding: utf-8

my_dict_square: dict[int, int] = { n: n**2 for n in range(10) }
my_dict_off_one: dict[int, int] = { n: n - 1 if n > 0 else n for n in range(10) }
print("my_dict_square:", my_dict_square)
print("my_dict_off_one:", my_dict_off_one)


d: dict[str, int] = {
    "k1": 100, 
    "k2": 200
}
print("dict:", d)

print("Keys:")
for k in d.keys():
    print("-", k)

print("Values:")
for v in d.values():
    print("-", v)

print("Items:")
for item in d.items():
    print("-", item)


