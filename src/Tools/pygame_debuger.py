import pygame

pygame.init()
font = pygame.font.Font(None, 20)
# screen = pygame.display.set_mode((PYGAME_CONFIG['WIDTH'], PYGAME_CONFIG['HIGHT']))

# Screen Characters, location

from src.stats.Constants import PYGAME_CONFIG
from src.stats.Constants import COLOR_PALETTE
from src.stats.Constants import POINT_FEATURES


def debug(info, y=10, x=PYGAME_CONFIG["WIDTH"] - 250):
    display_surface = pygame.display.get_surface()
    debug_surf = font.render(str(info), True, COLOR_PALETTE["light_black"])
    debug_rect = debug_surf.get_rect(topleft=(x, y))
    pygame.draw.rect(display_surface, COLOR_PALETTE["white"], debug_rect)
    display_surface.blit(debug_surf, debug_rect)


def show_information(text_info: str, text_info_position: pygame.Vector3):
    font = pygame.font.Font(None, 20)
    # console.log(text_info_position)
    display_surface = pygame.display.get_surface()
    debug_surf = font.render(str(text_info), True, COLOR_PALETTE["blue"])
    debug_rect = debug_surf.get_rect(topright=text_info_position)
    pygame.draw.rect(display_surface, COLOR_PALETTE["black"], debug_rect)
    display_surface.blit(debug_surf, debug_rect)


def show_position_vector(screen, vec, text):
    pygame.draw.line(screen, COLOR_PALETTE["gray"], (0, 0), vec, 1)
    pygame.draw.circle(screen, "deeppink", vec, POINT_FEATURES["radius"])
    show_information(
        f"Pos:{text} <{vec.x:2.2f},{vec.y:2.2f}>",
        (vec.x - POINT_FEATURES["offset_x"], vec.y + POINT_FEATURES["offset_y"]),
    )
