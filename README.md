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

You might’ve noticed the pass keyword. pass is a unique statement in Python that does nothing. It can be used as a placeholder for future code. Nothing happens when the pass statement is executed, but you avoid getting an error when empty code is not allowed. In the context of this project, it's used in the class skeleton to indicate where you need to add your method implementations.

Your first task is to define the initial state of your GameOfLife class. You must use the provided skeleton as a guide to implement the __init__ method (the class constructor).

In this method, you'll set up the initial game state—an empty grid with dimensions x_dim by y_dim. For this project, we'll represent this grid as a 2D list, with each element being either a 0 or a 1. A 0 illustrates a dead cell, and a 1 represents a live cell. All cells should be dead at the start, so your grid should be filled with zeros.

Good luck with your first step into bringing the Game of Life to... life.
