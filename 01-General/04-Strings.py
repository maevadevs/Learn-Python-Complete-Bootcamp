#!/usr/bin/env python
# coding: utf-8

# Single quotes word, equivalent to double-quotes
print('Hello!')

# Double quotes word, equivalent to single-quotes
print("Hello!")


from typing import Final

# Entire phrase
PHRASE: Final[str] = "This is also a string"
print(PHRASE)


from typing import Final

# Multi-line and pre-formatted strings
MULTILINE: Final[str] = """\
This is a multi-line string.
    These strings are typically used for docstring.
    They are preformatted and maintain their format.\
"""
print(MULTILINE)


from typing import Final

# Be careful with quotes: Escape or Nest
# phrase_2 = 'I'm using single quotes, but will create an error'
PHRASE_3: Final[str] = "I\'m using single quotes, and this one works fine"
PHRASE_4: Final[str] = "Now I'm ready to use the single quotes ' inside a double-quoted string!"
print(PHRASE_3)
print(PHRASE_4)


from typing import Final

# Raw String
# No special-processing and escaping are applied
RAW_STRING: Final[str] = r"This is a raw string.\nNo escape is applied.\nEverything is 'as-is'."
print(RAW_STRING)


# Using print() function for output
print("Hello World!")
print("Use \\n \nto print a new line")
print("\n")
print("See what I mean?")
print("\nHere is \t also a tabbed \t line using \\t")


# Length of a string
print(len("Hello World"))


from typing import Final

# Assign ST as a string
ST: Final[str] = "Hello World"
print(ST)


# First element
print(ST[0])


# Second element
print(ST[1])


# Third element
print(ST[2])


# Grab everything from the second term all the way to the end of st which, is len(s)
print(ST[1:])


# Original string: No changes
print(ST)


# Grab everything UP TO the 3rd index, EXCLUSIVE
print(ST[:3])


# Grab everything
print(ST[:])


# Last letter (one index behind `0`, so it loops back around)
print(ST[-1])


# Grab everything, EXCEPT the last two letters
print(ST[:-2])


# Grab everything, go in step size of 1 (Default)
print(ST[::])


# Grab everything, but go in step size of 2
print(ST[::2])


# Printing a string backward
print(ST[::-1])


st: str = "hello"
print(st)


# st[0] = "x" # => TypeError: "str" object does not support item assignment


# Re-assigning a string as a whole
st = "x"
print(st)


# Re-assigning again
st = "Hello World"
print(st)


from typing import Final

# Concatenating 2 strings
X: Final[str] = "Hello, "
Y: Final[str] = "world"
st = X + Y
print(st)


# Concatenate strings!
print(st + " concatenate me!")


# Again, we can reassign str completely (Creating a new value)!
st += " concatenate me me me!"
print(st)


print("z" * 10 + "!") 


print("Hello World!" * 5)


# Here is our original test string
st = "Test string"


print(st.upper())


# And the original is... Unchanged!
print(st)


print(st.lower())


# And the original is... Unchanged!
print(st)


print(st.split())


# Splitting on t's instead
print(st.split(sep="t"))


# The sep argument can be passed without a name
print(st.split("t"))


# Using str.format()
st1: str = "Insert another string with curly brackets: {}"
st2: str = st1.format("The inserted string. And a value {}.")
print(st2.format(1 + 2 + 3))


# We can let the position determine the order
print("The {} {} {}".format("fox", "brown", "quick"))


# Or we can use numbered indexes
print("The {2} {1} {0}".format("fox", "brown", "quick"))


# Or we can use named indexes
print("The {q} {b} {f}".format(f="fox", b="brown", q="quick"))


from typing import Final

RESULT: Final[float] = 100 / 777

print("The result was {}".format(RESULT))
print("The result was {r}".format(r=RESULT))
print("The result was {r:0.5f}".format(r=RESULT)) # => {value:width.precision f}
print("The result was {r:10.5f}".format(r=RESULT)) # => {value:width.precision f}, width adds whitespaces


AGE: int = 18
print(f"Using f-string: The result was {RESULT:0.3f}, and the age was {AGE}.")


# Concatenate the strings in the list with a "-" as a separator
print("-".join(["This","is","a","simple","Hello","World","!"]))


