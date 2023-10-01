import pygame
import math
from typing import Union, Tuple
from rich.console import Console, ConsoleOptions

console = Console()

# Things we need to address
from src.stats.Constants import PYGAME_CONFIG, COLOR_PALETTE


class MVector(pygame.Vector2):
    CONFIG = {
        "centerline_line_width": 3,
        "grid_line_width": 3,
        "grid_fine_line_width": 1,
        "grid_spacing_x": 50,
        "grid_spacing_y": 50,
        "grid_fine_spacing_x": 10,
        "grid_fine_spacing_y": 10,
        "arrow_line_width": 5,
        "guidelines": 2,
        "point_radius": 8,
        "offset_font_x": 10,
        "offset_font_y": 50,
        "Composition-x-line-width": 2,
        "Composition-y-line-width": 2,
    }
    COMPOSITION_VISIBLE: bool = True

    def __init__(self, x: float, y: float):
        super().__init__(x, y)
        self.width = PYGAME_CONFIG["WIDTH"] / 2.0
        self.hight = PYGAME_CONFIG["HIGHT"] / 2.0
        self.center_vector = pygame.Vector2(PYGAME_CONFIG["WIDTH"] / 2.0,
                                            PYGAME_CONFIG["HIGHT"] / 2.0)

    def MTranslate(self, position: Union[str, tuple] = [0, 0]):
        self.translate_vector = pygame.Vector2(position[0], position[1])
        # if isinstance(position, (list, tuple)):
        # else:
        #     raise TypeError("You must provide a list or tuple for the coordinates ...")

    def MRotate(self, theta):
        self.x = self.x * math.cos(theta) - self.y * math.sin(theta)
        self.y = self.x * math.sin(theta) + self.y * math.cos(theta)

    def draw_vector(self, surface, lablel=""):

        self.surface = pygame.display.get_surface()
        self.xnew = self.x + self.translate_vector.x + self.width
        self.ynew = -(self.y + self.translate_vector.y) + self.hight

        #pygame.draw.circle(self.surface, "red", [self.xnew, self.ynew], 10)
        pygame.draw.circle(self.surface, "red", self.center_vector, 10)
        pygame.draw.circle(
            self.surface,
            "red",
            [
                self.center_vector.x + self.translate_vector.x,
                self.center_vector.y - self.translate_vector.y,
            ],
            10,
        )

        #pygame.draw.circle(surface, "red", [self.xnew, self.ynew], 10)

        # Draw label and the coordinates
        font = pygame.font.Font(None, 30)
        text_surf = font.render(
            f"({lablel}:{self.center_vector.x:2.1f},{self.center_vector.y:2.1f})",
            True,
            COLOR_PALETTE["light_black"],
        )
        text_surf.set_alpha(127)
        self.surface.blit(
            text_surf,
            (self.center_vector),
        )

        # Draw label and the coordinates
        font = pygame.font.Font(None, 30)
        text_surf = font.render(
            f"({lablel}:{self.translate_vector.x:2.1f},{self.translate_vector.y:2.1f})",
            True,
            COLOR_PALETTE["light_black"],
        )
        text_surf.set_alpha(127)
        self.surface.blit(
            text_surf,
            (
                self.center_vector.x + self.translate_vector.x,
                self.center_vector.y - self.translate_vector.y,
            ),
        )

    # def Translate(self, position=[0, 0]):
    #     self.translate_x = position[0]
    #     self.translate_y = position[1]
    #     return self
    #
    # def MRotate(self, theta = 0.0):
    #     # This method will give us all the components we want from a given vector.
    #     # self.x = self.x * math.cos(theta) - self.y * math.sin(theta)
    #     # self.y = self.x * math.sin(theta) + self.y * math.cos(theta)
    #
    #     self.x = self.x * math.cos(theta) - self.y * math.sin(theta)
    #     self.y = self.x * math.sin(theta) + self.y * math.cos(theta)
    #     return self
    #
    # def MUpdate(self):
    #     # getting the translated coordinates from the user if he uses the (Translate method)
    #     self.relative_x = self.x + self.translate_x
    #     self.relative_y = self.y + self.translate_y
    #
    #     # From the middle of screen
    #     self.transformed_x = self.x + self.translate_x + self.width
    #     self.transformed_y = -(self.y + self.translate_y) + self.hight
    #     return self
    #
    # def MDraw_from_origin(self, lablel: str = ""):
    #
    #     # Getting the surface using the pygame module
    #     self.surface = pygame.display.get_surface()
    #
    #     pygame.draw.line(
    #         self.surface,
    #         COLOR_PALETTE["light_blue"],
    #         [self.width, self.hight],
    #         [self.transformed_x, self.transformed_y],
    #         MVector.CONFIG["guidelines"],
    #     )
    #
    #     # Draw label and the coordinates
    #     font = pygame.font.Font(None, 30)
    #     text_surf = font.render(
    #         f"({lablel}:{self.relative_x:2.1f},{self.relative_y:2.1f})",
    #         True,
    #         COLOR_PALETTE["light_black"],
    #     )
    #     text_surf.set_alpha(127)
    #     self.surface.blit(
    #         text_surf,
    #         (
    #             self.transformed_x + MVector.CONFIG["offset_font_x"],
    #             self.transformed_y + MVector.CONFIG["offset_font_y"],
    #         ),
    #     )
    #
    #     # Draw the components of the vector from origin
    #     if MVector.COMPOSITION_VISIBLE:
    #
    #         # basis vectors  from origin to x and y
    #         pygame.draw.line(
    #             self.surface,
    #             "red",
    #             [self.width, self.hight],
    #             [self.width + self.relative_x, self.hight],
    #             4,
    #         )
    #         pygame.draw.line(
    #             self.surface,
    #             "blue",
    #             [self.width, self.hight],
    #             [self.width, self.hight - self.relative_y],
    #             4,
    #         )
    #
    #         # complement vectors from origin
    #         pygame.draw.line(
    #             self.surface,
    #             "red",
    #             [self.width + self.relative_x, self.hight],
    #             [self.transformed_x, self.transformed_y],
    #             1,
    #         )
    #         pygame.draw.line(
    #             self.surface,
    #             "blue",
    #             [self.width, self.hight - self.relative_y],
    #             [self.transformed_x, self.transformed_y],
    #             1,
    #         )
    #     # Draw the point at give user x,y
    #     pygame.draw.circle(self.surface, "red", [self.transformed_x, self.transformed_y], 10)
