
--------------
PyGrapher
--------------

Description:
This project is a graphical tracer application that allows you to draw and visualize various mathematical functions, including parabolas, lines, and cubic curves. It provides a user-friendly interface for adjusting parameters and displays the equations of the curves on the screen.

Features:
- Draw parabolas, lines, and cubic curves on a graphical canvas.
- Adjust parameters such as slope, y-intercept, coefficients, and scale.
- Real-time rendering of curves as parameters are changed.
- Display equations of the curves on the screen.
- Save the equations to a text file for further analysis.

Requirements:
- Python 3.x
- Pygame library

Installation:
1. Clone or download the project files from the GitHub repository: [repository URL]
2. Make sure you have Python 3.x installed on your system.
3. Install the required dependencies by running the following command in your terminal:


Usage:
1. Open a terminal or command prompt and navigate to the project directory.
2. Run the `main.py` file using the following command:
3. The graphical tracer application will open in a new window.
4. Use the following keys to switch between different curve types:
- Press "p" for parabolas.
- Press "l" for lines.
- Press "c" for cubic curves.
5. Adjust the parameters using the user interface controls provided on the screen.
6. The equations for the currently displayed curve will be written to the "equations.txt" file every 5 seconds.

Additional Notes:
- The `main.py` file contains the main program logic and handles user input and drawing of curves using the Pygame library.
- The `equation_writer.py` file runs in a separate thread and updates the equations in the `equations.txt` file every 5 seconds.
- The `parabola_gui.py`, `linear_gui.py`, and `cubic_gui.py` files contain the graphical user interface classes for each curve type.
- The `parabola_logic.py`, `linear_logic.py`, and `cubic_logic.py` files contain the logic for drawing the curves.
- The `equations.txt` file will be created in the project directory and will contain the equations for the curves.
- Feel free to modify the code and customize the user interface and functionality to suit your needs.

Author:
[ Kushal Prajapati ]
[ Kushpraja6@gmail.com ]
