from os import system
import random
import cursor
import curses
from curses import textpad
from simple_term_menu import TerminalMenu
from constants import (
    WELCOME_MSG,
    RULES,
    END_MSG,
    GAME_OVER_MSG,
    RETURN_MSG,
    OPPOSITES,
)


# Main menu options
def main():
    choice = None

    while choice != "Exit":
        print(WELCOME_MSG)
        choice = display_main_menu()
        if choice == "Play":
            curses.wrapper(main_body)
        elif choice == "Rules":
            print(RULES)
            terminal_menu = TerminalMenu(["Return"])
            terminal_menu.show()
        system("clear")
    print(END_MSG)


# Display for the main menu
def display_main_menu():
    options = ["Play", "Rules", "Exit"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    return options[menu_entry_index]


def food_object(snake, container):
    """
    Function to place food inside the game container and not the body of
    the snake
    """
    food = None
    while food is None:
        food_y = random.randint(container[0][0] + 1, container[1][0] - 4)
        food_x = random.randint(container[0][1] + 1, container[1][1] - 4)
        food = [food_y, food_x]

        if food in snake:
            food = None
    return food


# Display score
def show_score(screen, score):
    score_display = "score: {}".format(score)
    width = curses.COLS
    screen.addstr(1, width // 2 - len(score_display) // 2, score_display)
    screen.refresh()


def game_over(
    snake,
    height,
    width,
    screen,
    upper_left_x,
    upper_left_y,
    lower_right_x,
    lower_right_y,
):
    has_hit_wall = snake[0][0] in [upper_left_y, lower_right_y] or snake[0][
        1
    ] in [upper_left_x, lower_right_x]
    has_hit_snake = snake[0] in snake[1:]

    if has_hit_wall or has_hit_snake:
        screen.addstr(
            height // 3, width // 2 - len(GAME_OVER_MSG) // 2, GAME_OVER_MSG
        )
        screen.addstr(
            height // 2, width // 2 - len(RETURN_MSG) // 2, RETURN_MSG
        )
        screen.nodelay(0)
        screen.getch()
        screen.clear()
        return True
    return False


def main_body(screen):
    cursor.hide()
    screen.nodelay(1)
    screen.timeout(160)

    height, width = screen.getmaxyx()
    # container coordinates
    upper_left_y = 2
    upper_left_x = 2
    lower_right_y = height - 2
    lower_right_x = width - 2
    container = [[upper_left_y, upper_left_x], [lower_right_y, lower_right_x]]
    textpad.rectangle(
        screen, upper_left_y, upper_left_x, lower_right_y, lower_right_x
    )

    # Snake starting position and direction
    snake = [
        [height // 2, width // 2 + 1],
        [height // 2, width // 2],
        [height // 2, width // 2 - 1],
    ]
    direction = curses.KEY_RIGHT
    blocked_key = curses.KEY_LEFT

    # Add snake
    for y, x in snake:
        screen.addstr(y, x, "#")

    # Add food
    food = food_object(snake, container)
    screen.addstr(food[0], food[1], "*")

    # Score
    score = 0
    show_score(screen, score)
    while True:

        key = screen.getch()

        # set direction when arrow key is pressed
        if key in [
            curses.KEY_RIGHT,
            curses.KEY_LEFT,
            curses.KEY_UP,
            curses.KEY_DOWN,
        ]:
            direction = key

        if direction == blocked_key:
            direction = OPPOSITES[direction]

        # next position of new snake head when snake moves
        head = snake[0]
        if direction == curses.KEY_RIGHT:
            next_head = [head[0], head[1] + 1]
        elif direction == curses.KEY_LEFT:
            next_head = [head[0], head[1] - 1]
        elif direction == curses.KEY_DOWN:
            next_head = [head[0] + 1, head[1]]
        elif direction == curses.KEY_UP:
            next_head = [head[0] - 1, head[1]]

        blocked_key = OPPOSITES[direction]

        # prints new head
        snake.insert(0, next_head)
        screen.addstr(next_head[0], next_head[1], "#")

        # Increase size of snake when food object is eaten
        if snake[0] == food:
            food = food_object(snake, container)
            screen.addstr(food[0], food[1], "*")
            score += 1
            show_score(screen, score)
        else:
            screen.addstr(snake[-1][0], snake[-1][1], " ")
            snake.pop()

        # Game over when wall is hit
        is_game_over = game_over(
            snake,
            height,
            width,
            screen,
            upper_left_x,
            upper_left_y,
            lower_right_x,
            lower_right_y,
        )

        if is_game_over:
            break

    screen.refresh()


if __name__ == "__main__":
    main()
