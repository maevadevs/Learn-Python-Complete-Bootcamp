#!/usr/bin/env python
# coding: utf-8

from typing import Callable, Optional


s: str = "A sample Global Variable"

def func() -> None:
    print(locals())

func()


print(globals().keys())


print(globals()["s"])


def say_hello(name: Optional[str] = "Anonymous") -> str:
    return f"Hello {name}"

print(say_hello())


greet: Callable = say_hello # Assigning a function to a variable
print(type(greet))
greet()


del say_hello
greet() # Still works even if say_hello() was deleted: Copied by value


def hello(name: str = "Anonymous") -> None:
    print("The hello() function has been executed.")

    def greet() -> str:
        return "\tThis is from the inside of the greet() function"

    def welcome() -> str:
        return "\tThis is from the inside of the welcome() function"

    print(greet())
    print(welcome())
    print("Now we are back inside the hello() function")

hello()


def hello_again(name: str = "Anonymous") -> Callable[[], str]:
    def greet() -> str:
        return "\tThis is inside the greet() function"

    def welcome() -> str:
        return "\tThis is inside the welcome() function"

    if name == "Anonymous":
        return greet  # A function object
    else:
        return welcome  # A function object


my_value: Callable[[], str] = hello_again()
print(type(my_value))
print(my_value())


del hello_again
my_value()


def hello2() -> str:
    return "Hello!"

def other(func: Callable) -> None:
    print("Other code would go here")
    print(func())
    print("Other code would go here")


other(hello2)


def my_decorator(func: Callable) -> Callable:
    def wrap_func() -> None:
        print("<This is a decoration from the decorator>")
        func()
        print("</This is a decoration from the decorator>")

    return wrap_func

def needs_decorator() -> None:
    print("This is from inside the function argument.")


needs_decorator()


# Right way to call a decorator
@my_decorator
def needs_decorator2():
    print("This is from inside the function argument.")


needs_decorator2()


