import curses #pozwala modyfikować terminal
from curses import wrapper

def main(stdscr): #standart screen
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    stdscr.clear()
    stdscr.addstr("Hello World!")  #dodajemy tutaj printy inputy inaczaj. musimy używać funkcji z biblioteki cusrses
    stdscr.refresh()
    stdscr.getkey()

