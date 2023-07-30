#!/usr/bin/env python
# coding: utf-8

from typing import List


st: str = "Print only the words that Start with s in this sentence"


# Code here: List Comprehension
word_list: List[str] = st.split(" ")
words_with_s: List[str] = [word for word in word_list if (word[0].lower() == "s")]
print(words_with_s)


my_list: List[int] = [x for x in range(0, 11, 2)]
print(my_list)


print([num for num in range(1, 50+1) if num % 3 == 0])


st = "Print every word in this sentence that has an even number of letters"


for word in st.split(" "):
    if (len(word) % 2 == 0):
        print(word + "\t\t: even")
    else:
        print(word + "\t\t: odd")


lst: List[str] = [word + "\t: odd" if len(word) % 2 == 0 else word + "\t: even" for word in str.split(" ")]
for el in lst:
    print(el)


# Code in this cell
for x in range(1, 101):
    if (x % 3 == 0 and x % 5 == 0): #multiple of both 3 and 5
        print("FizzBuzz")
    elif x % 3 == 0: #multiple of 3 only
        print("Fizz")
    elif x % 5 == 0: #multiple of 5 only
        print("Buzz")
    else:
        print(x)


st = "Create a list of the First Letters of every word in this string"


first_words: List[str] = [x[0] for x in st.split()]
print(first_words)


