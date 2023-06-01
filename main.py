import pygame
import sys
import pygame_gui
from pygame.locals import *
from gui.parabola_gui import ParabolaGUI
from gui.linear_gui import LinearGUI
from gui.cubic_gui import CubicGUI
from gui.start_screen import start_screen
from gui.sinusoidal_gui import SinusoidalGUI
from logic.parabola_logic import draw_parabola
from logic.linear_logic import draw_line
from logic.cubic_logic import draw_cubic
from logic.sinusoidal_logic import draw_sinusoidal
from gui.reciprocal_gui import ReciprocalGUI
from logic.reciprocal_logic import draw_reciprocal

# Initialize Pygame
pygame.init()

# Set up the screen
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("PyGrapher")

# Set up colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (255, 165, 0)
DARK_GREY = (64, 70, 84)




# Set up the time increment
dt = 0.1

# Create the ParabolaGUI instance
parabola_gui = ParabolaGUI(screen, width, height, 0.05, 0, BLUE)
# Create the LinearGUI instance
linear_gui = LinearGUI(screen, width, height, GREEN, scale=0.05)
# Create the CubicGUI instance
cubic_gui = CubicGUI(screen, width, height, RED, scale=0.05)
# Create the SinusoidalGUI instance
sinusoidal_gui = SinusoidalGUI(screen, width, height, 100, 0.01, 0, ORANGE)
# Create the ReciprocalGUI instance
reciprocal_gui = ReciprocalGUI(screen, width, height, 1, 0, BLACK)
# Create the font
font = pygame.font.Font("Fonts/Lato-Regular.ttf", 20)

# Drop-down menu options
function_options = {
    "Parabola": parabola_gui,
    "Linear": linear_gui,
    "Cubic": cubic_gui,
    "Sinusoidal": sinusoidal_gui,
    "Reciprocal": reciprocal_gui
}

# Create the manager
manager = pygame_gui.UIManager((width, height))

# Create the drop-down menu
menu_rect = pygame.Rect(width - 200, 0, 200, 30)
menu_options = list(function_options.keys())
menu = pygame_gui.elements.ui_drop_down_menu.UIDropDownMenu(
    options_list=menu_options,
    starting_option=menu_options[0],
    relative_rect=menu_rect,
    manager=manager
)

# Create the button for switching between dark and light mode
button_rect = pygame.Rect(width - 200, height - 60, 200, 30)
button = pygame_gui.elements.UIButton(
    relative_rect=button_rect,
    text="Dark Mode",
    manager=manager
)

# Global variable for background color
background_color = WHITE

# Main game loop
def main():
    tracer = parabola_gui

    clock = pygame.time.Clock()

    global background_color  # Declare background_color as a global variable

    while True:
        time_delta = clock.tick(60) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                    selected_option = event.text

                    if selected_option in function_options:
                        tracer = function_options[selected_option]

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if button.rect.collidepoint(event.pos):
                        if button.text == "Dark Mode":
                            background_color = DARK_GREY
                            button.text = "Light Mode"
                        else:
                            background_color = WHITE
                            button.text = "Dark Mode"

            manager.process_events(event)

            # Pass events to the active tracer
            tracer.handle_event(event)

        manager.update(time_delta)

        # Clear the screen
        screen.fill(background_color)

        # Update the tracer
        tracer.update(dt)

        # Draw the tracer
        if isinstance(tracer, ParabolaGUI):
            draw_parabola(screen, width, height, tracer.slope_slider.get_current_value(), tracer.y_intercept_slider.get_current_value(), tracer.color)
        elif isinstance(tracer, LinearGUI):
            draw_line(screen, width, height, tracer.slope_slider.get_current_value(), tracer.y_intercept_slider.get_current_value(), tracer.color, tracer.scale_slider.get_current_value())
        elif isinstance(tracer, CubicGUI):
            draw_cubic(screen, width, height, tracer.a_slider.get_current_value(), tracer.b_slider.get_current_value(), tracer.c_slider.get_current_value(), tracer.d_slider.get_current_value(), tracer.color, tracer.scale_slider.get_current_value())
        elif isinstance(tracer, SinusoidalGUI):  
            draw_sinusoidal(screen, width, height, tracer.amplitude_slider.get_current_value(), tracer.frequency_slider.get_current_value(), tracer.phase_shift_slider.get_current_value(), tracer.color)
        elif isinstance(tracer, ReciprocalGUI):
            draw_reciprocal(screen, width, height, tracer.k_slider.get_current_value(), tracer.d_slider.get_current_value(), tracer.color)

        # Draw the GUI
        tracer.draw()

        # Render and display the equations
        if isinstance(tracer, ParabolaGUI):
            equation = f"y = {tracer.slope_slider.get_current_value():.2f}x^2 + {tracer.y_intercept_slider.get_current_value():.2f}"
        elif isinstance(tracer, LinearGUI):
            equation = f"y = {tracer.slope_slider.get_current_value():.2f}x + {tracer.y_intercept_slider.get_current_value():.2f}"
        elif isinstance(tracer, CubicGUI):
            equation = f"y = {tracer.a_slider.get_current_value():.2f}x^3 + {tracer.b_slider.get_current_value():.2f}x^2 + {tracer.c_slider.get_current_value():.2f}x + {tracer.d_slider.get_current_value():.2f}"
        elif isinstance(tracer, SinusoidalGUI):
            amplitude = tracer.amplitude_slider.get_current_value()
            frequency = tracer.frequency_slider.get_current_value()
            equation = f"y = {amplitude:.2f} * sin({frequency:.2f}x)"
        elif isinstance(tracer, ReciprocalGUI):
            equation = f"y = {tracer.k_slider.get_current_value():.2f} / x + {tracer.d_slider.get_current_value():.2f}"
        else:
            equation = ""

        equation_text = font.render(equation, True, BLACK)
        equation_rect = equation_text.get_rect()
        equation_rect.bottomleft = (30, height - 50)  # Position at the bottom left with 20 pixels padding
        screen.blit(equation_text, equation_rect.bottomleft)

        manager.draw_ui(screen)

        # Update the display
        pygame.display.update()


if __name__ == '__main__':
    start_screen()
    main()
