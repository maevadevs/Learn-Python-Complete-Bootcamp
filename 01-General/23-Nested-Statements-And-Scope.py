#!/usr/bin/env python
# coding: utf-8

from typing import Any, Callable, List


x: int = 25

def printer() -> int:
    x: int = 50
    return x

print(f"This grabs the global variable: {x}")
print(f"This grabs the local variable: {printer()}")


# x is local here: lambda act as a function
x = 25
func: Callable[[int], int] = lambda x: x**2
func(3)


name: str = "This is a global name"

def greet() -> None: # Enclosing function
    name: str = "Sammy" # This name is local to greet()
  
    def hello() -> None: 
        # Enclosed function
        print(f"Hello {name}")
    
    hello() # Calling greet() will eventually call hello() here


# hello() # hello() is not defined in this scope. This is an error
greet() # 


print(name) # global


def func2(x: int) -> None:
    # Globals can be used in function as passed parameters if no local is declared yet
    print("x is", x)
    # But locals would take precedence once present
    x = 2
    print("Changed local x to", x)
    print("Now x is", x)


x = 50
func2(x)
print("x global is still", x)


x = 100 # This is global x

def func3():
    global x # This x refers to the x defined outside
    print("This function is now using the global x!")
    print("Because of global, x is:", x)
    x = 2 # This is global x: We cannot shadow to local
    print("Ran func(), changed global x to", x)


print("Before calling func(), x is:", x)
print("-----")
func3()
print("-----")
print("Value of x (outside of func()) is:", x)


loc: dict[str, Any] = locals()
loc_keys: List[str] = []

for k in list(loc.keys()):
    loc_keys.append(k)

print(sorted(loc_keys))


glob: dict[str, Any] = globals()
glob_keys: List[str] = []

for k in glob.keys():
    glob_keys.append(k)

print(sorted(glob_keys))


