# Instruction
This is a Python code for a game called "Nu, pogodi!" or "Catch the egg!" in English. It uses the Pygame library to create a graphical interface and game mechanics.

The game consists of a wolf character holding a basket, and eggs falling from four different positions on the screen. The player must move the basket to catch the eggs while avoiding "losses," which are essentially bombs that fall from the same positions as the eggs. The game ends when the player misses three eggs, and the score is displayed on the screen.

The code begins by importing the necessary libraries and defining a function to display text on the screen. It then initializes Pygame, sets up the screen, loads images and music, and sets up variables and positions for the game elements.

The game loop is run with a while statement, which continues until the player quits the game by closing the window. The loop handles events, such as keyboard input for moving the basket, and updates the game state, such as the position of the eggs and the score.

When the player misses three eggs, the game over function is called, which displays the final score and saves the top score in a file if it is higher than the previous top score.

Overall, this code creates a simple but entertaining game using Pygame.
