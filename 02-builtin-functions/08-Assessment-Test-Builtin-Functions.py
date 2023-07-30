#!/usr/bin/env python
# coding: utf-8

from functools import reduce
from typing import Any, Callable, List, Sequence, Tuple


word_lengths: Callable[[str], Tuple[int,...]] = lambda phrase: tuple(map(len, phrase.split())) # default split is @ (" ")
print("How long are the words in this phrase? ", end="")
print(word_lengths("How long are the words in this phrase"))


digits_2_num: Callable[[Sequence[int]],int] = lambda digits: reduce(lambda aggr, next: aggr * 10 + next, digits)

print("digits_2_num((3, 4, 3, 2, 1, 4, 5, 6, 7)) = ", end="")
print(digits_2_num((3, 4, 3, 2, 1, 4, 5, 6, 7)))


# Equivalent in using for-loop
tpl: Tuple[int,...] = (3, 4, 3, 2, 1, 4, 5, 6, 7)
num: int = 0

for n in tpl:
    num = num * 10 + n
    
print(num)


filter_words: Callable[[Sequence[str], str], filter] = lambda word_list, letter: filter(lambda word: str(word[0]).lower() == str(letter).lower() , word_list)

words = ("Hello","are","cat","dog","ham","Hi","go","to","heart")
print(tuple(filter_words(words,"h")))


concatenate: Callable[[Sequence[str], Sequence[str], str], Sequence[str]] = lambda L1, L2, connector: [f"{x}{connector}{y}" for x, y in zip(L1, L2)]
print("concatenate(['A','B'], ['a','b'], '-'):", concatenate(["A","B"],["a","b"],"-"))


d_list: Callable[[List[Any]], dict[Any, int]] = lambda el: { el_val: el_key for (el_key, el_val) in enumerate(el) }
print("d_list(['a', 'b', 'c']):", d_list(["a", "b", "c"]))


count_match_index: Callable[[List[Any]], int] = lambda L: len([x for (i, x) in enumerate(L) if x == i]) # Using list comprehension and conditioning
print("count_match_index([0, 2, 2, 1, 5, 5, 6, 10]):", count_match_index([0, 2, 2, 1, 5, 5, 6, 10]))


