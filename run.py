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
    

    snake = [[height//2, width//2+1], [height//2, width//2], [height//2, width//2-1]]
    direction = curses.KEY_RIGHT

    for y,x in snake:
        screen.addstr(y, x, "#")

    screen.getch()


curses.wrapper(main)

