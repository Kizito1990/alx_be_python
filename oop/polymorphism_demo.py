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
        return f"The area of the Rectangle is: {self.width * self.length}"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return f"The area of the Circle is:{math.pi * self.radius * self.radius}"


