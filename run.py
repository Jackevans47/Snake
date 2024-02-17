import curses
from curses import textpad


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

        screen.refresh()





curses.wrapper(main)

