#!/usr/bin/env python
# coding: utf-8

def convert_integer(x: int, to: str = "bin") -> str:
    
    # Exception handling: x must be an integer
    if (not isinstance(x, int)):
        raise TypeError("Cannot convert non-integer values.")
    
    # Exception handling: to must be in ("bin", "hex")
    if (to not in ("bin", "hex")):
        raise ValueError("The 'to' argument is not valid.")

    res: str
    
    # Normal scenario
    if (to == "bin"):
        res = bin(x)

    if (to == "hex"):
        res = hex(x)
    
    return res


print("convert_integer(1024:", convert_integer(1024))
print("convert_integer(integer, to=\"hex\"):", convert_integer(1024, to="hex"))


def round_number(x: float, precision: int = 2) -> float:
    
    # Exception handling: x must a number
    if not (
        isinstance(x, int) 
        or isinstance(x, float) 
        or isinstance(float(x), float)
    ):
        raise TypeError("Cannot convert non-numeric values.")

    # Normal Scenario
    return round(x, precision)


print("round_number(5.23222):", round_number(5.23222))
print("round_number(5.23222, 4):", round_number(5.23222, 4))
print("round_number('5.23222'):", round_number(float("5.23222")))
print("round_number('100'):", round_number(float("100")))


st: str = "hello how are you Mary, are you feeling okay?"
print("str.islower()?", st.islower())


st = "twywywtwywbwhsjhwuwshshwuwwwjdjdid"
print("str.count('w'):", st.count("w"))


set1: set[int] = {2,3,1,5,6,8}
set2: set[int] = {3,1,7,5,6,8}

print("set1:", set1)
print("set2:", set2)
print("set1.difference(set2):", set1.difference(set2))


print("set1.union(set2):", set1.union(set2))


# Intersection
print("set1.intersection(set2):", set1.intersection(set2))


d: dict[int, int] = {x: x**3 for x in range(5)}
print("dict cubes using comprehension:", d)


lst: list[int] = [1,2,3,4]
print("lst:", lst)
lst.reverse()
print("lst.reverse()", lst)


lst = [3,4,2,5,1]
print("lst:", lst)
lst.sort()
print("lst.sort()", lst)


