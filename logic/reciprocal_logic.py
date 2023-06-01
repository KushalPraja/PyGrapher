import pygame
import pygame_gui

def draw_reciprocal(screen, width, height, k, d, color):
    middle_x = width // 2
    middle_y = height // 2

    for x in range(width):
        translated_x = x - middle_x

        # Check if translated_x is zero or too close to zero
        if abs(translated_x) < 0.001:
            continue

        # Calculate the y-coordinate
        y = int(k / translated_x + d + middle_y)
        pygame.draw.circle(screen, color, (x, y), 1)
