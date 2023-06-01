import pygame
import math


def draw_sinusoidal(screen, width, height, amplitude, frequency, phase_shift, color):
    middle_x = width // 2
    middle_y = height // 2
    # Adjust the frequency to match the screen width
    frequency *= 2 * math.pi / width
    for x in range(width):
        translated_x = x - middle_x
        y = int(amplitude * math.sin(frequency * translated_x + phase_shift) + middle_y)
        pygame.draw.circle(screen, color, (x, y), 1)
