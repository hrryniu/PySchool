import curses #pozwala modyfikować terminal
from curses import wrapper

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the Speed Typing Test!")
    stdscr.addstr("\nPress any key to begin!")
    stdscr.refresh()
    stdscr.gotkey()

def wpm_test(stdscr):
    target_text = "Hello world this is some test text for this app!"
    current_text =[]
    stdscr.clear()
    stdscr.addstr(target_text)
    stdscr.refresh()


def main(stdscr): #standart screen
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)
    wpm_test(stdscr)

wrapper(main)

