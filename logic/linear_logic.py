import pygame

def draw_line(screen, width, height, slope, y_intercept, color, scale):
    x1 = 0
    y1 = int((slope * x1 + y_intercept) / scale)
    x2 = width - 1
    y2 = int((slope * x2 + y_intercept) / scale)
    pygame.draw.line(screen, color, (x1, height - y1), (x2, height - y2), 1)
