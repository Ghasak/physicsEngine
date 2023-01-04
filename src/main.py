# import os
import sys

# import math
# from typing import Union #,List , Dict, Tuple
import pygame
from rich.console import Console

# from rich import print as rprint
# import numpy as np

# Import our implementation
from src.Tools.pygame_debuger import debug
from src.stats.Constants import PYGAME_CONFIG
from src.stats.Constants import COLOR_PALETTE
from src.Tools.layout import Environment, Environment_testing_1, Environment_testing_2

# ---------- implementation ----------------
console = Console()

# Intialize the pygame
pygame.init()
pygame.font.init()
# font =pygame.font.Font(None, 30)

# ---------- Pygame characteristics ----------------
screen = pygame.display.set_mode((PYGAME_CONFIG["WIDTH"], PYGAME_CONFIG["HIGHT"]))
clock = pygame.time.Clock()

global_theta = 0.0
update_angle = 0.0
# ---------- Main Loop ----------------
pygame_running = True
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
    env.centerlines(selected_color="light_black")
    env.grid(selected_color="light_gray", theta=None)

    # +------------------------------------+
    #    Calling some Examples goes here:
    # +------------------------------------+
    update_angle = Environment_testing_2(
        screen, pygame, PYGAME_CONFIG, COLOR_PALETTE, global_theta, update_angle
    )
    Environment_testing_1(
        screen, pygame, PYGAME_CONFIG, COLOR_PALETTE, global_theta, update_angle
    )

    debug(f"time detla {dt} in milliseconds")
    pygame.display.update()
    # pygame.display.flip()
    clock.tick(60)
