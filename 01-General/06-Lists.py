#!/usr/bin/env python
# coding: utf-8

from typing import List

# Assigning a list to a variable named my_list
MY_LIST: List[int] = [1, 2, 3, 4, 5]
print(MY_LIST)


from typing import List

# Building a list of string characters from a string
MY_LIST_STR: List[str] = list("HELLO")
print(MY_LIST_STR)


from typing import List, Any

# Dynamic types
MY_LIST2: List[Any] = ["A string", 23, 100.232, "o", True, False]
print(MY_LIST2)


print(f"Length of MY_LIST: {len(MY_LIST)}")
print(f"Length of MY_LIST2: {len(MY_LIST2)}")


from typing import List

MLIST: List[int] = [0, 10, 20, 30, 40, 50]


# Grab element at index 0
print(f"MLIST[0]: {MLIST[0]}")


# Grab index from 1 and everything past it
print(f"MLIST[1:]: {MLIST[1:]}")


# Grab everything UP TO index 3 (Exclusive)
print(f"MLIST[:3]: {MLIST[:3]}")


# Grab everything from inde 1 to the end, by step of 2
print(f"MLIST[:3]: {MLIST[1::2]}")


from typing import List

int_list: List[int] = [0, 10, 20, 30, 40, 50]
new_list: List[int] = MLIST + [60, 70, 80]
print(new_list)

# Concatenate and re-assign
new_list += [90, 100]
print(new_list)


# Note: This doesn't actually change the original list!
print(f"int_list: {int_list}") # => Remains unchanged
print(f"new_list: {new_list}")


new_list += [70, 80]
print(f"new_list: {new_list}")


print(f"set(new_list): {set(new_list)}")


# Here is the original
print(f"new_list: {new_list}")


# Now we add one item
# new_list + ["Attempt to add New Item"] # Not allowed with mypy, unless using Any
new_list + [-1000]


# Did it added to my_list?... nope
print(f"my_list: {new_list}") # => Remains unchanged


# Concatenate and reassign for permanent changes
new_list += [-1000]


# Now run again?... Yes!
print(f"my_list: {new_list}") # => Changed


# Make the list double
print(MLIST * 2)


# Again duplication is not permanent unless re-assigned
print(MLIST)


from typing import List

# Create a new list
ls: List[int] = [1, 2, 3, 4, 5]
print(ls)


ls.append(6)
print(ls)


ls.pop(0) # Remove the first element
print(ls)


# Assign the popped element, remember default popped index is -1 (last item)
POPPED_ITEM: int = ls.pop()
print(POPPED_ITEM)


# Show remaining list
print(ls)


# Out of range error
try:
    ls[100]
except Exception as e:
    print(f"Error: {(type(e)).__name__}: {e}")


from typing import List

another_list: List[str] = ["a", "e", "x", "b", "c"]
print(another_list)


# Use ls.reverse() to reverse order (PERMANENT!)
another_list.reverse()
print(another_list) # => Change is permanent


# Use ls.sort() to sort the list (PERMANENT)
# In this case in alphabetical order, but for numbers it will go ascending)
another_list.sort()
print(another_list) # => Change is permanent


# Let's add numbers to the list
# Note: Must be in string format because "<" does not support comparison between int and str
another_list.append("4")
another_list.append("6")
another_list.append("89")
another_list.append("567")
another_list.append("1234")

# View the current list
print(another_list)


# Sort again: Numbers will be before letters
another_list.sort()
print(another_list) # => Change is permanent


from typing import List

# Let's make three lists
ls_1: List[int] = [1, 2, 3]
ls_2: List[int] = [4, 5, 6]
ls_3: List[int] = [7, 8, 9]


# Make a list of lists to form a matrix
matrix: List[List[int]] = [ls_1, ls_2, ls_3]
print(matrix)


# Grab first item in matrix object
print(matrix[0])


# Grab first item of the first item in the matrix object
print(matrix[0][0])


print(matrix)


from typing import Final, List

# List comprehension
FIRST_COL: Final[List[int]] = [row[0] for row in matrix]
SECOND_COL: Final[List[int]] = [row[1] for row in matrix]
THIRD_COL: Final[List[int]] = [row[2] for row in matrix]

print(f"First Column of the matrix: {FIRST_COL}")
print(f"Secnnd Column of the matrix: {SECOND_COL}")
print(f"Third Column of the matrix: {THIRD_COL}")


