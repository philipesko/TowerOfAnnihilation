import pygame, os.path

from main_window import BUTTON_NAME_FOR_MAIN_MENU,MAIN_MENU_BUTTON, CreateMainWindow


class CheckMousePos:

    def __init__(self):

        self.cmw = CreateMainWindow()
        self.button = self.cmw.main_menu_buttons()
        self.start_button = self.button[0]
        self.exit_button = self.button[1]


    def mouse_coordinates(self, coordinates):

        self.mouse = coordinates

        # print(f' start: {self.start_button}, exit: {self.exit_button}')

        if self.start_button[0] + self.start_button[2] > self.mouse[0] > self.start_button[0] and \
                self.start_button[1] + self.start_button[3] > self.mouse[1] > self.start_button[1]:

            pygame.mouse.set_cursor(*pygame.cursors.diamond)
            self.cmw.draw_button(BUTTON_NAME_FOR_MAIN_MENU[4], MAIN_MENU_BUTTON['button_start']['y'])
            self.cmw.draw_button(BUTTON_NAME_FOR_MAIN_MENU[1], MAIN_MENU_BUTTON['button_exit']['y'])

        elif self.exit_button[0] + self.exit_button[2] > self.mouse[0] > self.exit_button[0] and\
                self.exit_button[1] + self.exit_button[3] > self.mouse[1] > self.exit_button[1]:
            self.cmw.draw_button(BUTTON_NAME_FOR_MAIN_MENU[0], MAIN_MENU_BUTTON['button_start']['y'])
            pygame.mouse.set_cursor(*pygame.cursors.diamond)
            self.cmw.draw_button(BUTTON_NAME_FOR_MAIN_MENU[5], MAIN_MENU_BUTTON['button_exit']['y'])

            # for self.click in pygame.event.get():
            #     if self.click.type == pygame.MOUSEBUTTONDOWN and self.click.button == 1:
            #         self.isrunning = False

        else:
            # set standard cursor
            pygame.mouse.set_cursor(*pygame.cursors.tri_left)

























        # if 427+170 > self.mouse[0] > 427 and 345+56 > self.mouse[1] > 345:
        #     self.draw_button(self._button_name[4], 0.45)
        #     self.draw_button(self._button_name[1], 0.55)
        # elif 427+170 > self.mouse[0] > 427 and 422+56 > self.mouse[1] > 422:
        #     self.draw_button(self._button_name[0], 0.45)
        #     self.draw_button(self._button_name[5], 0.55)
        #     for self.click in pygame.event.get():
        #         if self.click.type == pygame.MOUSEBUTTONDOWN and self.click.button == 1:
        #             self._isrunning = False