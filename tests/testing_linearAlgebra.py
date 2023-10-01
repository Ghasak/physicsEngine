from rich import console
from rich.console import Console
from src.Tools.linearAlgebra import MVector


# Initize our console log
console = Console()



# Using the MVector class, extended from the `pygame.Vector2` class.
a = MVector(10,10)
b = MVector(20,20)
console.log(a + b)






