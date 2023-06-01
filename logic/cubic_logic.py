import pygame
import pygame.font


def draw_cubic(screen, width, height, a, b, c, d, color, scale):
    for x in range(width):
        x_coord = (x - width/2) / scale
        y_coord = -(a * x_coord ** 3 + b * x_coord ** 2 + c * x_coord + d) / scale
        pygame.draw.circle(screen, color, (int(x), int(height/2 + y_coord*scale)), 1)

