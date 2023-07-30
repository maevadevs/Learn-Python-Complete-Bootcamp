#!/usr/bin/env python
# coding: utf-8

import re

# List of patterns to search for
patterns: list[str] = ["term1", "term2"]

# Text to parse
text: str = "This is a string with term1, but it does not have the other term."

for pattern_to_search in patterns:
    print(f"Searching for {pattern_to_search} in: {text}\n...")

    # Check for match: re.search(pattern, text)
    if re.search(pattern_to_search, text):
        print("Match was found: ")
        print(re.search(pattern_to_search, text))
        print("-" * 75)
    else:
        print("No Match was found: ")
        print(re.search(pattern_to_search, text))
        print("-" * 75)


import re
from re import Match
from typing import Optional

# List of patterns to search for
ptrn: str = "term1"

# Text to parse
text = "This is a string with term1, but it does not have the other term."

match: Optional[Match[str]] = re.search(ptrn, text)
print(type(match))


help(match)


if match:
    # Show start of match
    print(match.start())

    # Show end
    print(match.end())


# Term to split on
split_at_term: str = " "  # Each space
phrase: str = "What is the domain name of someone with the email: hello@gmail.com"

# Split the phrase
print(re.split(split_at_term, phrase))


print(phrase.split(split_at_term))


# Returns a list of all matches
cases: list[str] = re.findall("match", "test phrase match is in middle and match is close to the end.")
print(cases)


# Function to count the appearance of a specific text within a long string
def count_appearance_in_text(to_find: str, long_text: str) -> int:
    return len(re.findall(to_find, long_text))

to_find = "match"
text = "test phrase match is in middle and match is close to the end. And here are more match, match, match!! math!"
print("match", count_appearance_in_text(to_find, text))


def multi_re_find(patterns: list[str], phrase: str) -> None:
    """Takes in a list of regex patterns and prints a list of all matches.

    Args:
        `patterns`: A list of regex patterns.
        `phrase`: A list of all the matches.

    Returns:
        - `None`
    """
    
    for pattern in patterns:
        print(f"Searching the phrase using the re check: {pattern}")
        print(re.findall(pattern, phrase))
        print("\n")


test_phrase: str = "sdsd..sssddd...sdddsddd...dsdds...dsssss...sddddddd"
test_patterns: list[str] = [
    "sd*",      # s followed by zero or more d's: [0, ...]
    "sd+",      # s followed by one or more d's: [1, ...]
    "sd?",      # s followed by zero or one d's: [0, 1]
    "sd{3}",    # s followed by n d's: [n]
    "sd{2,3}",  # s followed by m to n d's: [m, n]
    "sd{3,}",   # s followed by m or more d's: [m, ...]
    "sd{,3}",   # s followed by zero or at most m d's: [0, ..., m]
]

multi_re_find(test_patterns, test_phrase)


test_phrase = "sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd"
test_patterns = [
    "[sd]",     # either s or d
    "s[sd]+"    # s followed by one or more s or d
]

multi_re_find(test_patterns, test_phrase)


test_phrase = "This is a string! But it has punctuation. How can we remove them?"
test_patterns = ["[^!.? ]+"]
multi_re_find(test_patterns, test_phrase)


test_phrase = "ThiS is an exAmple senTence. Lets sEe if we can fInd soMe letters."
test_patterns = [
    "[a-z]+",  # sequences of lower case letters
    "[A-Z]+",  # sequences of upper case letters
    "[a-zA-Z]+",  # sequences of lower or upper case letters
    "[A-Z][a-z]+" # one upper case letter followed by lower case letters
]

multi_re_find(test_patterns, test_phrase)


test_phrase = "This is a string with some numbers 1233 and a symbol #hashtag"
test_patterns = [
    r"\d+",  # sequence of digits
    r"\D+",  # sequence of non-digits
    r"\s+",  # sequence of whitespace
    r"\S+",  # sequence of non-whitespace
    r"\w+",  # alphanumeric characters
    r"\W+",  # non-alphanumeric
]

multi_re_find(test_patterns, test_phrase)


