import pygame
import os.path


class CreateMainWindows:

    def __init__(self, width=1024, height=768):
        self._current_path = os.path.dirname(__file__)  # Where your .py file is located
        self._resource_path = os.path.join(self._current_path, 'resources')
        self._project_name = 'Tower of Annihilation'
        self._path_dir_resources = 'resources'

        # Size of a window in px
        self.size = width, height
        self.surface = pygame.display.set_mode(self.size)

    def create(self):

        # Loading and formatting windows icon to 32x32
        icon = pygame.image.load(os.path.join(self._resource_path, 'tower-defense-levels-ship.png'))
        icon = pygame.transform.scale(icon, (32, 32))

        # Loading background for main menu, was scaled previously, but may be scaled in case of size changing
        main_menu_background = pygame.image.load(os.path.join(self._resource_path, 'main.png'))

        # Load font and position the text
        main_menu_greets = pygame.font.Font(os.path.join(self._resource_path, 'font_forever.ttf'), 28)
        main_menu_greets = main_menu_greets.render(f'Welcome to the {self._project_name}', 1, (207, 204, 127))
        text_pos = main_menu_greets.get_rect()
        text_pos.center = main_menu_background.get_rect().center

        # Setting a window caption and an icon
        set_capture = pygame.display.set_caption(self._project_name)
        set_capture = pygame.display.set_icon(icon)
        self.surface.blit(main_menu_background, (0, 0))
        self.surface.blit(main_menu_greets, text_pos)
