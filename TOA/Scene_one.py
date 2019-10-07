import pygame
import os.path


from MainWindow import CreateMainWindow


class Scene1(CreateMainWindow):

    def __init__(self):
        """Main method MainWindow class reinitialization for scene 1(level1)"""
        CreateMainWindow.__init__(self)
        self.main_menu_greets = None
        self.main_menu_greets_position = None
        self._resource_path = os.path.join(self._current_path, 'resources/maps')
        self.background = self.main_menu_background = pygame.image.load(os.path.join(self._resource_path, 'Map1.png'))

    def create(self):
        """Main method from MainWindows reinitialization"""
        # super(Scene1, self).create()

        # Set background for scene 1
        self.surface.blit(self.main_menu_background, (0, 0))



