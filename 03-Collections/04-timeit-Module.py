#!/usr/bin/env python
# coding: utf-8

import timeit


# Variable Assignment Hello World
timeit.timeit('x = "Hello World"', number=100000)


# Using For-Loop
def for_loop_generate(x: int) -> str:
    return "-".join(str(n) for n in range(x))


# Using List Comprehension
def list_comp_generate(x: int) -> str:
    return "-".join([str(n) for n in range(x)])


# Using map()
def map_generate(x: int) -> str:
    return "-".join(map(str, range(x)))


# For loop... Measuring
timeit.timeit('"-".join(str(n) for n in range(100))', number=100000)


# List comprehension... Measuring
timeit.timeit('"-".join([str(n) for n in range(100)])', number=100000)


# Map()... Measuring
timeit.timeit('"-".join(map(str, range(100)))', number=100000)


# Measuring Code runtime
import time

# Start timer
start_time: float = time.time()

for x in range(100000):
    _ = for_loop_generate(100)

# End timer
end_time: float = time.time()

# End timer
print("--- For Loops: Finished in {0} seconds ---".format(end_time - start_time))


# Start timer
start_time = time.time()

for x in range(100000):
    _ = list_comp_generate(100)

# End timer
end_time = time.time()

# End timer
print("--- List Comprehension: Finished in {0} seconds ---".format(end_time - start_time))


# Start timer
start_time = time.time()

for x in range(100000):
    _ = map_generate(100)

# End timer
end_time = time.time()

# End timer
print("--- map(): Finished in {0} seconds ---".format(end_time - start_time))


