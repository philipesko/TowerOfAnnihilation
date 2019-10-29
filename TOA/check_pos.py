from config import MAIN_SIZE_FOR_WINDOW, CELL_SIZE, GRID


class CheckMousePos:

    def mouse_coordinates(self, coordinates):
        """

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


