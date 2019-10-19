import pygame, os.path

# from main_window import button_exit_position, button_start_position, BUTTON_NAME_FOR_MAIN_MENU, MAIN_MENU_BUTTON, CreateMainWindow


class CheckMousePos:

    # def __init__(self, coordinates):

    #     self.mouse_coordinates(coordinates)

    def mouse_coordinates(self, coordinates):

        self.mouse_coordinates = coordinates
        print(coordinates)


    # def __init__(self):

    #     self.cmw = CreateMainWindow()
    #     self.button = self.cmw.main_menu_buttons()
    #     self.start_button = self.button[0]
    #     self.exit_button = self.button[1]


    # def mouse_coordinates(self, coordinates):

    #     self.mouse = coordinates

    #     # print(f' start: {self.start_button}, exit: {self.exit_button}')

    #     if self.start_button[0] + self.start_button[2] > self.mouse[0] > self.start_button[0] and \
    #             self.start_button[1] + self.start_button[3] > self.mouse[1] > self.start_button[1]:

    #         pygame.mouse.set_cursor(*pygame.cursors.diamond)
    #         self.cmw.draw_button(BUTTON_NAME_FOR_MAIN_MENU[4], MAIN_MENU_BUTTON['button_start']['y'])
    #         self.cmw.draw_button(BUTTON_NAME_FOR_MAIN_MENU[1], MAIN_MENU_BUTTON['button_exit']['y'])

    #     elif self.exit_button[0] + self.exit_button[2] > self.mouse[0] > self.exit_button[0] and\
    #             self.exit_button[1] + self.exit_button[3] > self.mouse[1] > self.exit_button[1]:
    #         self.cmw.draw_button(BUTTON_NAME_FOR_MAIN_MENU[0], MAIN_MENU_BUTTON['button_start']['y'])
    #         pygame.mouse.set_cursor(*pygame.cursors.diamond)
    #         self.cmw.draw_button(BUTTON_NAME_FOR_MAIN_MENU[5], MAIN_MENU_BUTTON['button_exit']['y'])

    #         # for self.click in pygame.event.get():
    #         #     if self.click.type == pygame.MOUSEBUTTONDOWN and self.click.button == 1:
    #         #         self.isrunning = False

    #     else:
    #         # set standard cursor
    #         pygame.mouse.set_cursor(*pygame.cursors.tri_left)
