import math

import pygame


class Environment(object):
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
        "offset_font_x": 5,
        "offset_font_y": 5,
        "Composition-x-line-width": 2,
        "Composition-y-line-width": 2,
    }

    def __init__(self, surface, pygame, config, color, global_theta):
        self.globaltheta = global_theta
        self.config = config
        self.surface = surface
        self.pygame = pygame
        self.hight = config["HIGHT"]
        self.width = config["WIDTH"]
        self.color = color

    def grid(self, selected_color="gray", theta=None, refined=True):

        # Font size configurations
        font = pygame.font.Font(None, 20)

        if refined:
            for ticks_x in range(self.config["WIDTH"]):
                self.pygame.draw.line(
                    self.surface,
                    self.color["light_gray"],
                    (0, Environment.CONFIG["grid_fine_spacing_x"] * ticks_x),
                    (
                        self.config["WIDTH"],
                        Environment.CONFIG["grid_fine_spacing_x"] * ticks_x,
                    ),
                    Environment.CONFIG["grid_fine_line_width"],
                )
            for ticks_y in range(self.config["HIGHT"]):
                self.pygame.draw.line(
                    self.surface,
                    self.color["light_gray"],
                    (Environment.CONFIG["grid_fine_spacing_y"] * ticks_y, 0),
                    (
                        Environment.CONFIG["grid_fine_spacing_y"] * ticks_y,
                        self.config["HIGHT"],
                    ),
                    Environment.CONFIG["grid_fine_line_width"],
                )
        for ticks_x in range(self.config["WIDTH"]):
            self.pygame.draw.line(
                self.surface,
                self.color[f"{selected_color}"],
                (0, Environment.CONFIG["grid_spacing_x"] * ticks_x),
                (self.config["WIDTH"],
                 Environment.CONFIG["grid_spacing_x"] * ticks_x),
                Environment.CONFIG["grid_line_width"],
            )
        for ticks_y in range(self.config["HIGHT"]):
            self.pygame.draw.line(
                self.surface,
                self.color[f"{selected_color}"],
                (Environment.CONFIG["grid_spacing_y"] * ticks_y, 0),
                (Environment.CONFIG["grid_spacing_y"] * ticks_y,
                 self.config["HIGHT"]),
                Environment.CONFIG["grid_line_width"],
            )

        for ticks_x in range(self.config["WIDTH"]):
            # To avoide draw duplicated the font tick on middle of axis
            if int(ticks_x *
                   Environment.CONFIG["grid_spacing_x"]) != (self.hight / 2):
                display_surface = self.pygame.display.get_surface()
                font_surf = font.render(
                    str(int(ticks_x * Environment.CONFIG["grid_spacing_x"])),
                    True,
                    self.color["blue"],
                )
                font_rect = font_surf.get_rect(topleft=(
                    (self.width / 2) + Environment.CONFIG["offset_font_x"],
                    Environment.CONFIG["grid_spacing_x"] * ticks_x,
                ))
                pygame.draw.rect(display_surface, self.color["white"],
                                 font_rect)
                display_surface.blit(font_surf, font_rect)

        for ticks_y in range(self.config["HIGHT"]):
            # To avoide draw duplicated the font tick on middle of axis
            if int(ticks_y *
                   Environment.CONFIG["grid_spacing_y"]) != (self.width / 2):
                display_surface = self.pygame.display.get_surface()
                font_surf = font.render(
                    str(int(ticks_y * Environment.CONFIG["grid_spacing_y"])),
                    True,
                    self.color["blue"],
                )
                font_rect = font_surf.get_rect(topleft=(
                    Environment.CONFIG["grid_spacing_y"] * ticks_y,
                    (self.hight / 2) + Environment.CONFIG["offset_font_y"],
                ))
                pygame.draw.rect(display_surface, self.color["white"],
                                 font_rect)
                display_surface.blit(font_surf, font_rect)

    def centerlines(self, selected_color):
        self.pygame.draw.line(
            self.surface,
            self.color[f"{selected_color}"],
            (0, self.hight / 2),
            (self.width, self.hight / 2),
            Environment.CONFIG["centerline_line_width"],
        )
        self.pygame.draw.line(
            self.surface,
            self.color[f"{selected_color}"],
            (self.width / 2, 0),
            (self.width / 2, self.hight),
            Environment.CONFIG["centerline_line_width"],
        )

    def draw_vector(self,
                    pos: pygame.Vector2 = None,
                    vector: pygame.Vector2 = pygame.Vector2(0, 0),
                    theta: float = None,
                    selected_color: str = "black",
                    visualize_composition=True,
                    vector_text=""):
        """Draw vector for any position you want
        Input:
        - self `Environment instance`: Extension from our Environment class
            - pos `pygame.Vector2`: Vector2 represents where you want to draw the vector origin (tail) from our middle of screen as origin ( 0, 0 ), shiftted by (x,y).
            - vector `pygame.Vector2`: Vector2 respents our given vector drawn from the origin (with respect to the pos) the new position of the origin.
            - theta `theta`: is the rotational angle of the tip of the vector assume the tail will stay at the new origin (pos + middle of screen).
            - selected_color `string`: selected color for drawing the vector.

        """
        origin_x_new, origin_y_new = (
            self.config["WIDTH"] / 2.0,
            self.config["HIGHT"] / 2.0,
        )

        # Create a vecotr from the given coordinates
        if pos is None:
            tail_origin_vector = self.pygame.Vector2(origin_x_new,
                                                     origin_y_new)
            vector = vector + pos
        else:
            tail_origin_vector = self.pygame.Vector2(pos.x + origin_x_new,
                                                     pos.y + origin_y_new)
            self.pygame.draw.line(
                self.surface,
                self.color["light_blue"],
                [origin_x_new, origin_y_new],
                tail_origin_vector,
                Environment.CONFIG["guidelines"],
            )

        if theta is not None:
            transformed_x = vector.x * math.cos(theta) - vector.y * math.sin(
                theta)
            transformed_y = vector.x * math.sin(theta) + vector.y * math.cos(
                theta)
            tip_transformed_vector = self.pygame.Vector2(
                transformed_x, transformed_y)
        else:
            tip_transformed_vector = self.pygame.Vector2(vector.x, vector.y)

        transformed_x = tip_transformed_vector.x + self.config["WIDTH"] / 2.0
        transformed_y = -tip_transformed_vector.y + self.config["HIGHT"] / 2.0

        # Transfer our new position if it existed.
        if pos is None:
            tip_transformed_vector = self.pygame.Vector2(
                transformed_x, transformed_y)
        else:
            tip_transformed_vector = (
                self.pygame.Vector2(transformed_x, transformed_y) + pos)

        # Draw the vector
        self.pygame.draw.line(
            self.surface,
            self.color["light_blue"],
            [origin_x_new, tail_origin_vector.y],
            tail_origin_vector,
            Environment.CONFIG["guidelines"],
        )
        self.pygame.draw.line(
            self.surface,
            self.color[f"{selected_color}"],
            tail_origin_vector,
            tip_transformed_vector,
            Environment.CONFIG["arrow_line_width"],
        )
        self.pygame.draw.line(
            self.surface,
            self.color["light_blue"],
            [tail_origin_vector.x, origin_y_new],
            tail_origin_vector,
            Environment.CONFIG["guidelines"],
        )
        self.pygame.draw.circle(
            self.surface,
            self.color[f"{selected_color}"],
            tail_origin_vector,
            Environment.CONFIG["point_radius"],
        )

        if visualize_composition:
            # Font size configurations
            font = pygame.font.Font(None, 30)
            display_surface = self.pygame.display.get_surface()
            vec = tip_transformed_vector - tail_origin_vector
            # +--------------------------+
            #      X- Composition
            # +--------------------------+
            font_vec_surf = font.render(
                str(f"x-axis"),
                True,
                self.color["red"],
            )
            font_vec_rect = font_vec_surf.get_rect(
                topleft=(tail_origin_vector.x + vec.x, tail_origin_vector.y))
            pygame.draw.rect(display_surface, self.color["white"],
                             font_vec_rect)
            display_surface.blit(font_vec_surf, font_vec_rect)

            self.pygame.draw.line(
                self.surface,
                self.color["red"],
                tail_origin_vector,
                (tail_origin_vector.x + vec.x, tail_origin_vector.y),
                Environment.CONFIG['Composition-x-line-width'],
            )
            # +--------------------------+
            #      Y- Composition
            # +--------------------------+
            font_vec_surf = font.render(
                str(f"y-axis"),
                True,
                self.color["blue"],
            )
            font_vec_rect = font_vec_surf.get_rect(
                topleft=(tail_origin_vector.x, tail_origin_vector.y + vec.y))
            pygame.draw.rect(display_surface, self.color["white"],
                             font_vec_rect)
            display_surface.blit(font_vec_surf, font_vec_rect)

            self.pygame.draw.line(
                self.surface,
                self.color["blue"],
                tail_origin_vector,
                (tail_origin_vector.x, tail_origin_vector.y + vec.y),
                Environment.CONFIG['Composition-y-line-width'],
            )
            # +--------------------------+
            #    dd lable to the tip
            # +--------------------------+
            font_vec_surf = font.render(
                str(f"{vector_text}<{tip_transformed_vector.x + Environment.CONFIG['offset_font_x']:2.2f},{tip_transformed_vector.y +Environment.CONFIG['offset_font_y']:2.2f}>"
                    ),
                True,
                self.color["orange"],
            )
            font_vec_rect = font_vec_surf.get_rect(
                topleft=(tip_transformed_vector))
            pygame.draw.rect(display_surface, self.color["white"],
                             font_vec_rect)
            display_surface.blit(font_vec_surf, font_vec_rect)


def Environment_testing_1(screen, pygame, PYGAME_CONFIG, COLOR_PALETTE,
                          global_theta, angle):
    global_theta = 0.0
    env = Environment(screen, pygame, PYGAME_CONFIG, COLOR_PALETTE,
                      global_theta)
    env.centerlines("light_black")
    # Before trasnformation
    env.draw_vector(
        pos=pygame.Vector2(300, 0),
        vector=pygame.Vector2(100, 0),
        theta=None,
        selected_color="blue",
    )
    env.draw_vector(
        pos=pygame.Vector2(300, 0),
        vector=pygame.Vector2(0, 100),
        theta=None,
        selected_color="blue",
    )
    # After Transformation (applying 90 degree angle)
    env.draw_vector(
        pos=pygame.Vector2(-300, 0),
        vector=pygame.Vector2(100, 0),
        theta=math.pi / 2,
        selected_color="red",
    )
    env.draw_vector(
        pos=pygame.Vector2(-300, 0),
        vector=pygame.Vector2(0, 100),
        theta=math.pi / 2,
        selected_color="red",
    )


def Environment_testing_2(screen, pygame, PYGAME_CONFIG, COLOR_PALETTE,
                          global_theta, angle):
    global_theta = 0.0
    env = Environment(screen, pygame, PYGAME_CONFIG, COLOR_PALETTE,
                      global_theta)
    env.centerlines("light_black")

    # draw vector in first sector (x is + and y is + )
    env.draw_vector(
        pos=pygame.Vector2(50, 50),
        vector=pygame.Vector2(100, 0),
        theta=angle,
        selected_color="red",
    )
    env.draw_vector(
        pos=pygame.Vector2(50, 50),
        vector=pygame.Vector2(0, 100),
        theta=angle,
        selected_color="red",
    )
    # draw vector in first sector (x is - and y is + )
    env.draw_vector(
        pos=pygame.Vector2(-50, 50),
        vector=pygame.Vector2(100, 0),
        theta=angle,
        selected_color="red",
    )
    env.draw_vector(
        pos=pygame.Vector2(-50, 50),
        vector=pygame.Vector2(0, 100),
        theta=angle,
        selected_color="red",
    )

    # draw vector in first sector (x is + and y is - )
    env.draw_vector(
        pos=pygame.Vector2(50, -50),
        vector=pygame.Vector2(100, 0),
        theta=angle,
        selected_color="red",
    )
    env.draw_vector(
        pos=pygame.Vector2(50, -50),
        vector=pygame.Vector2(0, 100),
        theta=angle,
        selected_color="red",
    )

    # draw vector in first sector (x is - and y is - )
    env.draw_vector(
        pos=pygame.Vector2(-50, -50),
        vector=pygame.Vector2(100, 0),
        theta=angle,
        selected_color="red",
    )
    env.draw_vector(
        pos=pygame.Vector2(-50, -50),
        vector=pygame.Vector2(0, 100),
        theta=angle,
        selected_color="red",
    )

    # angle = (angle + (1/100)) % (360)
    angle = angle + 0.01
    return angle


if __name__ == "__main__":
    pass

    # Environment_testing_1(screen, pygame,PYGAME_CONFIG,  COLOR_PALETTE,global_theta, update_angle)
    # update_angle = Environment_testing_2(screen, pygame,PYGAME_CONFIG,  COLOR_PALETTE,global_theta, update_angle)
