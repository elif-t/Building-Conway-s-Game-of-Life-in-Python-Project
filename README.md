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

## 2.Create a Method to Return the Grid
Now that you have successfully initialized your grid in the constructor, your next task is implementing a method named get_grid() to return this grid. This method is simple yet crucial for accessing the game’s current state outside the class.

## 3.Create a Method to Print the Grid
Your game is starting to take shape. Now that you can create and retrieve your grid, it would be helpful to visualize it. This is where the print_grid() method comes into play. This method will print your current game grid in a user-friendly way, making it easier to track the progress of the game.

IMG_3_1

## 4.Create a Method to Populate the Grid
So far, we’ve created the constructor of our project and implemented a getter that returns the grid object and a print method that prints the grid on the screen.

The next task is to implement the populate_grid() method, which allows you to initialize the game state by specifying which cells in the grid should start as ‘alive’ (represented by a 1). This will help set the stage for the Game of Life. The method should take the argument coord which is a list of tuples, where each tuple represents the coordinates [in the format (row, column)] of a cell that should be marked as ‘alive.’

Note that this is the only instance of the game where we can intervene and change the outcome by choosing which cells on the grid start as alive and which ones as dead. After executing this step, the initial state evolves according to the game’s rules, and no further user input is required.

## 5.Create a Method to Make a Step in the Game of Life
Now that the grid is populated with live cells, we must create a method that advances in the Game of Life. We’ll start with a technique that moves only a single step; call it make_step(). It should iterate over each cell in the grid, evaluate its neighbors, and update the cell's state based on the Game of Life rules.

## 6.Create a Method to Make n Steps in the Game of Life
You’ve done most of the work by implementing the make_step method. Your next task is creating a new one, make_n_steps, designed to simulate the Game of Life for \(n\) steps. In other words, it repeatedly applies the rules of the Game of Life (i.e., the make_step method) \(n\) times to evolve the game. Realizing this new method would allow us to do something exciting: obtain a snapshot of the game at a specific step.

## 7.Create a Method to Draw the Grid
Now that we have implemented the main mechanics of the Game of Life, it would be great to have a visual representation of our game board. For this task, you need to implement the draw_grid() method. The method aims to provide a visual plot of the current state of the game board using the matplotlib library. This would serve as an improved version of the print_grid() method where we simply printed the grid.

In the method, you’ll create a scatter plot where the \(x\) and \(y\) coordinates are the positions of the cells in the grid, and the color of each point is determined by whether the cell is alive or dead.

Remember that the grid’s visualized version should look the same as the printed one. In other words, the positions of the live and dead cells in the scatter plot should match their positions when printed on the console.

Enjoy creating the game board!

## 8.Document the Code
Your progress is commendable. Great job!

Documenting your code is the final required task for completing the project. Proper documentation is essential for making your code understandable to others and reminding yourself what your code does when you revisit it in the future. Python provides a built-in way of writing documentation using comments known as docstrings.

Docstrings are a type of comment used at the beginning of functions, methods, classes, and modules to describe what they do. They are written between triple quotes, allowing for multiple lines of text.

Your task is to add docstrings to each method in your GameOfLife class.

To give you a starting point, note how to document the populate_grid method:

def populate_grid(self, coord):
    '''
    Populates the game grid with live cells at the specified coordinates.
    
    Parameters:
    coord: A list of tuples. Each tuple represents the (x, y) coordinates of a live cell.

    Returns:
    The updated life_grid with the new live cells.
    '''
    # Given a list of 2D coordinates (represented as tuples/lists with 2 elements each),
    # set the corresponding elements in your grid to 1.
In this docstring, the first line briefly describes what the method does. The Parameters section lists the input parameters and their types and explains what they represent. The Returns section describes what the function returns.

Add similar docstrings to the rest of the methods in your GameOfLife class. Remember, good documentation makes your code more accessible and maintainable for others and your future self. Explain clearly what the method or class does without explaining how it works. The reader can look at the code for that information.

Happy documenting!
