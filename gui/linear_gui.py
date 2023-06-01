import pygame
import pygame_gui

class LinearGUI:
    def __init__(self, screen, width, height, color, scale):
        # Initialize pygame_gui
        self.manager = pygame_gui.UIManager((width, height))

        # Create a slider for slope
        slope_slider_rect = pygame.Rect(50, 50, 200, 20)
        self.slope_slider = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=slope_slider_rect,
            start_value=0,
            value_range=(0.1, 10),
            manager=self.manager
        )

        # Create a slider for y-intercept
        y_intercept_slider_rect = pygame.Rect(50, 100, 200, 20)
        self.y_intercept_slider = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=y_intercept_slider_rect,
            start_value=0,
            value_range=(-10, 10),
            manager=self.manager
        )

        scale_slider_rect = pygame.Rect(50, 150, 200, 20)
        self.scale_slider = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=scale_slider_rect,
            start_value=1,
            value_range=(0.1, 10),
            manager=self.manager
        )

        # Create headings
        slope_heading_rect = pygame.Rect(50, 20, 100, 20)
        slope_heading = pygame_gui.elements.UILabel(
            relative_rect=slope_heading_rect,
            text="Slope",
            manager=self.manager
        )

        y_intercept_heading_rect = pygame.Rect(50, 80, 100, 20)
        y_intercept_heading = pygame_gui.elements.UILabel(
            relative_rect=y_intercept_heading_rect,
            text="Y-Intercept",
            manager=self.manager
        )

        scale_heading_rect = pygame.Rect(50, 130, 100, 20)
        scale_heading = pygame_gui.elements.UILabel(
            relative_rect=scale_heading_rect,
            text="Scale",
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
