import pygame
import os.path

#ImgOnOff = []

class CreateMainWindow:

    def __init__(self, width=1024, height=768):
        self._current_path = os.path.dirname(__file__)  # Where your .py file is located
        self._resource_path = os.path.join(self._current_path, 'resources')
        self._project_name = 'Tower of Annihilation'
        self._button_name = ['start.png', 'exit.png']
        self._buttons_start_pos = 0.45

        # Size of a window in px
        self.size = width, height
        self.surface = pygame.display.set_mode(self.size)

        # Load Fonts, background image and position main text
        self.main_menu_greets_fonts = pygame.font.Font(os.path.join(self._resource_path, 'font_forever.ttf'), 28)
        self.main_menu_greets = self.main_menu_greets_fonts.render(f'Welcome to the {self._project_name}', 1, (207, 204, 127))
        self.main_menu_greets_position = self.surface.blit(self.main_menu_greets, (30, 260))
        self.main_menu_background = pygame.image.load(os.path.join(self._resource_path, 'main.png'))


    def positiontext(self, text, position):
        # draw text with team fonts on active window
        text_position = self.main_menu_greets_fonts.render(text, 2, (207, 204, 127))
        self.surface.blit(text_position, position)


    def create(self):

        # Loading and formatting windows icon to 32x32
        icon = pygame.image.load(os.path.join(self._resource_path, 'tower-defense-levels-ship.png'))
        icon = pygame.transform.scale(icon, (32, 32))

        # Setting a window caption and an icon
        pygame.display.set_caption(self._project_name)
        pygame.display.set_icon(icon)

        # Positioning background and pointer indicator for main menu
        self.surface.blit(self.main_menu_background, (0, 0))
        self.surface.blit(self.main_menu_greets, self.main_menu_greets_position)
        self.show_mouse_position_with_px()
        self.main_menu_buttons()


    def show_mouse_position_with_px(self):
        self.main_menu_greets_fonts = pygame.font.Font(os.path.join(self._resource_path, 'font_forever.ttf'), 10)
        self.positiontext(f'Mouse position {pygame.mouse.get_pos()}', (770, 20))


    # def center_by_x(self, x, y, obj_start):
        self.x = 0.5 * self.size[0]
        self.y = 0.5 * self.size[1]
    #     self.obj_start = self.get_rect()
    #     self.obj_start = self.obj_start[2]/2
    #     self.obj_start = self.x - self.obj_start


    def main_menu_buttons(self):
        # Start button
        start_butt = self.draw_button(self._button_name[0])
        # self.start_button = self.surface.blit(self.start_button, 
        # ((0.5 * self.size[0] - self.start_button_position), (0.45 * self.size[1])))


        # Exit button
        exit_butt = self.draw_button(self._button_name[1])
        # self.start_button = self.surface.blit(self.start_button, 
        # ((0.5 * self.size[0] - self.start_button_position), (0.55 * self.size[1])))
    

    def draw_button(self, button_name):
        x = 0.5 * self.size[0]
        y = 0.45 * self.size[1]
        self.start_button = pygame.image.load(os.path.join(self._resource_path, 'buttons', button_name))
        self.start_button_position = self.start_button.get_rect()
        self.start_button_position = self.start_button_position[2]/2
        self.start_button = self.surface.blit(self.start_button, 
        ((x - self.start_button_position), y)
        return y