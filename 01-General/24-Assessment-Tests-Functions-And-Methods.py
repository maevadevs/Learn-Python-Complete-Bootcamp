#!/usr/bin/env python
# coding: utf-8

from math import pi # Need to import math.pi for all math works in here
from typing import Any, List, Tuple


def volume(r: float) -> float:
    return (4/3) * pi * (r**3)


# Testing
r: float = 3
print(volume(r))


def range_check(num: int, low: int, high: int) -> str:
    """
    Check if `num` is within the range of `low` and `high`. Return answer as a string.
    
    Arguments:   
        - `num`: The number to check
        - `low`: The lower limit (inclusive)
        - `high`: The higher limit (inclusive)
    
    Return: 
        - Text stating the result
    """
    
    if num in range(low, high+1):
        return "{0} is within the range of [{1}, {2}]".format(num, low, high)
    else:
        return "{0} is not in the range of [{1}, {2}]".format(num, low, high)


print(range_check(10, 5, 67))


# If you only wanted to return a boolean:
def range_bool(num: int, low: int, high: int) -> bool:
    """
    Check whether `num` is within the range of `low` and `high` or not.
    
    Arguments:   
        - `num`: The number to check
        - `low`: The lower limit (inclusive)
        - `high`: The higher limit (inclusive)
    
    Return: 
        - Boolean result of whether the check is True or False
    """
    
    return num in range(low, high+1)


print(range_bool(3, 1, 10))


from string import (
    ascii_lowercase, 
    ascii_uppercase, 
    punctuation
)

def count_chars(strg: str) -> Tuple[int, int, int]:
    """
    Check the number of uppercases characters, lowercases characters, and punctuations in a string.
    Need to import the string module. 
    Return the numbers in a tuple.
    
    Arguments:   
        - `str`: The original string to test
    
    Return: 
        - Count of uppercases characters, lowercases characters, and punctuations in the string
    """
    
    upper_count: int = 0
    lower_count: int = 0
    punct_count: int = 0
    letters: List[str] = [strg[i] for i in range(0, len(strg))]
    
    for ltr in letters:
        if (ltr in ascii_uppercase):
            upper_count += 1
        if (ltr in ascii_lowercase):
            lower_count += 1
        if (ltr in punctuation):
            punct_count += 1
    
    return (upper_count, lower_count, punct_count)


TEST_STRING: str = "Hello Mr. Rogers, how are you this fine Tuesday?"
UPPER, LOWER, PUNCT = count_chars(TEST_STRING)

print(f"Sample string: {TEST_STRING}")
print(f"Uppercases: {UPPER}")
print(f"Lowercases: {LOWER}")
print(f"Punctuations: {PUNCT}")


# Using lambda expression
# To get unique values, we use set(), then back to list
def unique_list(ls: List[Any]) -> List[Any]:
    """
    Get the unique elements from a list.

    Arguments:
        - `ls`: The list that we want to check the unique elements for.

    Return:
        - List of the unique elements in the list.
    """
    return list(set(ls))


test_list: List[int] = [1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]
uniques: List[int] = unique_list(test_list)
print(f"test_list: {test_list}")
print(f"uniques: {uniques}")


from functools import reduce

def multiply(numbers: List[int]) -> int:
    """
    Multiply all the numbers in a list.

    Arguments:
        - `numbers`: A list of numbers to multiply.

    Return:
        - Result of the multiplication.
    """

    return reduce(lambda agg, next: agg * next, numbers, 1)


multiply([1, 2, 3, -4])


def palindrome(st: str) -> bool:
    """
    Checks whether a passed string is a palindrome or not.

    Arguments:
        `st`: The string to check.

    Returns:
        Whether the passed string is palindrome or not.
    """
    
    # Consider alphanumeric characters only and compare at lower case
    st_clean: str = "".join([char.lower() for char in st if char.isalnum()])

    # Palindrome if the reverse is the same as the forward
    return st_clean == st_clean[::-1]


print(palindrome("nurses run"))
print(palindrome("madam"))
print(palindrome("abracadabra"))
print(palindrome("Al lets Della call Ed Stella"))
print(palindrome("Are we not pure? 'No, sir!' Panama’s moody Noriega brags. 'It is garbage!' Irony dooms a man—a prisoner up to new era."))


# In[ ]:


from string import ascii_lowercase

def is_pangram(st: str, alphabet: str = ascii_lowercase) -> bool:
    """
    Checks whether a passed string is a pangram or not.
    Pangrams are words or sentences containing every letter of the alphabet at least once.

    Arguments:
        - `st`: The string to check.
        - `alphabet` (optional): A list of alphabet to use. Defaults to `ascii_lowercase`.

    Returns:
        - Whether the passed string is a pangram or not
    """
    st_lower: str = st.lower() # compare at lowercases only
    return len(set(alphabet)) <= len(set(st_lower))


# In[ ]:


print(is_pangram("Jackdaws love my big sphinx of quartz"))
print(is_pangram("A quick brown fox jumps over the lazy dog"))
print(is_pangram("Hello World!"))


