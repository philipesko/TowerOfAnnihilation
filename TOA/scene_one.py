import pygame
import os.path


from main_window import CreateMainWindow
from config import PATH_TO_RESOURCE
from sprites import SpriteTower
from grid import Grid
from check_pos import CheckMousePos


class Scene1(CreateMainWindow):

    def __init__(self):
        """Main method MainWindow class reinitialization for scene 1(level1)"""
        super(CreateMainWindow, self).__init__()

        # CreateMainWindow.__init__(self)
        # Defining a grid
        self.grid_class = Grid()
        self.grid = self.grid_class.define_grid()
        # Tracking mouse events
        self.click_event = CheckMousePos()

        self.main_menu_greets = None
        self.main_menu_greets_position = None
        self._resource_path = os.path.join(PATH_TO_RESOURCE, 'maps')
        self.background = self.main_menu_background = pygame.image.load(os.path.join(self._resource_path, 'Map_grid.png'))
        # Setting active cells
        self.active_cells_scene1 = ['6:3', '9:3', '12:3', '8:5', '11:5', '13:5', '9:6', '10:6', '11:6', '13:6',
                                    '11:7', '4:8', '6:8', '11:9', '2:10', '4:10', '7:10', '5:12', '8:12']
        self.grid_class.active_cells(self.active_cells_scene1)
        print(self.grid)

    def create(self):
        """Main method from MainWindows reinitialization"""
        CreateMainWindow.show_mouse_position_with_px(self)
        # Set background for scene 1
        self.surface.blit(self.main_menu_background, (0, 0))
        # temporary Create sprite
        sp = SpriteTower()
        sp = sp.create_tower_1(surface=self.surface)
        self.surface.blit(sp, (468, 295))
