import pygame
import os.path

from config import MAIN_MENU_BUTTON, NAME_PROJECT, BUTTON_NAME_FOR_MAIN_MENU, PATH_TO_RESOURCE, MAIN_SIZE_FOR_WINDOW

button_start_position = None
button_exit_position = None


class CreateMainWindow:
    surface = pygame.display.set_mode(MAIN_SIZE_FOR_WINDOW)

    def __init__(self):

        self._project_name = NAME_PROJECT
        self.isrunning = True
        self.switch_scene = False

        # Load Fonts, background image and position main text
        self.main_menu_greets_fonts = pygame.font.Font(os.path.join(PATH_TO_RESOURCE, 'font_forever.ttf'), 28)
        self.main_menu_greets = self.main_menu_greets_fonts.render(f'Welcome to the {self._project_name}', 1,
                                                                   (207, 204, 127))
        self.main_menu_greets_position = self.surface.blit(self.main_menu_greets, (30, 260))
        self.main_menu_background = pygame.image.load(os.path.join(PATH_TO_RESOURCE, 'main.png'))

        # create icon
        self.icon = pygame.image.load(os.path.join(PATH_TO_RESOURCE, 'tower-defense-levels-ship.png'))
        self.icon = pygame.transform.scale(self.icon, (32, 32))

        pygame.display.set_caption(self._project_name)
        pygame.display.set_icon(self.icon)

    def positiontext(self, text, position):
        """
        Positioning Greetings text and drawing it
        :param text:
        :param position:
        """
        # draw text with team fonts on active window
        text_position = self.main_menu_greets_fonts.render(text, 2, (207, 204, 127))
        self.surface.blit(text_position, position)

    def create(self):
        """
        Creating Main window, with background, caption, icon, buttons, etc
        """
        # Positioning background and pointer indicator for main menu
        self.surface.blit(self.main_menu_background, (0, 0))
        self.surface.blit(self.main_menu_greets, self.main_menu_greets_position)
        self.show_mouse_position_with_px()
        self.main_menu_buttons()

    def show_mouse_position_with_px(self):
        """
        Drawing mouse position/click tracker
        """
        self.main_menu_greets_fonts = pygame.font.Font(os.path.join(PATH_TO_RESOURCE, 'font_forever.ttf'), 10)
        self.positiontext(f'Mouse position {pygame.mouse.get_pos()}', (770, 20))
        self.mouse = pygame.mouse.get_pos()
        return self.mouse

    def main_menu_buttons(self):
        """Launching button drawing func and tracking mouseover action"""
        button_start_position = self.draw_button(MAIN_MENU_BUTTON['button_start']['image'],
                                                 MAIN_MENU_BUTTON['button_start']['y'])
        button_exit_position = self.draw_button(MAIN_MENU_BUTTON['button_exit']['image'],
                                                MAIN_MENU_BUTTON['button_exit']['y'])

        if button_start_position[0] + button_start_position[2] > self.mouse[0] > button_start_position[0] and \
                button_start_position[1] + button_start_position[3] > self.mouse[1] > button_start_position[1]:

            pygame.mouse.set_cursor(*pygame.cursors.diamond)
            self.draw_button(BUTTON_NAME_FOR_MAIN_MENU[4], MAIN_MENU_BUTTON['button_start']['y'])
            self.draw_button(BUTTON_NAME_FOR_MAIN_MENU[1], MAIN_MENU_BUTTON['button_exit']['y'])

            for self.click in pygame.event.get():
                if self.click.type == pygame.MOUSEBUTTONDOWN and self.click.button == 1:
                    self.surface.fill((30, 30, 30))
                    pygame.mouse.set_cursor(*pygame.cursors.tri_left)
                    self.switch_scene = True

        elif button_exit_position[0] + button_exit_position[2] > self.mouse[0] > button_exit_position[0] and\
                button_exit_position[1] + button_exit_position[3] > self.mouse[1] > button_exit_position[1]:
            self.draw_button(BUTTON_NAME_FOR_MAIN_MENU[0], MAIN_MENU_BUTTON['button_start']['y'])
            pygame.mouse.set_cursor(*pygame.cursors.diamond)
            self.draw_button(BUTTON_NAME_FOR_MAIN_MENU[5], MAIN_MENU_BUTTON['button_exit']['y'])

            for self.click in pygame.event.get():
                if self.click.type == pygame.MOUSEBUTTONDOWN and self.click.button == 1:
                    self.isrunning = False

        else:
            # set standard cursor
            pygame.mouse.set_cursor(*pygame.cursors.tri_left)

    def draw_button(self, button_name, y):
        '''
        Calculating buttons position and drawing them
        :param button_name:
        :param y:
        :return:
        '''
        x = 0.5 * MAIN_SIZE_FOR_WINDOW[0]
        y = y * MAIN_SIZE_FOR_WINDOW[1]
        self.menu_button = pygame.image.load(os.path.join(PATH_TO_RESOURCE, 'buttons', button_name))
        self.menu_button_size = self.menu_button.get_rect()
        self.menu_button_offsetx = self.menu_button_size[2] / 2
        self.menu_button = self.surface.blit(self.menu_button,
                                             ((x - self.menu_button_offsetx), y))
        return self.menu_button
