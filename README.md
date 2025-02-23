# Terminal Tic Tac Toe

Having too much fun coding tic-tac-toe for my application for the Recurse Center.

I'm a 39 year old career switcher focusing on transitioning from life as a musician to life as a coder.

I tried to implement this with some OOP but I keep being turned off by the connection between objects and state.

So I'm mostly sticking to functions and seeing how this works out. It's exhilerating!

## Mighta gone overboard with this

My curious tic tac toe implementation (aspirationally) includes:

- [x] a TUI
  - [x] controllable by WASD, vi bindings, and arrows
  - [ ] current player and win-state indicators
- [x] square grid of variable size
  - [ ] size stipulated by command argument (presently in global variable)
- [x] rules which follow the size of the grid
- [ ] variable player quantity
  - [ ] stipulated by command argument

## Urgent TODO

- map curses window grid onto game grid, so that each square has its' own coordinate
  - this will make win-states calculable
- win-states lol
- putting down moves!

## what I'm presently distracted by

### making the cursor fill the whole square, which is a retained mode PITA

before I can modify the cursor effectively I need to make sure that the grid is redrawn behind it (and the marked squares) on every move, and that the old cursor position is removed. fun! lol just a bit more than I expected
