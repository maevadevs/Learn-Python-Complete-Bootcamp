#!/usr/bin/env python
# coding: utf-8

from typing import Callable, List


# Original def function
def square(num: int) -> int:
    return num**2

print(square(2))


# We can actually write this in one line (although it would be bad style to do so)
def square2(num: int) -> int: return num**2
print(square2(2))


square3: Callable[[int], int] = lambda num: num**2
print(square3(2))


lambda num1, num2: num1 * num2


multiply: Callable[[int, int], int] = lambda num1, num2: num1 * num2
print(multiply(2, 5))


# Check if a number is even
is_even: Callable[[int], bool] = lambda x: x % 2 == 0

print(is_even(3))
print(is_even(8987698759859866))


# Now, from lambda to def
def is_even2(number: int) -> bool:
    return number % 2 == 0

print(is_even2(5))


# Grab first character of a string:
get_first_char: Callable[[str], str] = lambda st: st[0]
print(get_first_char("hello"))


# Reverse a string:
reverse_string: Callable[[str], str] = lambda st: st[::-1]
print(reverse_string("hello"))


# Two arguments: No parenthesis
add: Callable[[int, int], int] = lambda x, y : x + y
print(add(2, 3))


my_nums: List[int] = [1, 2, 3, 4, 5, 6, 7]
my_nums_squared: List[int] = [x for x in map(lambda el: el**2, my_nums)]
print(my_nums_squared)


my_nums = [1, 2, 3, 4, 5, 6, 7]
my_even_nums = [x for x in filter(lambda el: el % 2 == 0, my_nums)]
print(my_even_nums)


from functools import reduce

my_nums = [1, 2, 3, 4, 5, 6, 7]
my_nums_product = reduce(lambda x, y: x * y, my_nums)

print(my_nums_product)


