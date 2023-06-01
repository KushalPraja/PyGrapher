import pygame
import pygame_gui

class CubicGUI:
    def __init__(self, screen, width, height, color, scale):
        # Initialize pygame_gui
        self.manager = pygame_gui.UIManager((width, height))

        # Create a slider for a, b, c, and d coefficients
        a_slider_rect = pygame.Rect(50, 50, 200, 20)
        self.a_slider = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=a_slider_rect,
            start_value=0,
            value_range=(-10, 10),  # Increase the range to -10 to 10
            manager=self.manager
        )

        b_slider_rect = pygame.Rect(50, 100, 200, 20)
        self.b_slider = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=b_slider_rect,
            start_value=0,
            value_range=(-10, 10),  # Increase the range to -10 to 10
            manager=self.manager
        )

        c_slider_rect = pygame.Rect(50, 150, 200, 20)
        self.c_slider = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=c_slider_rect,
            start_value=0,
            value_range=(-10, 10),  # Increase the range to -10 to 10
            manager=self.manager
        )

        d_slider_rect = pygame.Rect(50, 200, 200, 20)
        self.d_slider = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=d_slider_rect,
            start_value=0,
            value_range=(-10, 10),  # Increase the range to -10 to 10
            manager=self.manager
        )

        scale_slider_rect = pygame.Rect(50, 250, 200, 20)
        self.scale_slider = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=scale_slider_rect,
            start_value=50,
            value_range=(0, 100),
            manager=self.manager
        )

        # Create headings
        a_heading_rect = pygame.Rect(50, 20, 100, 20)
        a_heading = pygame_gui.elements.UILabel(
            relative_rect=a_heading_rect,
            text="a",
            manager=self.manager
        )

        b_heading_rect = pygame.Rect(50, 80, 100, 20)
        b_heading = pygame_gui.elements.UILabel(
            relative_rect=b_heading_rect,
            text="b",
            manager=self.manager
        )

        c_heading_rect = pygame.Rect(50, 130, 100, 20)
        c_heading = pygame_gui.elements.UILabel(
            relative_rect=c_heading_rect,
            text="c",
            manager=self.manager
        )

        d_heading_rect = pygame.Rect(50, 180, 100, 20)
        d_heading = pygame_gui.elements.UILabel(
            relative_rect=d_heading_rect,
            text="d",
            manager=self.manager
        )

        scale_heading_rect = pygame.Rect(50, 230, 100, 20)
        scale_heading = pygame_gui.elements.UILabel(
            relative_rect=scale_heading_rect,
            text="Scale",
            manager=self.manager
        )

        self.screen = screen
        self.width = width
        self.height = height
        self.color = color
        self.scale = scale

    def handle_event(self, event):
        # Pass events to pygame_gui
        self.manager.process_events(event)

    def update(self, dt):
        # Update the GUI
        self.manager.update(dt)

    def draw(self):
        # Draw the GUI
        self.manager.draw_ui(self.screen)