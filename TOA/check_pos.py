from config import CELL_SIZE, GRID


class CheckMousePos:

    def mouse_coordinates(self, coordinates):

        print(f'Координаты клика: {coordinates}')
        self.x = int(coordinates[0] / CELL_SIZE[0])
        self.y = int(coordinates[1] / CELL_SIZE[1])
        self.cell = f'{self.x}:{self.y}'
        for cell_name in GRID.keys():
            if cell_name == self.cell:
                print(f"Активна ли ячейка: {GRID[cell_name]['is_active']}")
                print(f'Имя ячейки: {cell_name}')
                print(f"Координаты: {GRID[cell_name]['coord']}")

if __name__ == '__main__':
    CheckMousePos()
