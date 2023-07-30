#!/usr/bin/env python
# coding: utf-8

# The most basic example of a print statement
print("This is a string")


# Using % formatter
st: str = "STRING"
print("Place another string with a mod and s: %s" % (st))


# Using .format()
print("Place another string with a mod and s: {:s}".format(st))


# Using f-string
print(f"Place another string with a mod and s: {st:s}")


# Using % formatter
print("Floating point numbers: %1.2f" % (13.144))
print("Floating point numbers: %1.0f" % (13.144))
print("Floating point numbers: %1.5f" % (13.144))
print("Floating point numbers: %10.2f" % (13.144))
print("Floating point numbers: %25.2f" % (13.144))


# Using .format()
print("Floating point numbers: {:1.2f}".format(13.144))
print("Floating point numbers: {:1.0f}".format(13.144))
print("Floating point numbers: {:1.5f}".format(13.144))
print("Floating point numbers: {:10.2f}".format(13.144))
print("Floating point numbers: {:25.2f}".format(13.144))


# Using f-string
print(f"Floating point numbers: {13.144:1.2f}")
print(f"Floating point numbers: {13.144:1.0f}")
print(f"Floating point numbers: {13.144:1.5f}")
print(f"Floating point numbers: {13.144:10.2f}")
print(f"Floating point numbers: {13.144:25.2f}")


# Using % formatter
print("Here is a number: %s. Here is a string: %s" % (123.1,"hi"))
print("Here is a number: %r. Here is a string: %r" % (123.1,"hi"))


# Using .format(): Implicit conversion to str. Use repr() if needed
print("Here is a number: {0}. Here is a string: {1}".format(123.1,"hi"))
print("Here is a number: {0}. Here is a string: {1}".format(repr(123.1), repr("hi")))


# Using f-string: Implicit conversion to str. Use repr() if needed
# String expressions inside f-string must use the opposite quote
print(f"Here is a number: {123.1}. Here is a string: {'hi'}")
print(f"Here is a number: {repr(123.1)}. Here is a string: {repr('hi')}")


# Using % formatter
print("First: %s, Second: %1.2f, Third: %r" % ("hi!", 3.14, 22))


# Using .format()
print("First: {}, Second: {:1.2f}, Third: {}".format("hi!", 3.14, 22))


# Using .format()
print(f"First: {'hi!'}, Second: {3.14:1.2f}, Third: {22}")


# Implicitly insert in order
print("This is a string with an {}".format("insert"))
# No equivalent for f-string


# Explicitly insert by placeholder order
print("This is a string with an {0}".format("insert"))
# No equivalent for f-string


# Explicitly insert by variable name
print("This is a string with an {p}".format(p="insert"))
p: str = "insert"
print(f"This is a string with an {p}")


# We can insert multiple times
print("One: {0}, Two: {0}, Three: {0}".format("Hi!"))
val: str = "Hi!"
print(f"One: {val}, Two: {val}, Three: {val}")


# We can also insert multiple times using variable names
print("One: {p}, Two: {p}, Three: {p}".format(p="Hi!"))
p = "Hi!"
print(f"One: {p}, Two: {p}, Three: {p}")


# Several Objects, and using formatter
print("Object 1: {a}, Object 2: {b}, Object 3: {c:0.2f}".format(a=repr(1), b="two", c=12.3))
a: str = repr(1)
b: str = "two"
c: float = 12.3
print(f"Object 1: {a}, Object 2: {b}, Object 3: {c:0.2f}")


