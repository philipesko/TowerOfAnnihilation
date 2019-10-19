from config import MAIN_SIZE_FOR_WINDOW


class Grid:

    def __init__(self):

        # Defining grid
        self.grid = []

        # Defining cell size
        self.cell = (58, 58)

        # Number of cells on X axis
        self.x_cells_quantity = int(MAIN_SIZE_FOR_WINDOW[0] / self.cell[0])

        # Number of cells on Y axis
        self.y_cells_quantity = int(MAIN_SIZE_FOR_WINDOW[1] / self.cell[1])

        # Generating grid with keys only
        self.grid = self.define_cell_list(self.x_cells_quantity)
        print(self.grid['0:5'])

    def define_cell_list(self, cell_quantity):
        """
        Making list for a row or a string
        """
        # Defining empty row/string list
        list_obj = {}
        # Making dictionary
        for cell_quantity in range(cell_quantity):
            for i in range(13):
                list_obj[f'{cell_quantity}:{i}'] = {'coord': ([0, 0], [58, 0], [0, 58], [58, 58])}
        # Starting coordinates
        # list_obj['0:1']['coord'] = ([0, 0], [58, 0], [0, 58], [58, 58])
        # Filling grid with default values
        for item in list_obj.values():
            coord = item['coord']
            item['is_active'] = False
            item['towerlevel'] = 0
            for i in coord:
                i[0] += 59
                i[1] += 59
        return list_obj


if __name__ == '__main__':
    Grid()
