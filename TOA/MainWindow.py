import pygame
import os.path

#ImgOnOff = []

class CreateMainWindow:

    def __init__(self, width=1024, height=768):
        
        self._current_path = os.path.dirname(__file__)  # Where your .py file is located
        self._resource_path = os.path.join(self._current_path, 'resources')
        self._project_name = 'Tower of Annihilation'
        self._button_name = ['start.png', 'exit.png', 'start_pressed.png', 'exit_pressed.png', 'start_light.png', 'exit_light.png']
        self._isrunning = True
        # self._buttons_start_pos = 0.35

        # Size of a window in px
        self.size = width, height
        self.surface = pygame.display.set_mode(self.size)

        # Load Fonts, background image and position main text
        self.main_menu_greets_fonts = pygame.font.Font(os.path.join(self._resource_path, 'font_forever.ttf'), 28)
        self.main_menu_greets = self.main_menu_greets_fonts.render(f'Welcome to the {self._project_name}', 1, (207, 204, 127))
        self.main_menu_greets_position = self.surface.blit(self.main_menu_greets, (30, 260))
        self.main_menu_background = pygame.image.load(os.path.join(self._resource_path, 'main.png'))

        #create icon
        self.icon = pygame.image.load(os.path.join(self._resource_path, 'tower-defense-levels-ship.png'))
        self.icon = pygame.transform.scale(self.icon, (32, 32))

        pygame.display.set_caption(self._project_name)
        pygame.display.set_icon(self.icon)



    def positiontext(self, text, position):
        '''
        Positioning Greetings text and drawing it
        '''
        # draw text with team fonts on active window
        text_position = self.main_menu_greets_fonts.render(text, 2, (207, 204, 127))
        self.surface.blit(text_position, position)


    def create(self):
        '''
        Creating Main window, with backround, caption, icon, buttons, etc
        '''
        # Loading and formatting windows icon to 32x32
        # icon = pygame.image.load(os.path.join(self._resource_path, 'tower-defense-levels-ship.png'))
        # icon = pygame.transform.scale(icon, (32, 32))

        # Setting a window caption and an icon
        # pygame.display.set_caption(self._project_name)
        # pygame.display.set_icon(icon)

        # Positioning background and pointer indicator for main menu
        self.surface.blit(self.main_menu_background, (0, 0))
        self.surface.blit(self.main_menu_greets, self.main_menu_greets_position)
        self.show_mouse_position_with_px()
        self.main_menu_buttons()


    def show_mouse_position_with_px(self):
        '''
        Drawing mouse position/click tracker
        '''
        self.main_menu_greets_fonts = pygame.font.Font(os.path.join(self._resource_path, 'font_forever.ttf'), 10)
        self.positiontext(f'Mouse position {pygame.mouse.get_pos()}', (770, 20))
        self.mouse = pygame.mouse.get_pos()
        

    def main_menu_buttons(self):
        '''
        Launching button drawing func and tracking mouse over action
        '''
        self.draw_button(self._button_name[0], 0.45)
        start_coord = self.menu_button
        self.draw_button(self._button_name[1], 0.55)
        exit_coord = self.menu_button


        if 427+170 > self.mouse[0] > 427 and 345+56 > self.mouse[1] > 345:
            pygame.mouse.set_cursor(*pygame.cursors.diamond)
            self.draw_button(self._button_name[4], 0.45)
            self.draw_button(self._button_name[1], 0.55)
        elif 427+170 > self.mouse[0] > 427 and 422+56 > self.mouse[1] > 422:
            self.draw_button(self._button_name[0], 0.45)
            pygame.mouse.set_cursor(*pygame.cursors.diamond)
            self.draw_button(self._button_name[5], 0.55)
            for self.click in pygame.event.get():
                if self.click.type == pygame.MOUSEBUTTONDOWN and self.click.button == 1:
                    self._isrunning = False
        else:
            # set standard cursor
            pygame.mouse.set_cursor(*pygame.cursors.tri_left)
                
    def draw_button(self, button_name, y):
        '''
        Calculating buttons position and drawing them
        '''
        x = 0.5 * self.size[0]
        y = y * self.size[1]
        self.menu_button = pygame.image.load(os.path.join(self._resource_path, 'buttons', button_name))
        self.menu_button_size = self.menu_button.get_rect()
        self.menu_button_offsetx = self.menu_button_size[2]/2
        self.menu_button = self.surface.blit(self.menu_button, 
        ((x - self.menu_button_offsetx), y))
        return self.menu_button

    # def load_image(self, image):
        