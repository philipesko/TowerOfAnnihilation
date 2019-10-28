from config import CELL_SIZE, GRID


class CheckMousePos:

    def mouse_coordinates(self, coordinates):

        print(coordinates)
        self.x = int(coordinates[0] / CELL_SIZE[0])
        self.y = int(coordinates[1] / CELL_SIZE[1])
        self.cell = f'{self.x}:{self.y}'
        for i in GRID.keys():
            if i == self.cell:
                print(GRID[i]['is_active'])
                print(i)


if __name__ == '__main__':
    CheckMousePos()
