#!/usr/bin/env python
# coding: utf-8

from typing import (
    Any, 
    Final, 
    Generator, 
    List, 
    Optional,
    Tuple
)


def name_of_function(arg1: Any, arg2: Any) -> None:
    """
    This is where the function"s Document String (docstring) goes.
    
    Docstring explains about the function and will be showed when using `help()`.
    Type annotation of arguments can be ommitted if using _PEP 484: 
    https://www.python.org/dev/peps/pep-0484/
    
    Arguments:
        - `arg1`: The first argument.
        - `arg2`: The second argument.
    
    Return:
        The returned result.
    """
    
    # Do stuff here within the function
    # return desired result
    return None


help(name_of_function)


# Example 1: A simple print "hello" function
def say_hello() -> None:
    """
    Print "hello" in the console.
    """
    
    print("hello")


# Now, call the function
say_hello()


# Example 2: A simple greeting function
# Let"s write a function that greets people with their name.
def greeting(name: str) -> None:
    """
    Print name in the console.

    Arguments:
        - `name`: The name to be printed.
    """
    
    print("Hello, {0}!".format(name))


greeting("John")


# Example 3: A simple create_greeting function
# Let"s write a function that creates a greeting from people"s name.
def create_greeting(name: str) -> str:
    """
    Create a greeting with a given name.

    Arguments:
        - `name`: The name to be greeted.

    Return:
        - The greeting string.
    """
    
    return "Hello, {0}!".format(name)


GREETING: Final[str] = create_greeting(name="John")
print(GREETING)


# Example 3: Addition function
def add(num_1: int|float, num_2: int|float) -> int|float:
    """
    Add two numbers and return the result.

    Arguments:
        - `num_1`: The first operand.
        - `num_2`: The second operand.

    Return:
        - The result of the addition.
    """
    
    return num_1 + num_2


print(add(456, 654))


RESULT: Final[int|float] = add(4, 5)
print(RESULT)


# What happens if we input two strings?
# print(add("one","two")) # This will throw an error when using mypy


def is_prime_naive(num: int) -> bool:
    """
    Very naive method for verifiying that a number is prime.

    Arguments:
        - `num`: The number to check if it is prime or not.

    Return:
        - True if `num` is prime. False otherwise.
    """
    
    if num < 2:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
    
    return True


print(is_prime_naive(21079))


import math

def is_prime_semi_naive(num: int) -> bool:
    """
    Semi-naive method for verifiying that a number is prime. 
    Using only up to the square root of the number and exclude by default all even numbers.

    Arguments:
        - `num`: The number to check if it is prime or not.

    Return:
        - True if `num` is prime. False otherwise.
    """
    
    if num < 2:
        return False

    if num == 2:
        return True

    if num % 2 == 0 and num > 2: 
        return False

    for i in range(3, int(math.sqrt(num)) + 1, 2): # range() for python3
        if num % i == 0:
            return False

    return True


print(is_prime_semi_naive(21079))


from math import sqrt

def is_prime(num: int) -> Tuple[bool, Optional[int]]:
    """   
    Optimised method for checking if an integer number is prime or not.
    Also returning the found smallest divisor if the number is not prime.

    Arguments:
        - `num`: The number to check if it is prime or not.

    Return:
        - Whether the `num` is prime or not, and the found smallest divisor if not prime.
    """

    # Special cases
    if type(num) != int or num <= 1:
        raise Exception(f"Argument 'num' must be of type {type(1)} and value > 1.\nInstead, received type {type(num)} and value {num}.")

    # First 4 prime numbers
    if num in (2, 3, 5, 7):
        return True, None

    # Divisible by 2
    if num % 2 == 0:
        return False, 2

    # Divisible by 5
    if num % 5 == 0:
        return False, 5

    # Beyond 10, only integers ending in 1,3,7,9 can be prime
    # Else, they are either divisible by 2 or 5
    if num % 10 in (1,3,7,9):
        # Loop through possible divisors up to the sqrt
        for n in range(3, int(sqrt(num))+1):
            if num % n == 0:
                return False, n

    # If still here then prime
    return True, None


print(is_prime(21079))


def generate_top_primes(n: int) -> List[int]:
    """
    Generate a list of n-primes, using while loop.

    Arguments:
        - `n`: The number of prime numbers to generate

    Return:
        - List of `n` prime numbers
    """

    def _generator(limit: int) -> Generator[int, None, None]:
        num = 2
        countPrimes = 0
        while countPrimes < limit:
            if is_prime(num)[0]:
                yield num
                countPrimes += 1
            num += 1
    
    # Return the final list using the generator
    return [num for num in _generator(n)]


# Measuring Code runtime
import time

# Start timer
start_time: float = time.time()
primes: List[int] = generate_top_primes(10000)
# End timer
print("--- Finished in {0} seconds ---".format(time.time() - start_time))
#print(p)


# We could also use filter and range
# This is way faster than previous method
def primes_up_to(x: int) -> List[int]:
    """
    Better way to list the first x number of primes, using range() and filter().
    """
    return list(filter(is_prime, range(2, x)))


# Measuring Code runtime
import time
# Start timer
start_time = time.time()
primes = primes_up_to(10000)
# End timer
print("--- Finished in {0} seconds ---".format(time.time() - start_time))
#print(p)


def my_sum(*args: int|float) -> int|float:
    return sum(args) # args is a tuple

print(my_sum(4, 5, 6.7, 7, 8, 9.6))
print(my_sum(4, 5))
print(my_sum(40, 50, 60))


def my_func(**kwargs: str) -> None:
    if "fruit" in kwargs:
        print(f"Fruit is present as {kwargs['fruit']}")
    else:
        print("No fruit found")

my_func(animal="lion", vegetable="carrot", fruit="apple")


def another_func(*args: Any, **kwargs: str) -> None:
    print("args:", args)
    print("kwargs:", kwargs)
    print(f"I would like {args[0]} {kwargs['food']}")

another_func(10, 30, 4, "John", food="eggs", non_food="plastic")


