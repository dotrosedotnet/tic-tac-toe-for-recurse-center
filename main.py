#! /usr/bin/env nix-shell
"""
runs script with nix-shell below to access python libraries in nixos
"""
#!nix-shell -i python3 -p "python3.withPackages(ps: [ ps.unicurses ps.pynput ])"

import curses
import math
import pprint
import random

# from pynput import keyboard
from pynput.keyboard import Controller, Key, Listener

"""
COMPONENTS

- screen
- windows
    - title
    - instructions/feedback/success state
    - two for player turns (one on each side declaring whose turn it is)
    - game board
        - create game board window so game grid (1,1) is at window grid (2,2) so that
          window grid can divide row and column by 2 to get game grid
- pad
- cursor
- squares
- user 'pieces' ('X' and 'O')
- grid

LOGIC

- grid is 3x3
- players take turns putting down an X or O
- players must take turn
- X and O are fixed to each player
- X and O must go on empty squares
- first player is randomized
- game ends when all squares are filled or player wins
- three in a row wins
  - label grid with row integer and column integer
  - player wins if pieces are:
      - all in the same column (adjacent first number, static second number ie [[1,1],[2,1],[3,1]])
      - all in the same row (static first number, adjacent second number ie [[1,1],[1,2],[1,3]])
      - diagonal
          - [(1,1) (2,2) (3,3)] or [(1,3) (2,2) (3,1)]
          - row and column are each three adjacent integers!

"""
# set up a quit function
# set up a title in a window
# set up a game board in a window
# set up directions in a window, which also announce game-winner/loser/tie

GAME_TITLE = "Tic-Tac-Toe"

GRID_SIDE_LENGTH = 3

PLAYERS = ["X", "Y"]


def make_title_win(game_title):
    """
    initiate, run, and close title window
    """
    title_win = newwin_horizontal_center(3, len(game_title) + 2, 1)
    title_win.clear()
    title_win.addstr(1, 1, game_title.strip())
    title_win.box()
    title_win.refresh()


def newwin_horizontal_center(height, width, begin_y):
    """
    creates window which is centered horizontally
    """
    center = int(
        (curses.COLS / 2) - (width / 2) - 1
    )  # why is there a magical '1' needed
    return curses.newwin(height, width, begin_y, center)


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


# pprint.pprint(grid_maker(3))
# print(grid_maker(3))


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


def win_center(height, width):
    """
    creates window centered on screen
    """
    v_center = int((curses.LINES / 2) - height / 2)
    h_center = int((curses.COLS / 2) - width / 2)
    return curses.newwin(height, width, v_center, h_center)


def center_text(text):
    """
    takes in strings and outputs x offset to center them
    """
    screen_center = curses.COLS / 2
    half_text = len(text) / 2
    x_position = int(screen_center - half_text)
    return x_position


def draw_cursor(grid_window):
    """
    makes cursor prettier hopefully
    """
    grin = grid_window
    curs_y, curs_x = grin.getyx()
    grin.addstr(curs_y - 1, curs_x - 1, "▄▄▄", 3)
    grin.move(curs_y, curs_x)


# TODO: draw and redraw grid need to be their own things so that my cool cursor can work. also I need to get on mapping the window grid to the game grid so that window grid cursor positions are bounced back as game grid coordinates in move data
# can I OVERLAY a cursor window on top of a player symbols window on top of the grid window?


def cursor_move_initialize(new_cursor_location):
    """
    takes in game grid coordinate for new location
    clears entire window
    prints grid in grid window
    prints grid state (who has what squares) over grid
    prints cursor at new location
    """


def move_cursor(grid_window):
    """
    controls cursor movement in grid
    I could simulate a full square cursor by writing ▓ chars to the cursor and surrounding spaces
    """
    grin = grid_window
    max_y, max_x = grin.getmaxyx()
    grin.move(2, 2)
    draw_cursor(grid_window)

    def on_key_press(key):
        if key == Key.left:
            Controller().press("h")
            Controller().release("h")
        if key == Key.down:
            Controller().press("j")
            Controller().release("j")
        if key == Key.up:
            Controller().press("k")
            Controller().release("k")
        if key == Key.right:
            Controller().press("l")
            Controller().release("l")
        if key == Key.esc:
            Controller().press("q")
            Controller().release("q")

    def on_key_release(
        key,
    ):  # this is doing nothing right now because I don't want to deal with it
        if key == Key.esc:
            return False

    listener = Listener(on_press=on_key_press, on_release=on_key_release)
    listener.start()

    def move_left():
        grin.move(curs_y, curs_x - 4)

    def move_down():
        grin.move(curs_y + 2, curs_x)

    def move_up():
        grin.move(curs_y - 2, curs_x)

    def move_right():
        grin.move(curs_y, curs_x + 4)

    while True:
        key = grin.getch()
        curs_y, curs_x = grin.getyx()
        if key == ord("h") or key == ord("a"):
            if curs_x <= 4:
                grin.move(curs_y, max_x - 4)
            else:
                move_left()
        if key == ord("j") or key == ord("s"):
            if curs_y >= max_y - 2:
                grin.move(1, curs_x)
            else:
                move_down()
        if key == ord("k") or key == ord("w"):
            if curs_y <= 2:
                grin.move(max_y - 2, curs_x)
            else:
                move_up()
        if key == ord("l") or key == ord("d"):
            if (
                curs_x >= max_x - 4
            ):  # this seems to work invariably, but needs an explanation why '4'?
                grin.move(curs_y, 2)
            else:
                move_right()
        draw_cursor(grid_window)


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


def choose_first_player(players):
    """
    flips coin to choose first player
    """
    return players[round(random.random())]


def calculate_grid_coordinates(side_length):
    """
    takes in side_length and outputs 2d array of square coordinates (ie [[1,1],[1,2],etc])
    """
    rows = []
    cols = []
    grid = []
    for n in range(1, side_length + 1):
        rows.append(n)
        cols.append(n)
    for x in rows:
        for y in cols:
            grid.append([x, y])
    return grid


def make_winning_combinations(grid_side_length):
    """
    takes in grid_side_length and outputs all winning square combinations
    """
    winning_moves = {"rows": [], "cols": [], "diags": []}
    for x in range(grid_side_length):
        for x in winning_moves:
            winning_moves[x].append([])
    # each permutation of:
    #   same first number, adjacent second number       (rows)
    for x in range(grid_side_length):
        for y in range(grid_side_length):
            winning_moves["rows"][x].append([y + 1, x + 1])
    #   adjacent first numbers, same second number      (columns)
    for y in range(grid_side_length):
        for x in range(grid_side_length):
            winning_moves["cols"][y].append([y + 1, x + 1])
    # adjacent first number, adjacent second number   (diagonals)
    # x and y both ascending
    for y in range(grid_side_length):
        winning_moves["diags"][0].append([y + 1, y + 1])
    # x ascending, y descending
    for y in range(grid_side_length):
        winning_moves["diags"][1].append([y + 1, grid_side_length - y])
    # diagonal only has two solutions, this removes empty lists in diagonals
    winning_moves["diags"] = list(filter(lambda a: a, winning_moves["diags"]))
    return winning_moves


def initialize_game_stats(players, grid_side_length):
    """
    takes in player list and grid size
    populates game stats with player dictionary and moves available
    player dictionaries include player symbol and empty moves_done list
    returns initial game_stats
    """
    game_stats = {"players": {}}
    for i, player in enumerate(players):
        game_stats["players"].update(
            {f"player_{i+1}": {"symbol": player, "moves_done": []}}
        )
    game_stats.update({"moves available": calculate_grid_coordinates(grid_side_length)})
    game_stats.update({"whose_turn": choose_first_player(players)})
    game_stats.update({"winner": []})
    return game_stats


def win_state(game_stats):
    """
    assigns win state to players or declares tie
    takes in game_stats
    presently returns game_stats which has win state added, but maybe should just win state?
    """
    for player in game_stats["players"]:
        if (
            game_stats["players"][player]["moves_done"]
            in make_winning_combinations(GRID_SIDE_LENGTH)["rows"]
            or game_stats["players"][player]["moves_done"]
            in make_winning_combinations(GRID_SIDE_LENGTH)["cols"]
            or game_stats["players"][player]["moves_done"]
            in make_winning_combinations(GRID_SIDE_LENGTH)["diags"]
        ):
            game_stats["winner"].append(player)
        if len(game_stats["players"][player]["moves_done"]) == len(
            calculate_grid_coordinates(GRID_SIDE_LENGTH)
        ):
            game_stats["winner"].append("TIE!")
    return game_stats


# print(win_state(initialize_game_stats(PLAYERS, GRID_SIDE_LENGTH)))


def grid_map(grid_side_length):
    """
    takes in grid coordinates
    maps them to grid window
    """


def moving_on_grid(game_stats):
    """
    logic for moving cursor on grid
    idea:
        <-> moves to next/prev row on edge boundary
        up/down stays in same column on edge boundary?
    """


def inputting_move():
    """
    fills square with player's symbol on 'Enter' press
    adds move to player's move list
    removes square from moves available
    """


def one_round(game_stats):
    """
    takes in game_stats (player symbols, player moves done, moves available, whose turn)
    initializes cursor
    takes in move
    switches player
    returns dictionary of moves completed
    """


def main(stdscr: "curses._CursesWindow"):
    """
    it's the main show baby
    """
    # Clear screen
    stdscr.clear()

    make_title_win(GAME_TITLE)

    make_grid_win(grid_maker(GRID_SIDE_LENGTH))

    # stdscr.refresh()
    # stdscr.getkey()


if __name__ == "__main__":
    curses.wrapper(main)
