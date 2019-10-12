import pygame
import os.path


from main_window import CreateMainWindow
from config import PATH_TO_RESOURCE
from sprites import SpriteTower


class Scene1(CreateMainWindow):

    def __init__(self):
        """Main method MainWindow class reinitialization for scene 1(level1)"""
        super(CreateMainWindow, self).__init__()

        # CreateMainWindow.__init__(self)
        self.main_menu_greets = None
        self.main_menu_greets_position = None
        self._resource_path = os.path.join(PATH_TO_RESOURCE, 'maps')
        self.background = self.main_menu_background = pygame.image.load(os.path.join(self._resource_path, 'Map1.png'))

    def create(self):
        """Main method from MainWindows reinitialization"""
        # super(Scene1, self).create()
        print(self.surface)
        # Set background for scene 1
        # surface = self.surface
        self.surface.blit(self.main_menu_background, (0, 0))
        sp = SpriteTower()
        sp.create_tower_1(surface=self.surface)
        CreateMainWindow.show_mouse_position_with_px(self)




