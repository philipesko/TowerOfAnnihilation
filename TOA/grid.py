from config import MAIN_SIZE_FOR_WINDOW, CELL_SIZE
# from scene_one import Scene1


class Grid:

    def __init__(self):

        # self.scene1 = Scene1()
        # self.active_cells = Scene1().active_cells
        # print(self.active_cells)
        # Number of cells on X axis
        self.x_cells_quantity = int(MAIN_SIZE_FOR_WINDOW[0] / CELL_SIZE[0])
        # Number of cells on Y axis
        self.y_cells_quantity = int(MAIN_SIZE_FOR_WINDOW[1] / CELL_SIZE[1])
        # Generating grid
        self.define_grid()

    def define_cell_list(self, cell_quantity):
        """
        Generating a grid
        """
        # Defining a grid
        self.grid = {}
        # Making dictionary
        for cell_quantity in range(cell_quantity):
            for i in range(13):
                self.grid[f'{cell_quantity}:{i}'] = {}
        # Filling grid with default values
        for item in self.grid.values():
            item['is_active'] = False
            item['towerlevel'] = 0
        return self.grid

    def define_grid(self):
        '''
        Defining a grid
        '''
        self.grid = self.define_cell_list(self.x_cells_quantity)
        return self.grid

    def active_cells(self, cell_list):

        self.cell_list = cell_list
        for i in self.cell_list:
            self.grid[i]['is_active'] = True
        print(self.grid)
        return self.grid


if __name__ == '__main__':
    Grid()
