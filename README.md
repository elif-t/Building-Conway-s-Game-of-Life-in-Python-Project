# Building-Conway-s-Game-of-Life-in-Python-Project

## 1. Create the Class and Its __init__ Method
Conway’s Game of Life is a zero-player game requiring only an initial state and no further input. It occurs on a grid of square cells, each in one of two possible states: live or dead.

IMG_1_1

Every cell interacts with its eight neighbors (horizontally, vertically, or diagonally adjacent cells).

IMG_1_2

Starting at the initial state, the neighbors interact according to the following rules:

* Any live cell with two or three live neighbors survives. Otherwise, a cell dies due to loneliness (with no or only one neighbor) or overpopulation (with four or more neighbors).
* Any dead cell with (exactly) three live neighbors becomes a live cell. A dead cell with any other number of neighbors remains dead.

IMG_1_3

In this project, we will implement Conway’s Game of Life in Python.

The skeleton of your project includes the following:

```
class GameOfLife(object):  
    
    def __init__(self, x_dim, y_dim):
        # Initialize a 2D list with dimensions x_dim by y_dim filled with zeros.
        pass
    
    def get_grid(self):
        # Implement a getter method for your grid.
        pass

    def print_grid(self):
        # Implement a method to print out your grid in a human-readable format.
        pass

    def populate_grid(self, coord):
        # Given a list of 2D coordinates (represented as tuples/lists with 2 elements each),
        # set the corresponding elements in your grid to 1.
        pass

    def make_step(self):
        # Implement the logic to update the game state according to the rules of Conway's Game of Life.
        pass

    def make_n_steps(self, n):
        # Implement a method that applies the make_step method n times.
        pass

    def draw_grid(self):
        # Draw the current state of the grid.
        pass
```

