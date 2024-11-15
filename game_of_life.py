import matplotlib.pyplot as plt

class GameOfLife(object):

    # A class to simulate Conway's Game of Life.
    # Attributes:
    # grid: The 2D grid representing the game state.

    def __init__(self, x_dim, y_dim):
        # Initialize a 2D list with dimensions x_dim by y_dim filled with zeros.
        # Initializes the game grid with the given dimensions.
        # Parameters:
        # x_dim: Number of rows in the grid.
        # y_dim: Number of columns in the grid.
        self.grid = [[0 for _ in range(y_dim)] for _ in range(x_dim)]

    def get_grid(self):
        # Implement a getter method for your grid.
        return self.grid

    def print_grid(self):
        # Implement a method to print out your grid in a human-readable format.
        # Prints the grid in a console-friendly format.
        for row in self.grid:
            print(" ".join(str(cell) for cell in row))

    def populate_grid(self, coord):
        # Given a list of 2D coordinates (represented as tuples/lists with 2 elements each),
        # set the corresponding elements in your grid to 1.
        for (x, y) in coord:
            # Belirtilen koordinattaki hücreyi canlı yap
            self.grid[x][y] = 1

    def make_step(self):
        # Implement the logic to update the game state according to the rules of Conway's Game of Life.
        '''
        Advances the game by one step according to the Game of Life rules.

        Updates the grid by calculating the next state of each cell based on its neighbors.
        '''
        rows, cols = len(self.grid), len(self.grid[0])
        new_grid = [[0 for _ in range(cols)] for _ in range(rows)]

        for x in range(rows):
            for y in range(cols):
                # Komşuları değerlendir
                neighbors = [
                    (i, j)
                    for i in range(x - 1, x + 2)
                    for j in range(y - 1, y + 2)
                    if (i, j) != (x, y) and 0 <= i < rows and 0 <= j < cols
                ]
                live_neighbors = sum(self.grid[i][j] for i, j in neighbors)

                # Game of Life kurallarını uygula
                if self.grid[x][y] == 1:  # Hücre canlıysa
                    new_grid[x][y] = 1 if live_neighbors in (2, 3) else 0
                else:  # Hücre ölüyse
                    new_grid[x][y] = 1 if live_neighbors == 3 else 0

        self.grid = new_grid

    def make_n_steps(self, n):
        # Implement a method that applies the make_step method n times.
        '''
            Advances the game by n steps.

            Parameters:
            n: The number of steps to advance.
            '''
        for _ in range(n):
            self.make_step()

    def draw_grid(self):
        # Draw the current state of the grid.
        '''
            Draws the grid using a scatter plot for visual representation.
            '''
        rows, cols = len(self.grid), len(self.grid[0])
        x_coords, y_coords = [], []

        for x in range(rows):
            for y in range(cols):
                if self.grid[x][y] == 1:
                    x_coords.append(y)
                    y_coords.append(x)

        plt.figure(figsize=(6, 6))
        plt.scatter(x_coords, y_coords, c='black', s=100, marker='s')
        plt.gca().invert_yaxis()  # Görselleştirme, terminaldeki ile aynı hizayı korur
        plt.xticks(range(cols))
        plt.yticks(range(rows))
        plt.grid(True)
        plt.show()

# Initialize the game
game = GameOfLife(30, 30)

# Populate the grid with the given initial points
initial_points = [(14, 15), (15, 15), (16, 15), (15, 14), (16, 16), (14, 16), (15, 17)]
game.populate_grid(initial_points)

# Function to find the steady state
def find_steady_state(game):
    previous_grid = None
    step_count = 0

    while True:
        current_grid = [row[:] for row in game.get_grid()]  # Deep copy of the current grid
        game.make_step()
        step_count += 1

        # Check if the grid has reached a steady state
        if current_grid == game.get_grid():
            print(f"Steady state reached after {step_count} steps.")
            break
        else:
            previous_grid = current_grid

# Run the simulation
find_steady_state(game)

# Visualize the final state
game.draw_grid()

# Optionally, print the final state
game.print_grid()





