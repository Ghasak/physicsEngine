import math
from typing import Union  # ,List , Dict, Tuple
from rich.console import Console
import pygame

# Console debugger for our given class.
console = Console()


class CVector2d(object):
    CONFIG = {"num_of_vec": 0}

    def __init__(
        self,
        x: Union[int, float] = 0.0,
        y: Union[int, float] = 0.0,
        verbose: bool = False,
    ):
        self._x = x
        self._y = y
        self._verbose = verbose
        CVector2d.CONFIG["num_of_vec"] += 1
        self.vector_id = CVector2d.CONFIG["num_of_vec"]

    def __str__(self):
        return f"Custom Vec {self.vector_id}: <{self._x},{self._y}>"

    # Change the logging level by accessing the verbose boolian

    @property
    def verbose(self):
        console.log(f"We currently verbosely showing messages: {self._verbose}")
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
                f"Obtain the x coordinate from vector{self.vector_id}: <{self._x},{self._y}>"
            )
        return self._x

    @x.setter
    def x(self, value):
        if self._verbose:
            console.log(
                f"setting the x coordinate from vector{self.vector_id}: <{self._x},{self._y}> to {value}, it will give us: <{self.x + value},{self.y}>"
            )
        # return CVector2d(self._x + value, self._y)
        self._x = value

    # Component proerpty of y - coordinate
    @property
    def y(self):
        if self._verbose:
            console.log(
                f"Obtain the y coordinate from vector{self.vector_id}: <{self._x},{self._y}>"
            )
        return self._y

    @y.setter
    def y(self, value):
        if self._verbose:
            console.log(
                f"setting the y coordinate from vector{self.vector_id}: <{self._x},{self._y}> to {value}, it will give us: <{self.x},{self.y + value}>"
            )
        self._y = value

    # Delete the vector once it is finished to free memeory
    def remove(self):
        if self._verbose:
            console.log(
                f"Vector {self.vector_id}: <{self._x},{self._y}> is removed ..."
            )
        del self

    # adding the arithemtatics operations to the our vector

    def __add__(self, other):
        if isinstance(other, CVector2d):
            return CVector2d(self.x + other.x, self.y + other.y)
        elif isinstance(other, (int, float)):
            return CVector2d(self.x + other, self.y + other)
        else:
            raise TypeError(
                "Unsupported operand type(s) for +: `Vector` and `{}`".format(
                    type(other)
                )
            )

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, CVector2d):
            return CVector2d(self.x - other.x, self.y - other.y)
        elif isinstance(other, (int, float)):
            return CVector2d(self.x - other, self.y - other)
        else:
            raise TypeError(
                "unsupported operand type(s) for -: 'Vector' and '{}'".format(
                    type(other)
                )
            )

    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            return CVector2d(other - self.x, other - self.y)
        else:
            raise TypeError(
                "unsupported operand type(s) for -: '{}' and 'Vector'".format(
                    type(other)
                )
            )

    def __truediv__(self, other):
        if isinstance(other, CVector2d):
            return CVector2d(self.x / other.x, self.y / other.y)
        elif isinstance(other, (int, float)):
            return CVector2d(self.x / other, self.y / other)
        else:
            raise TypeError(
                "unsupported operand type(s) for /: 'Vector' and '{}'".format(
                    type(other)
                )
            )

    def __rtruediv__(self, other):
        if isinstance(other, (int, float)):
            return CVector2d(other / self.x, other / self.y)
        else:
            raise TypeError(
                "unsupported operand type(s) for /: '{}' and 'Vector'".format(
                    type(other)
                )
            )

    def __mul__(self, other):
        if isinstance(other, CVector2d):
            return CVector2d(self.x * other.x, self.y * other.y)
        elif isinstance(other, (int, float)):
            return CVector2d(self.x * other, self.y * other)

    def __rmul__(self, other):
        return CVector2d(self.x * other, self.y * other)

    def magnitude(self):
        """This will give us the magnitude of a position vector from the origin <0,0>"""
        return math.sqrt(self.x**2 + self.y**2)

    def magnitude_from(self, other):
        """magnitude function
        This will give us the magnitude of a displacement vector
        which consturcted between two positional vectors from the original.
        """
        if isinstance(other, CVector2d):
            return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        else:
            raise TypeError(
                f"Not supported for: {type(other)}, you should provide a vector of a type of {self.__class__.__name__} to the magnitude_from() method"
            )

    def rotate(self, angle):
        self.x = self.x * math.cos(angle) - self.y * math.sin(angle)
        self.y = self.x * math.sin(angle) + self.y * math.cos(angle)
        return self

    @staticmethod
    def converate_pygame_vector_to_cvector2d(vector):
        return CVector2d(vector.x, vector.y)

    def converate_cvector2d_to_pygame_vector(self):
        return pygame.Vector2(self.x, self.y)

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def project(self, other):
        projection_length = self.dot(other) / other.magnitude()
        projection_x = projection_length * other.x / other.magnitude()
        projection_y = projection_length * other.y / other.magnitude()
        return CVector2d(projection_x, projection_y)

    def vectorProjection(self, other):
        c = self.dot(other) / (other.magnitude()) ** 2
        d = c * other
        return d

    def vectorProjection2(self, other):
        bCopy = other.copy()
        bCopy = bCopy.normalize()
        sp = self.dot(bCopy)
        bCopy_new = bCopy * sp
        return bCopy_new

    @staticmethod
    def vectorProjection_static(a, b):
        bCopy = b.copy().normalize()
        console.log(f"bCopy by applying copy and normalize{bCopy}")
        sp = a.dot(bCopy)
        console.log(f"value of sp -> {sp}")
        bCopy = bCopy * sp
        console.log(f"Value of bCopy_new -> {bCopy}")
        return bCopy

    def normalize(self):
        magnitude = self.magnitude()
        if magnitude == 0:
            raise ZeroDivisionError("Cannot normalize vector with magnitude 0")
        self.x /= magnitude
        self.y /= magnitude
        return CVector2d(self.x, self.y)

    def copy(self):
        return CVector2d(self.x, self.y)


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
    console.log(a.rotate(math.pi / 2.0))
    a = CVector2d(10, 10)
    b = CVector2d(20, 30)

    c = pygame.Vector2(10, 10)
    d = pygame.Vector2(20, 30)

    console.log(CVector2d.vectorProjection(a, b))
    console.log(a.vectorProjection(b))
    console.log(a.vectorProjection2(b))
    console.log(c.project(d))


if __name__ == "__main__":
    testing()
