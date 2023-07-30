#!/usr/bin/env python
# coding: utf-8

from io import StringIO

# Arbitrary String
message: str = "This is just a normal string."

# Use StringIO method to set as file object
f: StringIO = StringIO(message)

# Now we have an object `f` that we will be able to treat just like a file
print("f.read():", f.read())


# We can also write to it:
print("Writing to file...")
f.write("\nSecond line written to file-like object")

# Reset cursor just like you would a file
f.seek(0)
# Read again
print("f.read():", f.read())


