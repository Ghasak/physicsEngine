import os
import sys
import math
from typing import Union #,List , Dict, Tuple
import pygame
from rich.console import Console
#from rich import print as rprint
#import numpy as np

console = Console()

# Intializing the
pygame.init()
pygame.font.init()



class CVector2d(object):
    CONFIG = {'num_of_vec': 0}

    def __init__(self, x: Union[int, float] = 0.0, y: Union[int, float] = 0.0, verbose: bool = False):
        self._x = x
        self._y = y
        self._verbose = verbose
        CVector2d.CONFIG['num_of_vec'] += 1
        self.vector_id = CVector2d.CONFIG['num_of_vec']

    def __str__(self):
        return f"Custom Vec {self.vector_id}: <{self._x},{self._y}>"
    # Change the logging level by accessing the verbose boolian

    @property
    def verbose(self):
        console.log(
            f"We currently verbosely showing messages: {self._verbose}")
        return self._verbose

    @verbose.setter
    def verbose(self, selection: bool):
        if isinstance(selection, bool):
            self._verbose = selection

    # Component proerpty of x - coordinate
    @property
    def x(self):
        if self._verbose:
            console.log(
                f"Obtain the x coordinate from vector{self.vector_id}: <{self._x},{self._y}>")
        return self._x

    @x.setter
    def x(self, value):
        if self._verbose:
            console.log(
                f"setting the x coordinate from vector{self.vector_id}: <{self._x},{self._y}> to {value}, it will give us: <{self.x + value},{self.y}>")
        # return CVector2d(self._x + value, self._y)
        self._x = value

    # Component proerpty of y - coordinate
    @property
    def y(self):
        if self._verbose:
            console.log(
                f"Obtain the y coordinate from vector{self.vector_id}: <{self._x},{self._y}>")
        return self._y

    @y.setter
    def y(self, value):
        if self._verbose:
            console.log(
                f"setting the y coordinate from vector{self.vector_id}: <{self._x},{self._y}> to {value}, it will give us: <{self.x},{self.y + value}>")
        self._y = value

    # Delete the vector once it is finished to free memeory
    def remove(self):
        if self._verbose:
            console.log(
                f"Vector {self.vector_id}: <{self._x},{self._y}> is removed ...")
        del self
    # adding the arithemtatics operations to the our vector

    def __add__(self, other):
        if isinstance(other, CVector2d):
            return CVector2d(self.x + other.x, self.y + other.y)
        elif isinstance(other, (int, float)):
            return CVector2d(self.x + other, self.y + other)
        else:
            raise TypeError(
                "Unsupported operand type(s) for +: `Vector` and `{}`".format(type(other)))

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, CVector2d):
            return  CVector2d(self.x - other.x, self.y - other.y)
        elif isinstance(other, (int, float)):
            return  CVector2d(self.x - other, self.y - other)
        else:
            raise TypeError("unsupported operand type(s) for -: 'Vector' and '{}'".format(type(other)))

    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            return CVector2d(other - self.x, other - self.y)
        else:
            raise TypeError("unsupported operand type(s) for -: '{}' and 'Vector'".format(type(other)))

    def __truediv__(self, other):
        if isinstance(other, CVector2d):
            return CVector2d(self.x / other.x, self.y / other.y)
        elif isinstance(other, (int, float)):
            return CVector2d(self.x / other, self.y / other)
        else:
            raise TypeError("unsupported operand type(s) for /: 'Vector' and '{}'".format(type(other)))

    def __rtruediv__(self, other):
        if isinstance(other, (int, float)):
            return CVector2d(other / self.x, other / self.y)
        else:
            raise TypeError("unsupported operand type(s) for /: '{}' and 'Vector'".format(type(other)))

    def __mul__(self, other):
        if isinstance(other, CVector2d):
            return CVector2d(self.x * other.x, self.y * other.y)
        elif isinstance(other, (int, float)):
            return CVector2d(self.x * other, self.y)

    def magnitude(self):
        '''This will give us the magnitude of a position vector from the origin <0,0>'''
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def magnitude_from(self, other):
        '''This will give us the magnitude of a displacement vector which consturcted between two positional vectors from the original'''
        if isinstance(other,CVector2d):
            return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        else:
            raise TypeError(f"Not supported for: {type(other)}, you should provide a vector of a type of {self.__class__.__name__} to the magnitude_from() method")

    def rotate(self, angle):
        x = self.x * math.cos(angle) - self.y * math.sin(angle)
        y = self.x * math.sin(angle) + self.y * math.cos(angle)
        self.x = x
        self.y = y
        #return CVector2d(self.x , self.y)
        # We will return the self, as we alter the vector by a rotation.
        return self


def testing():
    a = CVector2d(x=0, y=1, verbose=False)
    b = CVector2d(x=200.0, y=300.0, verbose=False)
    # console.log(a)
    # console.log(a.x)
    # console.log(a.y)
    # a.x = 20.0
    # console.log(a)
    # console.log(a.remove())
    # console.log(a.verbose)
    # a.verbose = False
    # console.log(a.verbose)
    # console.log(a)
    # console.log(a.x, a.y)
    # notice here we will use the __add__ method, with CVector2d instance
    console.log(a + b)
    # notice here we will use the __add__ method, with int type
    console.log(a + 20)
    # notice here we will use the __radd__ method
    console.log(30 + a)
    console.log(a.magnitude_from(b))
    console.log(a.magnitude())
    console.log(a.rotate(math.pi/2.0))

testing()

