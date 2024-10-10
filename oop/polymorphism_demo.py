#!/bin/bash
from abc import ABC, abstractmethod
import math

class Shape:


    @abstractmethod
    def area(self):
        raise "NotImplementedError"

class Rectangle(Shape):
    def __init__(self, width, length):
         self.width = width
         self.length = length

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


