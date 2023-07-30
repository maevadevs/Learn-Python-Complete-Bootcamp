#!/usr/bin/env python
# coding: utf-8

class _Const:
    """Allows a property to only be set once. 
    If it is already set, throw error if trying to set again.
    Allow read at anytime."""

    def __setattr__(self, name, value):
        # Error handling
        for key, val in self.__dict__.items():
            if key == name:
                raise self._ConstError(f"ConstError: Const {name} already exist: value = {val}.")
        # Else, assign
        self.__dict__[name] = value

    class _ConstError(TypeError):
        """Custom Type Exception class for Const class"""

CONST = _Const()
