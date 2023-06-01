import pygame
import pygame_gui
import math

class SinusoidalGUI:
    def __init__(self, screen, width, height, amplitude, frequency, phase_shift, color):
        # Initialize pygame_gui
        self.manager = pygame_gui.UIManager((width, height))

        # Create a slider for amplitude
        amplitude_slider_rect = pygame.Rect(50, 50, 200, 20)
        self.amplitude_slider = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=amplitude_slider_rect,
            start_value=amplitude,
            value_range=(0, height),
            manager=self.manager
        )

        # Create a slider for frequency
        frequency_slider_rect = pygame.Rect(50, 100, 200, 20)
        self.frequency_slider = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=frequency_slider_rect,
            start_value=frequency,
            value_range=(0.01, 10),
            manager=self.manager
        )

        # Create a slider for phase shift
        phase_shift_slider_rect = pygame.Rect(50, 150, 200, 20)
        self.phase_shift_slider = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=phase_shift_slider_rect,
            start_value=phase_shift,
            value_range=(0, 2 * math.pi),
            manager=self.manager
        )

        # Create headings
        amplitude_heading_rect = pygame.Rect(50, 20, 100, 20)
        amplitude_heading = pygame_gui.elements.UILabel(
            relative_rect=amplitude_heading_rect,
            text="Amplitude",
            manager=self.manager
        )

        frequency_heading_rect = pygame.Rect(50, 80, 100, 20)
        frequency_heading = pygame_gui.elements.UILabel(
            relative_rect=frequency_heading_rect,
            text="Frequency",
            manager=self.manager
        )

        phase_shift_heading_rect = pygame.Rect(50, 130, 100, 20)
        phase_shift_heading = pygame_gui.elements.UILabel(
            relative_rect=phase_shift_heading_rect,
            text="Phase Shift",
            manager=self.manager
        )

        self.screen = screen
        self.width = width
        self.height = height
        self.color = color

    def handle_event(self, event):
        # Pass events to pygame_gui
        self.manager.process_events(event)

    def update(self, dt):
        # Update the GUI
        self.manager.update(dt)

    def draw(self):
        # Draw the GUI
        self.manager.draw_ui(self.screen)
