import curses
WELCOME_MSG = """
Welcome to snake!
            """
RULES = """
Eat the apple to increase the size of the snake and score points, if the snake
eats itself or hits the wall then game over.
            """
END_MSG = "You have quit the game!"
GAME_OVER_MSG = "Game Over!"
RETURN_MSG = "Press any key to return to menu"
OPPOSITES = {
             curses.KEY_RIGHT: curses.KEY_LEFT,
             curses.KEY_LEFT: curses.KEY_RIGHT,
             curses.KEY_UP: curses.KEY_DOWN,
             curses.KEY_DOWN: curses.KEY_UP,
        }
