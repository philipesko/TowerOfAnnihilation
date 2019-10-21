from config import MAIN_SIZE_FOR_WINDOW


class Grid:

    def __init__(self):

        # Defining grid
        self.grid = {}

        # Defining cell size
        self.cell = (58, 58)

        # Number of cells on X axis
        self.x_cells_quantity = int(MAIN_SIZE_FOR_WINDOW[0] / self.cell[0])

        # Number of cells on Y axis
        self.y_cells_quantity = int(MAIN_SIZE_FOR_WINDOW[1] / self.cell[1])

        # Generating grid
        self.grid = self.define_cell_list(self.x_cells_quantity)
        # self.grid = self.compute_coordinates()
        print(self.grid)

    def define_cell_list(self, cell_quantity):
        """
        Making list for a row or a string
        """
        # Making dictionary
        for cell_quantity in range(cell_quantity):
            for i in range(13):
                self.grid[f'{cell_quantity}:{i}'] = {}
        # Filling grid with default values
        for item in self.grid.values():
            item['is_active'] = False
            item['towerlevel'] = 0
        return self.grid


if __name__ == '__main__':
    Grid()
