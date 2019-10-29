import pygame, os.path

from main_window import button_exit_position, button_start_position, BUTTON_NAME_FOR_MAIN_MENU,MAIN_MENU_BUTTON, CreateMainWindow


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


# if 427+170 > self.mouse[0] > 427 and 345+56 > self.mouse[1] > 345:
#     self.draw_button(self._button_name[4], 0.45)
#     self.draw_button(self._button_name[1], 0.55)
# elif 427+170 > self.mouse[0] > 427 and 422+56 > self.mouse[1] > 422:
#     self.draw_button(self._button_name[0], 0.45)
#     self.draw_button(self._button_name[5], 0.55)
#     for self.click in pygame.event.get():
#         if self.click.type == pygame.MOUSEBUTTONDOWN and self.click.button == 1:
#             self._isrunning = False