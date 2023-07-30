#!/usr/bin/env python
# coding: utf-8

my_set: set[int] = set()


my_set.add(1)
my_set.add(2)
my_set.add(3)
print("my_set.add(3):", my_set)

my_set.add(1)
print("my_set.add(1):", my_set)


my_set.clear()
print("my_set.clear():", my_set)


my_set = {1, 2, 3}
my_set_copy = my_set.copy()
print("my_set:", my_set)
print("my_set_copy:", my_set_copy)

my_set.add(4)
print("my_set.add(4):", my_set)
print("my_set_copy:", my_set_copy)


print("my_set.difference(my_set_copy):", my_set.difference(my_set_copy))


set1: set[int] = {1, 2, 3}
set2: set[int] = {1, 4, 5}

print("set1:", set1)
print("set2:", set2)

print("set1.difference_update(set2)")
set1.difference_update(set2)

print("set1 after:", set1)
print("set2 after:", set2)


my_set = {1, 2, 3, 4}
print("my_set:", my_set)
print("my_set.discard(2)")
my_set.discard(2)
print("my_set after:", my_set)


s1: set[int] = {1, 2, 3, 4}
s2: set[int] = {1, 2, 4, 5}

print("s1:", s1)
print("s2:", s2)
print("s1.intersection(s2):", s1.intersection(s2))
print("s1:", s1)


print("s1.intersection_update(s2)")
s1.intersection_update(s2)
print("s1:", s1)
print("s2:", s2)


s1 = {1, 2}
s2 = {1, 2, 4}
s3: set[int] = {5}

print("s1:", s1)
print("s2:", s2)
print("s3:", s3)
print("s1.isdisjoint(s2):", s1.isdisjoint(s2))
print("s1.isdisjoint(s3):", s1.isdisjoint(s3))


print("s1:", s1)
print("s2:", s2)
print("s1.issubset(s2):", s1.issubset(s2))


print("s2.issuperset(s1):", s2.issuperset(s1))


print("s1:", s1)
print("s2:", s2)
print("s1.symmetric_difference(s2):", s1.symmetric_difference(s2))
print("s1:", s1)
print("s2:", s2)
print("s1.symmetric_difference_update(s2)")
s1.symmetric_difference_update(s2)
print("s1:", s1)
print("s2:", s2)


s1 = {1, 2, 5}
s2 = {1, 2, 4}
print("s1:", s1)
print("s2:", s2)
print("s1.union(s2):", s1.union(s2))


s1 = {1, 2, 5}
s2 = {1, 2, 4}
print("s1:", s1)
print("s2:", s2)
print("s1.update(s2)")
s1.update(s2)
print("s1:", s1)


