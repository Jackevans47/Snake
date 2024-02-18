import curses
from curses import textpad
from random import randint


def next():
    print()

def food():
    print()

def game_over():
    print()


def main(screen):
    """
    Game area
    """
    curses.curs_set(0)
    screen.nodelay(1)
    screen.timeout(160)

    height,width = screen.getmaxyx()
    box = [[2,2], [height-2, width-2]]
    textpad.rectangle(screen, box[0][0], box[0][1], box[1][0], box[1][1])
    
    """
    Snake starting position and direction
    """
    snake = [[height//2, width//2+1], [height//2, width//2], [height//2, width//2-1]]
    direction = curses.KEY_RIGHT

    """
    Snake
    """
    for y,x in snake:
        screen.addstr(y, x, "#")
    
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
        screen.addstr(next_head[0], next_head[1], '#')

        # removes old head when snake is moving
        screen.addstr(snake[-1][0], snake[-1][1], ' ')
        snake.pop()

        # Game overc when wall is hit

        if (snake[0][0] in [box[0][0], box[1][0]] or 
			snake[0][1] in [box[0][1], box[1][1]] or 
			snake[0] in snake[1:]):
            msg = "Game Over!"
            screen.addstr(height//2, width//2-len(msg)//2, msg)
            screen.nodelay(0)
            screen.getch()
            break

    screen.refresh()

curses.wrapper(main)

