import curses
from curses import textpad
import random
from simple_term_menu import TerminalMenu

def main():
    choice = None
    while choice != "Exit":
        choice = display_main_menu()
        if choice == "Play":    
            curses.wrapper(main_body)
            print("Game Over")
        elif choice == "Rules":
            print("rules")
            terminal_menu = TerminalMenu(["Return"])
            terminal_menu.show()


def display_main_menu():
    options = ["Play", "Rules", "Exit"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    print(f"You have selected {options[menu_entry_index]}!")
    return options[menu_entry_index]

def food_object(snake, container):
    """ Function to place food inside the game container and not the body of 
    the snake
    """
    food = None
    while food is None:
        food = [random.randint(container[0][0]+1, container[1][0]-1),
		random.randint(container[0][1]+1, container[1][1]-1)]
        if food in snake:
            food = None
    return food

# Display score
def show_score(screen, score):
    score_display = "score: {}".format(score)
    height, width = screen.getmaxyx()
    screen.addstr(1, width//2 - len(score_display)//2, score_display)
    screen.refresh()

def game_over():
    print()


def main_body(screen):
    """
    Game area
    """
    curses.curs_set(0)
    screen.nodelay(1)
    screen.timeout(160)


    height,width = screen.getmaxyx()
    container = [[2,2], [height-2, width-2]]
    textpad.rectangle(screen, container[0][0], container[0][1], container[1][0], container[1][1])
    
    """
    Snake starting position and direction
    """
    snake = [[height//2, width//2+1], [height//2, width//2], [height//2, width//2-1]]
    direction = curses.KEY_RIGHT

    # Snake

    for y,x in snake:
        screen.addstr(y, x, "#")

    # Food
    food = food_object(snake, container)
    screen.addstr(food[0], food[1], '\U0001F34E')

    # Score
    score = 0
    show_score(screen, score)
    
    while 1:

        key = screen.getch()
        
        
        # set direction when arrow key is pressed
        if key in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP, curses.KEY_DOWN]:
            direction = key

        # next position of new snake head when snake moves
        head = snake[0]
        if direction == curses.KEY_RIGHT:
            next_head = [head[0],head[1]+1]
        elif direction == curses.KEY_LEFT:
            next_head = [head[0], head[1]-1]
        elif direction == curses.KEY_DOWN:
            next_head = [head[0]+1, head[1]]
        elif direction == curses.KEY_UP:
            next_head = [head[0]-1, head[1]]


        # prints new head
        snake.insert(0, next_head)
        screen.addstr(next_head[0], next_head[1], "#")

        # Increase size of snake when food object is eaten
        if snake[0] == food:
            food = food_object(snake, container)
            screen.addstr(food[0], food[1], '\U0001F34E')
            score += 1
            show_score(screen, score)
        else:
            screen.addstr(snake[-1][0], snake[-1][1], ' ')
            snake.pop()

        # Game over when wall is hit
        if (snake[0][0] in [container[0][0], container[1][0]] or 
			snake[0][1] in [container[0][1], container[1][1]] or 
			snake[0] in snake[1:]):
            game_over_msg = "Game Over!"
            return_msg = "Press any key to return to menu"
            screen.addstr(height//3, width//2-len(game_over_msg)//2, game_over_msg)
            screen.addstr(height//2, width//2-len(return_msg)//2, return_msg)
            screen.nodelay(0)
            screen.getch()
            screen.clear()
            break

    screen.refresh()


if __name__ == "__main__":
    main()

