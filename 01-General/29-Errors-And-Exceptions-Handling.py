#!/usr/bin/env python
# coding: utf-8

from os import path
from pathlib import Path
from io import TextIOWrapper

root: Path = Path().absolute()

try:
    f: TextIOWrapper = open(path.join(root, "..", "demofiles", "testfile3.txt"))
    f.write("Test write this")
except FileNotFoundError:
    # This will only check for an FileNotFoundError exception and then execute this print statement
    print("Error: Could not find file testfile3.txt or read data")
else:
    print("Content written successfully")
    f.close()


# We did not have write permission (opening only with "r")
try:
    f2: TextIOWrapper = open(path.join(root, "..", "demofiles", "testfile3.txt"), mode = "r")
    f2.write("Test write this")
except IOError:
    # This will only check for an IOError exception and then execute this print statement
    print("Error: Could not find file testfile3.txt or read data")
else:
    print("Content written successfully")
    f2.close()
    
print("Hey, I am still printing even though there was an error.")


try:
    f3: TextIOWrapper = open(path.join(root, "..", "demofiles", "testfile3.txt"), mode = "r")
    f3.write("Test write this")
except:
    # This will check for any exception and then excute this print statement
    print("Error: Could not find file testfile3.txt or read data")
else:
    print("Content written successfully")
    f3.close()


try:
    f4: TextIOWrapper = open(path.join(root, "..", "demofiles", "testfile3.txt"), mode = "r")
    f4.write("Test write statement")
except:
    print("An error occurred.")
else:
    print("success")
finally:
    print("Always execute finally code blocks.")


def ask_int() -> None:
    while True:
        try:
            val: int = int(input("Please enter an integer: "))
        except:
            print("Looks like you did not enter an integer! Please try again.")
            continue # Go back to the loop
        else:
            print("Yep that's an integer!" + f"\nYou entered {val}")
            break # Only break when we get an integer
        finally:
            print("Finally, I executed!")


ask_int()


def ask_int_again() -> None:
    try:
        val: int = int(input("Please enter an integer: "))
        print(val)
    except Exception as e:
        print("Oops! There was an error: " + str(e))
    finally:
        print("Finally, I executed!")


ask_int_again()


