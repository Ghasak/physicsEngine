# import os
import math
import sys

# from typing import Union #,List , Dict, Tuple
import pygame
from pygame.display import update
from rich.console import Console

from src.concepts.vectors_fundamentals.vector_projection import \
    vector_projection_fn
from src.stats.Constants import COLOR_PALETTE, PYGAME_CONFIG
from src.Tools.layout import (Environment, Environment_testing_1,
                              Environment_testing_2)
from src.Tools.linearAlgebra import MVector
# Import our implementation
from src.Tools.pygame_debuger import debug, show_position_vector

# from rich import print as rprint
# import numpy as np

# ---------- implementation ----------------
console = Console()

# Intialize the pygame
pygame.init()
pygame.font.init()
# font =pygame.font.Font(None, 30)

# ---------- Pygame characteristics ----------------
screen = pygame.display.set_mode(
    (PYGAME_CONFIG["WIDTH"], PYGAME_CONFIG["HIGHT"]))
clock = pygame.time.Clock()

global_theta = 0.0
update_angle = 0.0
# ---------- Main Loop ----------------


def setup():
    a = pygame.Vector2(PYGAME_CONFIG["WIDTH"] / 2.0,
                       PYGAME_CONFIG["HIGHT"] / 2.0)
    b = pygame.Vector2(PYGAME_CONFIG["WIDTH"] / 6.0,
                       PYGAME_CONFIG["HIGHT"] / 6.0)
    c = pygame.Vector2(100, 100)
    return a, b, c


pygame_running = True

c = MVector(100, 100)
c.MTranslate([50, 50])
#c.MTranslate([PYGAME_CONFIG["WIDTH"] / 6.0, PYGAME_CONFIG["HIGHT"] / 6.0])

while pygame_running:
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(COLOR_PALETTE["black"])

    # Create an Environment
    env = Environment(
        surface=screen,
        pygame=pygame,
        config=PYGAME_CONFIG,
        color=COLOR_PALETTE,
        global_theta=None,
    )
    # Adding centerline and girds
    env.grid(selected_color="light_gray", theta=None)
    env.centerlines(selected_color="light_black")
    a, b, c = setup()
    # +------------------------------------+
    #    Calling some Examples goes here:
    # +------------------------------------+
    update_angle = Environment_testing_2(screen, pygame, PYGAME_CONFIG,
                                         COLOR_PALETTE, global_theta,
                                         update_angle)
    Environment_testing_2(screen, pygame, PYGAME_CONFIG, COLOR_PALETTE,
                          global_theta, update_angle)
    #c.draw_vector(screen)
    #a.MRotate(update_angle)
    a = a.rotate(update_angle)
    #a = MVector(a.x, a.y).MUpdate()
    #a.MRotate(update_angle).MUpdate().MDraw_from_origin('vector A origin')
    #update_angle += 1
    b = b.rotate(update_angle)
    #b.MDraw(screen)
    pygame.draw.circle(screen, 'red', b, 10)
    d = c - b
    d = d.rotate(update_angle)
    #

    pygame.draw.line(screen, 'grey', a, d + a, 1)
    pygame.draw.line(screen, 'grey', a, d + b, 1)
    pygame.draw.line(screen, 'grey', a, d + c, 1)

    pygame.draw.line(screen, 'grey', b, d + b, 1)
    pygame.draw.line(screen, 'grey', c, d + c, 1)

    pygame.draw.circle(screen, "red", d + a, 5)
    pygame.draw.circle(screen, "blue", d + b, 5)
    pygame.draw.circle(screen, "purple", d + c, 5)
    pygame.draw.circle(screen, "black", d + a, 10, 3)
    pygame.draw.circle(screen, "black", d + b, 10, 3)
    pygame.draw.circle(screen, "black", d + c, 10, 3)
    #
    vector_projection_fn(pygame, screen, COLOR_PALETTE, MVector,
                         show_position_vector)
    debug(f"time detla {dt} in milliseconds")
    pygame.display.update()
    # pygame.display.flip()
    clock.tick(60)
