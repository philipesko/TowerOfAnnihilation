import pygame
import os.path


from main_window import CreateMainWindow
from config import PATH_TO_RESOURCE
from Tower import SpriteTower
from config import PATH_TO_RESOURCE, SURFACE, GRID
from grid import Grid
from check_pos import CheckMousePos
from creep import Creep


class Scene1(CreateMainWindow):

    def __init__(self):
        """Main method MainWindow class reinitialization for scene 1(level1)"""
        super(CreateMainWindow, self).__init__()
        self.tower_group = pygame.sprite.Group()
        # CreateMainWindow.__init__(self)
        self.game_exit = False
        # Defining a grid
        self.grid_class = Grid()
        self.grid = self.grid_class.define_grid()
        self.creep = Creep()
        # Initial health
        self.health_left = 2

        self.main_menu_greets = None
        self.main_menu_greets_position = None
        self._resource_path = os.path.join(PATH_TO_RESOURCE, 'maps')
        self.background = self.main_menu_background = pygame.image.load(os.path.join(self._resource_path, 'Map1.png'))
        # Setting active cells for towers
        self.active_cells_scene1 = ['6:3', '9:3', '12:3', '8:5', '11:5', '13:5', '9:6', '10:6', '11:6', '13:6',
                                    '11:7', '4:8', '6:8', '11:9', '2:10', '4:10', '7:10', '5:12', '8:12']
        self.grid_class.active_cells(self.active_cells_scene1)

    def create(self):
        """Main method from MainWindows reinitialization"""
        # Set background for scene 1
        self.surface.blit(self.main_menu_background, (0, 0))
        self.show_mouse_position_with_px()
    
    def show_mouse_position_with_px(self):
        """
        Drawing health status
        """
        self.main_menu_greets_fonts = pygame.font.Font(os.path.join(PATH_TO_RESOURCE, 'font_forever.ttf'), 10)
        self.positiontext(f'Health left: {self.health_left}', (10, 10))

    def move_creep(self):
        self.creep.move()
        if self.creep.damage:
            self.health_left -= 1
