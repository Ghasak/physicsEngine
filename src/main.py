import os
import sys
import math
from typing import Union #,List , Dict, Tuple
import pygame
from rich.console import Console
#from rich import print as rprint
#import numpy as np

# Import our implementation
from src.concepts.vectors_fundamentals.vector_class import CVector2d
from src.Tools.pygame_debuger import debug,show_information, show_position_vector
from src.stats.Constants import PYGAME_CONFIG
from src.stats.Constants import COLOR_PALETTE
# ---------- implementation ----------------
console = Console()

# Intialize the pygame
pygame.init()
pygame.font.init()
# font =pygame.font.Font(None, 30)


# ---------- Pygame characteristics ----------------
screen = pygame.display.set_mode((PYGAME_CONFIG['WIDTH'], PYGAME_CONFIG['HIGHT']))
clock = pygame.time.Clock()



# ---------- Main Loop ----------------
while True:
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(COLOR_PALETTE['black'])

    # This will get us at each frame the position vector of a mouse
    mouse_position = pygame.Vector2(pygame.mouse.get_pos())
    #pygame.draw.line(screen, 'blue', (0,0), (vec3), 3)
    path= pygame.Vector2(200, 60)
    pos= pygame.Vector2(100,200)


    head = pygame.Vector2(path + pos)
    # pygame.draw.line(screen, 'black', pos, head, 3)

    a = mouse_position - pos
    pygame.draw.line(screen, COLOR_PALETTE['red'], pos, a + pos, 3)
    pygame.draw.line(screen, COLOR_PALETTE['red'], pos,head, 3)

    #v =pygame.math.Vector2.project(a,path)
    a_dash =  CVector2d.converate_pygame_vector_to_cvector2d(a)
    path_dash =  CVector2d.converate_pygame_vector_to_cvector2d(path)
    #v = CVector2d.project(a,path)
    v1 = CVector2d.project(a_dash,path_dash)
    # You can also use

    #v2 = a_dash.vectorProjection(path_dash)
    v2 =CVector2d.vectorProjection( a_dash,path_dash)
    v = CVector2d.converate_cvector2d_to_pygame_vector(v2)
    pygame.draw.line(screen, 'deepskyblue4', v + pos, mouse_position, 5)
    pygame.draw.line(screen, 'deepskyblue4', pos,v + pos, 5)

    show_position_vector(screen = screen ,vec = mouse_position, text ="Vector M ->")
    show_position_vector(screen = screen ,vec = pos, text ="Vector pos ->")
    show_position_vector(screen = screen ,vec = pos + path, text ="Vector path ->")




    debug(f"time detla {dt} in milliseconds")
    pygame.display.update()
    clock.tick(60)


