import pygame.cursors
from config import CELL_SIZE, GRID


class CheckMousePos:

    def cell_compute(self, coordinates):

        self.x = int(coordinates[0] / CELL_SIZE[0])
        self.y = int(coordinates[1] / CELL_SIZE[1])
        self.cell = f'{self.x}:{self.y}'
        return self.cell

    def mouse_coordinates(self, coordinates, name_request):
        """
        This method show information from GRID to console
        :param name_request: Fasle - return "cell name"/ True - return "cell coordinate" from GRID
        :return:
        :param coordinates:
        :return: cell name or coordinates
        """
        self.cell_compute(coordinates)
        # return cell name
        if self.cell in GRID and name_request:
            return self.cell
        # return cell coords
        if self.cell in GRID and not GRID[self.cell]['towerlevel']\
                and GRID[self.cell]['is_active'] and not name_request:
            return GRID[self.cell]['coord']

    def cursor_type(self, coordinates):

        self.cell_compute(coordinates)
        if self.cell in GRID and GRID[self.cell]['is_active']:
            pygame.mouse.set_cursor(*pygame.cursors.diamond)
        else:
            pygame.mouse.set_cursor(*pygame.cursors.tri_left)
