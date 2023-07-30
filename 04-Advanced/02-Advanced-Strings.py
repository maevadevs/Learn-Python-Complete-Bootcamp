#!/usr/bin/env python
# coding: utf-8

string: str = "hello world! how's everyone doing today?..."


# Capitalize the very first word in string
print("string.capitalize():", string.capitalize())

# Uppercase all letters
print("string.upper():", string.upper())

# Lowercase all letters
print("string.lower():", string.lower())

# Make into a title format
print("string.title():", string.title())


print("string.count('o'):", string.count("o"))
print("string.find('o'):", string.find("o"))


print("\"hello\\thi\".expandtabs():", "hello\thi".expandtabs()) # Similar to print("hello\thi")


str1: str = "hello"
str2: str = "%^&"

# `isalnum()` will return True if all characters in string are alphanumeric
print("str1.isalnum():", str1.isalnum())
print("str2.isalnum():", str2.isalnum())


# `isalpha()` wil return True if all characters in string are alphabetic
print("str1.isalpha():", str1.isalpha())
print("str2.isalpha():", str2.isalpha())


# `islower()` will return True if all cased characters in string are lowercase and there is
# at least one cased character in string, False otherwise.
print("str1.islower():", str1.islower())


# `isspace()` will return True if all characters in string are whitespace
print("str2.isspace():", str2.isspace())


# `istitle()` will return True if str is a title-cased string and there is at least one character in str,
# i.e. uppercase characters may only follow uncased characters and lowercase characters only cased ones.
# Return False otherwise.
print("str1.istitle():", str1.istitle())
str3: str = "hello world! how are you doing today?".title()
print("str3.istitle():", str3.istitle())


# `isupper()` will return True if all cased characters in string are uppercase and there is
# at least one cased character in S, False otherwise.
print("str3.isupper():", str3.isupper())


# Another method is `endswith()` which is essentially the same as a boolean check on `s[-1]` but flexible
print("str1.endswith(\"lo\"):", str1.endswith("lo"))
print("str3.endswith(\"lo\"):", str3.endswith("lo"))


print("str1[-1] == 'o':", str1[-1] == "o")
print("str3[-1] == 'o':", str3[-1] == "o")


print("str3.split('e'):", str3.split("e"))
print("str3.partition('l'):", str3.partition("l")) # Only applies at the first instance


