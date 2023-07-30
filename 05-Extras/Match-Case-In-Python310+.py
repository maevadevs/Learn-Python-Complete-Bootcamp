#!/usr/bin/env python
# coding: utf-8

from inspect import currentframe
from sys import version_info as pyver

def weekday_greeting(day: str) -> str:    
    """Allows to select a greeting based on the day of the week passed.

    This function currently only supports Python 3.10+.
    For older version, an exception is raised.
    
    Args:
        - `day` (`str`): The day of the week. 
            Use one of the following value (`"mon"`,`"tue"`,`"wed"`,`"thu"`,`"fri"`,`"sat"`,`"sun"`). 
            If the day is not one of those value, raises an exception.
    
    Returns:
        `str`: The greeting for the day.
    """

    # Variables
    # ---------

    this_func_name: str
    if currentframe() is not None:
        this_func_name = currentframe().f_code.co_name
    else:
        this_func_name = "The current function f"

    # Exceptions Handling
    # -------------------

    # match-case is only supported by Python 3.10+
    if not (pyver.major >= 3 and pyver.minor >= 10):
        raise Exception(f"`{this_func_name}()` is not supported in Python {pyver.major}.{pyver.minor}. Python 3.10+ is required.")
    
    # Argument `day` must match the specs
    if day not in ("mon", "tue", "wed", "thu", "fri", "sat", "sun"):
        raise Exception(f"Unable to process the argument `{day}`. Expecting a day value from the specified list. Please check the documentation.")

    # Normal Program Flow
    # -------------------
    
    match day:
        case "mon":
            return "Mondays are not so bad as people may say! You can do it!"
        case "fri":
            return "Have a great weekend!"
        # Multiple cases can be combined with `|`
        case "sat"|"sun":
            return "How is your weekend going?"
        # Optional default: `None` if undefined
        case _:
            return "How's your week so far?"
    


# Testing weekday_greeting()
# --------------------------

from typing import Tuple, Any

args: Tuple[Any,...] = ("mon", True, "thu", "fri", 123, "sat", "hello")

for arg in args:
    try:
        print(f"{arg} - {weekday_greeting(arg)}")
    except Exception as err:
        print(f"{arg} ----- Error: {err}")


from inspect import currentframe
from sys import version_info as pyver
from typing import Tuple

def which_person(person: Tuple[str, int, str]) -> str:
    """Say something about the person based on the data passed.

    This function currently only supports Python 3.10+.
    For older version, an exception is raised.

    Args:
        - `person` (`Tuple[str, int, str]`): A tuple representing the person.
            Expected format is a tuple `(name, age, gender)`.

    Returns:
        - `str`: A short description of the person. An empty string if no Pattern match found.
    """

    # Variables
    # ---------

    this_func_name: str
    if currentframe() is not None:
        this_func_name = currentframe().f_code.co_name
    else:
        this_func_name = "The current function f"
        
    # Exceptions Handling
    # -------------------

    # match-case is only supported by Python 3.10+
    if not (pyver.major >= 3 and pyver.minor >= 10):
        raise Exception(f"`{this_func_name}()` is not supported in Python {pyver.major}.{pyver.minor}. Python 3.10+ is required.")

    # Argument `person` is required
    if not person:
        raise Exception("Argument `person` is required.")

    # Normal Program Flow
    # -------------------
    result: str = ""

    match person:
        # List in order of priority
        # Only the first match is used
        case name, _ , "male":
            result = f"{name} is a man."
        case name, _ , "female":
            result = f"{name} is a woman."
        case name, age , _:
            result = f"{name} is {age} year{'s' if age > 1 else None} old"

    return result


# Testing which_person()
# --------------------------
from typing import Any, Tuple

argts: Tuple[Tuple[Any,...],...] = (
    ("John", 30, "male"),
    ("Mary", 31, "female"),
    ("Elizabeth", 28),
    ("Jeremy"),
    ("Adam", 50, "non-binary")
)

for person in argts:
    try:
        print(f"{person} -- {which_person(person)}")
    except Exception as err:
        print(f"{person} ----- Error: {err}")


from dataclasses import dataclass
from sys import version_info as pyver

@dataclass
class Person:
    """A simple Person class."""

    # Attributes: With Default Values for the optionals
    # ----------

    name: str
    age: int = 0
    gender: str = ""

# Utility Function
# ----------------
    
def which_person(person: Person) -> str:
    """Say something about the person based on the data passed.

    This function currently only supports Python 3.10+.
    For older version, an exception is raised.

    Args:
        - `person` (`Person`): A Person object representing the person.

    Returns:
        - `str`: A short description of the person. An empty string if no Pattern match found.
    """

    # Variables
    # ---------

    this_func_name: str
    if currentframe() is not None:
        this_func_name = currentframe().f_code.co_name
    else:
        this_func_name = "The current function f"
        
    # Exceptions Handling
    # -------------------

    # match-case is only supported by Python 3.10+
    if not (pyver.major >= 3 and pyver.minor >= 10):
        raise Exception(f"`{this_func_name}()` is not supported in Python {pyver.major}.{pyver.minor}. Python 3.10+ is required.")

    # Argument `person` is required
    if not person:
        raise Exception("Argument `person` is required.")

    # Normal Program Flow
    # -------------------

    match person:
        # Person() here is NOT a constructor-call but a pattern to match the used constructor format
        # Additional conditions can also be used
        case Person(name, age, _) if age < 18:
            return f"{name} is a child."
        case Person(name, _ , "male"):
            return f"{name} is a man."
        case Person(name, _ , "female"):
            return f"{name} is a woman."
        case Person(name, age , _):
            return f"{name} is {age} year{'s' if age > 1 else None} old"
        # If no match found, return a default
        case _:
            return("")


# Testing Person.which_person()
# -----------------------------

arguments: Person = (
    Person("John", 30, "male"),
    Person("Mary", 31, "female"),
    Person("Elizabeth", 15),
    Person("Jeremy"),
    Person("Adam", 50, "non-binary")
)

for person in arguments:
    try:
        print(f"{person} -- {which_person(person)}")
    except Exception as err:
        print(f"{person} ----- Error: {err}")


from typing import List

users: List[Person] = [
    Person(name="John", gender="male", age=25),
    Person(name="Mary", gender="female", age=20),
    Person(name="Carla", gender="nonbinary", age=40),
    Person(name="Eric", gender=None, age=30)
]

match users:
    # Matching a list of Person objects
    case [Person()]:
        print("One user provided.")
    # Capture sub-pattern into variable
    case [Person(), Person() as p, *remaining]:
        print(f"We don't know the first user.")
        print(f"The second user is {p.name}.")
        print(f"And the remaining are: {[p.name for p in remaining]}")
    # We can pack values in iterables
    case [*all]:
        count: int = len(all)
        print(f"We have lots of users, precisely {count}")


