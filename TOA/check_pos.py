from config import MAIN_SIZE_FOR_WINDOW, CELL_SIZE, GRID


class CheckMousePos:

    def mouse_coordinates(self, coordinates):
        """
        This method show information from GRID to console
        :param coordinates:
        :return: coordinates
        """
        print(f'Координаты курсора: {coordinates}')
        self.x = int(coordinates[0] / CELL_SIZE[0])
        self.y = int(coordinates[1] / CELL_SIZE[1])
        self.cell = f'{self.x}:{self.y}'
        for cell_name, cell_value in GRID.items():
            if cell_name == self.cell:
                print(f"Активна ли ячейка: {GRID[cell_name]['is_active']}")
                print(f'Имя ячейки: {cell_name}')
                print(f"Координаты ячейки: {GRID[cell_name]['coord']}")
        return coordinates

    def get_cell_coordinate(self, mouse_coordinates):
        """
        This method for return cell coordinate from GRID for mouse coordinate
        :param mouse_coordinates:
        :return: cell coordinate from GRID
        """
        x = int(mouse_coordinates[0] / CELL_SIZE[0])
        y = int(mouse_coordinates[1] / CELL_SIZE[1])
        cell = f'{x}:{y}'
        try:
            if GRID[cell]['is_active']:
                return GRID[cell]['coord']
        except:
            print(f'Cell {cell} not found ')

    def get_cell_name(self, mouse_coordinates):
        """
        This method return cell name for GRID.
        :param mouse_coordinates:
        :return: cell name in GRID
        """

        x = int(mouse_coordinates[0] / CELL_SIZE[0])
        y = int(mouse_coordinates[1] / CELL_SIZE[1])
        cell = f'{x}:{y}'
        print('Cell not found')
        return cell
