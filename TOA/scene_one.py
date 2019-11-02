import pygame
import os.path


from main_window import CreateMainWindow
from config import PATH_TO_RESOURCE
from Tower import SpriteTower
from config import PATH_TO_RESOURCE, SURFACE
from grid import Grid
from check_pos import CheckMousePos


class Scene1(CreateMainWindow):

    def __init__(self):
        """Main method MainWindow class reinitialization for scene 1(level1)"""
        super(CreateMainWindow, self).__init__()
        self.tower_group = pygame.sprite.Group()
        # CreateMainWindow.__init__(self)
        # Defining a grid
        self.grid_class = Grid()
        self.grid = self.grid_class.define_grid()
        # Tracking mouse events
        # self.click_event = CheckMousePos()

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
        # temporary Create sprite
        # sp = SpriteTower()
        # mouse = self.show_mouse_position_with_px()
        # sp.set_param_tower()  # set parameters for tower in abstract class.
        # if 550 > mouse[0] > 500 and 550 > mouse[1] > 500:
        #     sp.selected = True
        #
        #
        # # sp.draw(mouse)
        #
        # sp_two = SpriteTower(x=600, y=600)
        # if 650 > mouse[0] > 600 and 650 > mouse[1] > 600:
        #     sp_two.selected = True

        # sp_two.turn_tower(mouse)
        # sp_two.draw()

        # for self.click in pygame.event.get():
        #     if self.click.type == pygame.MOUSEBUTTONDOWN and self.click.button == 1:
        #         try:
        #             check = CheckMousePos()
        #             coord = check.get_cell_coordinate(mouse)
        #             spite_tower = SpriteTower(x=coord[0], y=coord[1])
        #             self.tower_group.add(spite_tower)
        #             print('True')
        #         except:
        #             print('Not True')
        #
        # self.tower_group.update(SURFACE, mouse)
        # self.tower_group.draw(SURFACE)







