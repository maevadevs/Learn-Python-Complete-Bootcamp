#!/usr/bin/env python
# coding: utf-8

from typing import Final

A: Final[int] = -9     # Base 10, Negatives Integer
B: Final[int] = 50     # Base 10, Positives Integer
C: Final[int] = 0x4F   # Hexadecimals
D: Final[int] = 0o77   # Octal
E: Final[int] = 0b1101 # Binary

print("Negative Integer:", A)
print("Positive Integer:", B)
print("Hexadecimal:", C)
print("Octal:", D)
print("Binary:", E)


from typing import Final

F: Final[float] = -25.45       # Base 10, Negative Float
G: Final[float] = 17.4         # Base 10, Positive Float
H: Final[float] = 17.045e-10   # Base 10, Scientific Notation

print("Negative Float:", F)
print("Positive Float:", G)
print("Scientific Notation:", H)


from typing import Final

I: Final[bool] = True
J: Final[bool] = False

print(I)
print(J)


from typing import Final

K: Final[str] = 'Hello World' # Single Quotes
L: Final[str] = "Hello World" # Double Quotes
M: Final[str] = 'C' # Single Character, Single Quotes
N: Final[str] = "y" # Single Character, Double Quotes

print(K)
print(L)
print(M)
print(N)


from typing import Any, List, Final

A_LIST: Final[List[Any]] = ["a", "b", "c", 1, 2, 3.4, True, False, {}, [], (), 1, 0] # True and False same as 1 and 0
print(A_LIST)


from typing import Final, Tuple

A_TUPLE: Final[Tuple[int,...]] = (1, 2, 3) # With parenthesis
B_TUPLE: Final[Tuple[str,int,bool]] = "a", 200, True # Without parenthesis

print(A_TUPLE)
print(B_TUPLE)


from typing import Dict, Final

# Strings as keys
STRING_DICT: Final[Dict[str, str]]  = { 
    "fname": "John", 
    "lname": "Doe" 
}

# Integers as keys
NUM_DICT: Final[Dict[int, str]] = { 
    1: "Mary", 
    2: "John", 
    3: "Sally" 
}

print("string_dict:", STRING_DICT)
print("num_dict:", NUM_DICT)


# Library for working with complex numbers
from cmath import phase
from typing import Final

CP: Final[complex] = complex(5,4)

print(CP)
print(f"Real Portion: {CP.real}")
print(f"Imaginary Portion: {CP.imag}")
print(f"Conjugate: {CP.conjugate()}")
print(f"Phase: {phase(CP)}")


from typing import Final, Iterable

RG: Final[Iterable[int]] = range(5)
print(type(RG))

for num in RG:
    print(num, end=" ")


for i, num in enumerate(range(10, 20+1, 2)):
    print(i+1, ":", num)


from typing import Final

X: Final[set] = set()

X.add(11)
X.add(12)
X.add(13)
X.add(12)
X.add(11)

print(X)


from typing import Final

Y: Final[frozenset[int]] = frozenset({11, 12, 13, 12, 11})

print(Y)


from typing import Final

# String to byte
BTS_STR: Final[bytes] = bytes("Python is interesting", encoding="utf-8")
print(BTS_STR)

# Int to byte
BTS_INT: Final[bytes] = bytes(10)
print(BTS_INT)

# List of int or bool to byte
BTS_LST: Final[bytes] = bytes([1, 2, 3, 4, 5])
print(BTS_LST)


from typing import Final

# String to bytearray
BTARR_STR: Final[bytearray] = bytearray("Python is interesting", encoding="utf-8")
print(BTARR_STR)

# Int to bytearray
BTARR_INT: Final[bytearray] = bytearray(10)
print(BTARR_INT)

# List of int or bool to bytearray
BTARR_LST: Final[bytearray] = bytearray([1, 2, 3, 4, 5])
print(BTARR_LST)


from typing import Final, List

LS: Final[List[int]] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
MV: Final[memoryview] = memoryview(bytearray(LS))

print(MV[0])
print(bytes(MV[0:5]))
print(list(MV[5:10]))


byte_array: bytearray = bytearray("ABC", "utf-8")
print("Before update:", byte_array)

mv: memoryview = memoryview(byte_array)
# update 1st index of mv to Z
mv[1] = 90
print("After update:", byte_array)


