#!/usr/bin/env python
# coding: utf-8

from pathlib import Path
from os import path
from typing import Final, TextIO


ROOT: Final[Path] = Path().absolute()


# Open the testfile.txt we made earlier
MY_FILE: Final[TextIO] = open(path.join(ROOT, '..', 'demofiles', 'testfile1.txt'), encoding='utf8')


# We can now read the file: Seek to the beginning
MY_FILE.seek(0)


# Then start reading. Capture in a variable
CONTENTS: Final[str] = MY_FILE.read()
print(f'Reading the content of textfile1.txt: {CONTENTS}')


# But what happens if we try to read it again?
print(MY_FILE.read())


# Reset: Seek to the start of file (index 0)
MY_FILE.seek(0)


# Now read again
print(f'Reading textfile1.txt one more time: {MY_FILE.read()}')


MY_FILE.seek(0)
# Readlines returns a list of the lines in the file
print(f'Using readlines() to get each line: {MY_FILE.readlines()}')


MY_FILE.seek(0)

for line in MY_FILE.readlines():
    print(line, end="")


# Close the file when done
MY_FILE.close()


contents: str

with open(path.join(ROOT, '..', 'demofiles', 'testfile1.txt'), encoding='utf8') as my_new_file:
    contents = my_new_file.read()

print('Using the `with` keyword:')
print(contents)


my_file: TextIO

with open(path.join(ROOT, '..', 'demofiles', 'testfile2.txt'), mode='w+', encoding='utf8') as my_file:
    
    # Now write to the file (Overwrite)
    my_file.write('\nThis is a newly added line using w+')
    
    # Read the file
    my_file.seek(0)
    print(my_file.read())
    
    # Add another write
    my_file.write('\nThis is a second line')
    my_file.write('\nThis is a third line')
    my_file.write('\nThis is a fourth line')
    my_file.write('\nThis is a fifth line')
    
    # Read the file again
    my_file.seek(0)
    print(my_file.read())


for num, line in enumerate(open(path.join(ROOT, '..', 'demofiles', 'testfile2.txt'))):
    print(f'Line {num+1}: {line}')


