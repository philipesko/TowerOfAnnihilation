from grid import Grid
from config import CELL_SIZE


class CheckMousePos:

    def __init__(self):

        self.grid = Grid()
        self.grid = self.grid.define_grid()

    def mouse_coordinates(self, coordinates):

        print(coordinates)
        self.x = int(coordinates[0] / CELL_SIZE[0])
        self.y = int(coordinates[1] / CELL_SIZE[1])
        self.cell = f'{self.x}:{self.y}'
        for i in self.grid.keys():
            if i == self.cell:
                print(self.grid[i]['is_active'])
                print(i)


if __name__ == '__main__':
    CheckMousePos()
