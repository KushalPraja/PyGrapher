import pygame
import pygame_gui

class ParabolaGUI:

    def __init__(self, screen, width, height, slope, y_intercept, color):
        # Initialize pygame_gui
        self.manager = pygame_gui.UIManager((width, height))

        # Create a slider for slope
        slope_slider_rect = pygame.Rect(50, 50, 200, 20)
        self.slope_slider = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=slope_slider_rect,
            start_value=slope,
            value_range=(-10, 10),
            manager=self.manager
        )

        # Create a slider for y-intercept
        y_intercept_slider_rect = pygame.Rect(50, 100, 200, 20)
        self.y_intercept_slider = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=y_intercept_slider_rect,
            start_value=y_intercept,
            value_range=(-100, 100),
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
       
