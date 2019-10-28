from config import MAIN_SIZE_FOR_WINDOW, CELL_SIZE, GRID
# from scene_one import Scene1


class Grid:

    def __init__(self):

        self.x = CELL_SIZE[0]
        self.y = CELL_SIZE[1]
        # Number of cells on X axis
        self.x_cells_quantity = int(MAIN_SIZE_FOR_WINDOW[0] / self.x)
        # Number of cells on Y axis
        self.y_cells_quantity = int(MAIN_SIZE_FOR_WINDOW[1] / self.y)
        # Generating grid
        self.define_grid()
        print(GRID)

    def define_cell_list(self, cell_quantity):
        """
        Generating a grid
        """
        # Making dictionary
        for cell_quantity in range(cell_quantity):
            for i in range(13):
                GRID[f'{cell_quantity}:{i}'] = {'coord': [0, 0]}
        # Filling grid with default values
        for item in GRID.values():
            item['is_active'] = False
            item['towerlevel'] = 0
        self.fill_coords(self.x, self.y, 0)
        return GRID

    def define_grid(self):
        '''
        Defining a grid
        '''
        GRID = self.define_cell_list(self.x_cells_quantity)
        return GRID

    def fill_coords(self, x, y, start_pos):
        '''
        Filling grid with coordinates
        '''
        carriage = start_pos
        for cell_name, item in GRID.items():
            if cell_name == '0:0':
                continue
            if carriage == 986:
                carriage = 0
                y += 58
                item['coord'][1] += y
            carriage += x
            item['coord'][0] += carriage
            item['coord'][1] = y
            # print(f'z: {carriage}')
            # print(f'y: {y}')


    def active_cells(self, cell_list):

        self.cell_list = cell_list
        for i in self.cell_list:
            GRID[i]['is_active'] = True
        return GRID


if __name__ == '__main__':
    Grid()
