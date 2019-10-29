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
        # self.mouse_position_one = pygame.mouse.get_pos()

    def create(self):
        """Main method from MainWindows reinitialization"""
        # Set background for scene 1
        self.surface.blit(self.main_menu_background, (0, 0))
        # temporary Create sprite
        sp = SpriteTower()
        mouse = self.show_mouse_position_with_px()
        sp.set_param_tower()  # set parameters for tower in abstract class.
        if 550 > mouse[0] > 500 and 550 > mouse[1] > 500:
            sp.selected = True

        pos2 = pygame.math.Vector2(1,0)
        pos1 = pygame.math.Vector2(525 - mouse[0],  525 - mouse[1])
        pos1 = pos1.angle_to(pos2)
        # print(pos1)
        sp.turn_tower(pos1+90)
        sp.draw_radius()
        sp.draw_tower()



        # self.surface.blit(sp, (500, 500))
