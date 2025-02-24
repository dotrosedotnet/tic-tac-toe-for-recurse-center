#! /usr/bin/env nix-shell
"""
runs script with nix-shell below to access python libraries in nixos
"""
#!nix-shell -i python3 -p "python3.withPackages(ps: [ ps.unicurses ps.pynput ])"

import curses


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
