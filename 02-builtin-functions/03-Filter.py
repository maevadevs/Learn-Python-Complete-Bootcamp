#!/usr/bin/env python
# coding: utf-8

from typing import Any, Callable, List


is_even: Callable[[int], bool] = lambda num: num % 2 == 0
is_odd: Callable[[int], bool] = lambda num: num % 2 != 0


lst: range = range(20)
lst_even: List[int] = list(filter(is_even, lst))
print(lst_even)


lst_odd: List[int] = list(filter(is_odd, lst))
print(lst_odd)


lst_even = list(filter(lambda x: x % 2 == 0, lst))
print(lst_even)


from math import sqrt

def is_prime(num: int) -> bool:
    """   
    Optimised method for checking if an integer number is prime or not.

    Arguments:
        - `num`: The number to check if it is prime or not.

    Return:
        - bool Whether the `num` is prime or not
    """

    # Special cases
    if type(num) != int or num <= 1:
        return False

    # First 4 prime numbers
    if num in {2, 3, 5, 7}:
        return True

    # Divisible by 2
    if num % 2 == 0:
        return False

    # Divisible by 3
    if num % 3 == 0:
        return False

    # Divisible by 5
    if num % 5 == 0:
        return False

    # Beyond 10, only integers ending in 1,3,7,9 can be prime
    # Else, they are either divisible by 2 or 5
    if (num > 10) and (num % 10 in {1,3,7,9}):
        # Loop through possible divisors up to the sqrt
        for n in range(3, int(sqrt(num))+1):
            if num % n == 0:
                return False

    # If still here then prime
    return True


prime_numbers: List[int] = list(filter(is_prime, lst)) # Filter the prime numbers from our list
print("Prime Numbers:", prime_numbers)


from typing import Callable
from collections.abc import Sequence

def custom_filter_implementation(func_filter: Callable[[Any], bool], m_list: Sequence[Any]) -> List[Any]:
    final_list: List[Any] = []
    for el in m_list:
        if func_filter(el):
            final_list.append(el)
    return final_list


even_numbers: List[int] = custom_filter_implementation(lambda x: x % 2 == 0, lst)
print("Even Numbers using custom filter() implementation:", even_numbers)


