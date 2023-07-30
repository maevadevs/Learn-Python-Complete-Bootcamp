#!/usr/bin/env python
# coding: utf-8

from typing import Generator, Iterator, List


def generate_cubes(n: int) -> Generator[int, None, None]:
    for num in range(n):
        yield num ** 3


print(type(generate_cubes))
print(type(generate_cubes(3)))
print(generate_cubes(3))


ls: list[int] = []

for x in generate_cubes(10):
    ls.append(x)

print(", ".join(map(str, ls)))


def gen_fibonacci(n: int) -> Generator[int, None, None]:
    """
    Generate a fibonacci sequence up to n.
    """
    a = 1
    b = 1

    for i in range(n):
        yield a
        a, b = b, a + b


print([num for num in gen_fibonacci(50)])


# Equivalent Normal Function
def fibonacci(n: int) -> List[int]:
    a = 1
    b = 1
    output: List[int] = []

    for _ in range(n):
        output.append(a)
        a, b = b, a + b
        
    return output


print(fibonacci(50))


def simple_generator() -> Generator[int, None, None]:
    for x in range(5):
        yield x


# Assign simple_gen
gen: Generator[int, None, None] = simple_generator()

print(next(gen), end = " ")
print(next(gen), end = " ")
print(next(gen), end = " ")
print(next(gen), end = " ")
print(next(gen), end = " ")
#print(next(gen), end = " ") # StopIteration


st: str = "hello"

# Iterate over string
print([letter for letter in st])

# Try to use as an iterator
# print(next(s)) # TypeError: Not iterator


# Convert st into an iterator, because we cannot use next(st) directly
st_iterator: Iterator[str] = iter(st)

print(next(st_iterator), end = " ") # Now use next(st)
print(next(st_iterator), end = " ")
print(next(st_iterator), end = " ")
print(next(st_iterator), end = " ")
print(next(st_iterator), end = " ")
#print(next(st_iterator), end = " ") # StopIteration


# Generator comprehension
generator: Generator[int, None, None] = (n for n in range(3, 5))

print(next(generator), end = " ")
print(next(generator), end = " ")
# print(next(generator), end = " ") # StopIteration Error


my_greeting: str = "Hello"
my_greeting_generator: Generator[str, None, None] = (ch for ch in my_greeting)

print(next(my_greeting_generator), end = " ")
print(next(my_greeting_generator), end = " ")
print(next(my_greeting_generator), end = " ")
print(next(my_greeting_generator), end = " ")
print(next(my_greeting_generator), end = " ")
#print(next(my_greeting_generator), end = " ") # StopIteration


