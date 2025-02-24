#! /usr/bin/env nix-shell
"""
runs script with nix-shell below to access python libraries in nixos
"""
#!nix-shell -i python3 -p "python3.withPackages(ps: [ ps.unicurses ps.pynput ])"

import curses
import math


def grid_maker(grid_side_length):
    """
    takes in grid_side_length and outputs grid in a multiline string
    grid rows have a height of two, and then add one height bottom
    columns have width of four, and then add right side
    """
    char_rows = []
    text_rows = []
    grid_string = """"""
    # print first column to each row
    while len(char_rows) < grid_side_length * 2 + 1:
        char_rows.append([])
    for i, row in enumerate(char_rows):
        if i == 0:
            row.append("┌")
        elif i == grid_side_length * 2:
            row.append("└")
        elif i % 2 == 0:
            row.append("├")
        else:
            row.append("│")
    # print following columns for each grid_side_length until last
    for n in range(grid_side_length * 2):
        if n == grid_side_length * 2 - 1:  # magic number '1' needs explanation
            for i, row in enumerate(char_rows):
                if i == 0:
                    row.append("┐")
                elif i == grid_side_length * 2:
                    row.append("┘")
                elif i % 2 == 0:
                    row.append("┤")
                else:
                    row.append("│")
        if n % 2 == 0:
            for i, row in enumerate(char_rows):
                if i % 2 == 0:
                    row.append("───")
                else:
                    row.append("   ")
            for i, row in enumerate(char_rows):
                if n != grid_side_length * 2 - 2:  # magic number '2' needs explanation
                    if i == 0:
                        row.append("┬")
                    elif i == grid_side_length * 2:
                        row.append("┴")
                    elif i % 2 == 0:
                        row.append("┼")
                    else:
                        row.append("│")
    for row in char_rows:
        text_rows.append("".join(row))
    grid_string = "\n".join(text_rows)
    return grid_string


def calc_grid_height(grid):
    """
    calculates grid's height for use in window maker
    """
    return grid.count("\n") + 1


def calc_grid_width(grid):
    """
    calculates grid's width for use in window maker
    """
    return math.ceil(len(grid) / (grid.count("\n") + 1))


def draw_cursor(grid_window):
    """
    makes cursor prettier hopefully
    """
    grin = grid_window
    curs_y, curs_x = grin.getyx()
    grin.addstr(curs_y - 1, curs_x - 1, "▄▄▄", 3)
    grin.move(curs_y, curs_x)


def move_cursor(grid_window):
    """
    controls cursor movement in grid
    I could simulate a full square cursor by writing ▓ chars to the cursor and surrounding spaces
    """
    grin = grid_window
    max_y, max_x = grin.getmaxyx()
    grin.move(2, 2)
    draw_cursor(grid_window)


def win_center(height, width):
    """
    creates window centered on screen
    """
    v_center = int((curses.LINES / 2) - height / 2)
    h_center = int((curses.COLS / 2) - width / 2)
    return curses.newwin(height, width, v_center, h_center)


def make_grid_win(grid):
    """
    calculates and creates window that displays game's grid
    will contain subroutines for gameplay
    """
    grid_height = calc_grid_height(grid) + 1
    grid_width = calc_grid_width(grid)
    grid_win = win_center(grid_height, grid_width)
    grid_win.clear()
    grid_win.addstr(1, 0, grid.strip())
    move_cursor(grid_win)
    grid_win.refresh()
    grid_win.getkey()


def start(stdscr):
    """
    testing window overlays
    """
    stdscr.nodelay(False)
    curses.curs_set(False)
    stdscr.refresh()

    grid_win = curses.newwin(6, 6)
    moves_win = curses.newwin(6, 6)
    grid_win.border()
    moves_win.refresh()
    grid_win.refresh()

    stdscr.getch()  # prints 'nu'

    moves_win.addnstr(2, 2, "nu", 2)
    moves_win.overlay(grid_win)
    moves_win.refresh()

    stdscr.getch()  # prints another 'nu'

    # grid_win.refresh()

    moves_win.addnstr(4, 2, "nu", 2)
    # moves_win.overlay(grid_win) # without this a grid_win removes the above string!

    # stdscr.getch()

    moves_win.refresh()  # prints moves

    # stdscr.getch()

    # grid_win.refresh()
    stdscr.getch()

    grid_win.refresh()  # this only clears the last string added if moves_win is NOT declared as 'overlaid' to grid_win before last moves_win.refresh())

    stdscr.getch()


curses.wrapper(start)
