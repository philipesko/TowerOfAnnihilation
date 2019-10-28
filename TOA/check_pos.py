from config import CELL_SIZE, GRID
# import pygame


class CheckMousePos:

    def mouse_coordinates(self, coordinates):

        print(f'Координаты курсора: {coordinates}')
        self.x = int(coordinates[0] / CELL_SIZE[0])
        self.y = int(coordinates[1] / CELL_SIZE[1])
        self.cell = f'{self.x}:{self.y}'
        for cell_name, cell_value in GRID.items():
            if cell_name == self.cell:
                print(f"Активна ли ячейка: {GRID[cell_name]['is_active']}")
                print(f'Имя ячейки: {cell_name}')
                print(f"Координаты ячейки: {GRID[cell_name]['coord']}")
            # if cell_value['is_active'] is True:
            #     pygame.mouse.set_cursor(*pygame.cursors.diamond)
            # else:
            #     # set standard cursor
            #     pygame.mouse.set_cursor(*pygame.cursors.tri_left)


if __name__ == '__main__':
    CheckMousePos()
