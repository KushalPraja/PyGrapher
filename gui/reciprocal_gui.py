import pygame
import pygame_gui


class ReciprocalGUI:
    def __init__(self, screen, width, height, k, d, color):
        # Initialize pygame_gui
        self.manager = pygame_gui.UIManager((width, height))

        # Create a slider for k
        k_slider_rect = pygame.Rect(50, 50, 200, 20)
        self.k_slider = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=k_slider_rect,
            start_value=k,
            value_range=(-100, 100),
            manager=self.manager
        )

        # Create a slider for d
        d_slider_rect = pygame.Rect(50, 100, 200, 20)
        self.d_slider = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=d_slider_rect,
            start_value=d,
            value_range=(-10, 10),
            manager=self.manager
        )

        # Create headings
        k_heading_rect = pygame.Rect(50, 20, 100, 20)
        k_heading = pygame_gui.elements.UILabel(
            relative_rect=k_heading_rect,
            text="k",
            manager=self.manager
        )

        d_heading_rect = pygame.Rect(50, 80, 100, 20)
        d_heading = pygame_gui.elements.UILabel(
            relative_rect=d_heading_rect,
            text="d",
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
