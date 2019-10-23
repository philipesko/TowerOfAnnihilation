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
        # Set background for scene 1
        self.surface.blit(self.main_menu_background, (0, 0))
        # temporary Create sprite
        sp = SpriteTower()
        sp.create_tower_1()
        sp.turn_tower(90)

        # self.surface.blit(sp, (500, 500))




