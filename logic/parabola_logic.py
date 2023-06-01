import pygame

def draw_parabola(screen, width, height, slope, y_intercept, color):
    middle_x = width // 2
    for x in range(width):
        translated_x = x - middle_x
        y = int(slope * translated_x ** 2 + y_intercept)
        pygame.draw.circle(screen, color, (x, height - y), 1)