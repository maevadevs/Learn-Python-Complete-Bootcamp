#!/usr/bin/env python
# coding: utf-8

from typing import Tuple


from math import sqrt

class Line(object):
    def __init__(self, p0: Tuple[int, int] = (0,0), p: Tuple[int, int] = (0,0)) -> None:
        # p0 and p are tuples on self
        self.p0: Tuple[int, int] = p0    # p0 = (x0, y0)
        self.p: Tuple[int, int] = p      # p = (x, y)
    

    def distance(self) -> float:
        # Tuple unpacking: p0 and p are tuples on self
        x0: int; y0: int
        x: int; y: int
        x0, y0 = self.p0
        x, y = self.p

        # Using absolute value: Distance = sqrt((x-x0)**2 + (y-y0)**2)
        return sqrt((float(x) - float(x0))**2 + (float(y) - float(y0))**2)

  
    def slope(self) -> float:
        x0: int; y0: int
        x: int; y: int
        # tuple unpacking: p0 and p are tuples on self
        x0, y0 = self.p0
        x, y = self.p
        # Using absolute value: Slope = DeltaY / DelatX
        delta_x: float = float(x) - float(x0)
        delta_y: float = float(y) - float(y0)
        if delta_y == 0:
            raise ValueError("Unable to calculate the slope without a height: delta_y == 0")
        return abs(delta_y) / abs(delta_x)       
        


# EXAMPLE OUTPUT
point1: Tuple[int, int] = (3, 2)
point2: Tuple[int, int] = (8, 10)
li: Line = Line(point1, point2)

print("distance:", li.distance())
print("slope:", li.slope())


from math import pi

class Cylinder(object):
    def __init__(self, height: float = 1.0, radius: float = 1.0) -> None:
        self.height = height
        self.radius = radius


    def volume(self) -> float:
        # Cylinder volume: V = πr^2h
        return (pi * (self.radius ** 2)) * self.height


    def surface_area(self) -> float:
        # Cylinder surface area: A = 2πrh (side) + 2πr^2 (top circle)
        side: float = 2 * pi * self.radius * self.height
        top_circle: float = 2 * pi * self.radius ** 2
        return side + top_circle


# EXAMPLE OUTPUT
c: Cylinder = Cylinder(2.0, 3.0)
print("volume:", c.volume())
print("surface:", c.surface_area())


