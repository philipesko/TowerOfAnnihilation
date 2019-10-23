import pygame
import os.path

from config import PATH_TO_RESOURCE, SURFACE


class SpriteTower(pygame.sprite.Sprite):
    """Class for Towers"""

    def __init__(self):
        super(pygame.sprite.Sprite, self).__init__()
        self._path_to_sprite = os.path.join(PATH_TO_RESOURCE, 'tower-defense-turrets')
        self._image_tower1 = ['turret-1-1.png', 'turret-1-2.png', 'turret-1-3.png']
        self.angle = 0
        self.sprite_tower_1 = None
        self.x = None
        self.y = None
        self.surface = SURFACE

    def create_tower_1(self, flag_level_tower=2, scale_x=50, scale_y=50, x=500, y=500, angle=90):
        """"Create tower 1 (draw, load image, check level up for tower, x and y start coordinates)
        :param scaleY:
        :param scaleX:
        :param surface:
        :param flag_level_tower: load image with compare with level tower.
        :param x: Position X on window
        :param y: Position Y on window
        :param angle: to stream tower

        """
        self.x = x + 4
        self.y = y + 4
        # variable "flag_level_tower" the amount depends on the number of tower levels drawn in a
        # folder with "resources". Default = 0 => 1 Level
        self.sprite_tower_1 = pygame.image.load(os.path.join(self._path_to_sprite,
                                                             self._image_tower1[flag_level_tower]))
        # tmp scale
        self.sprite_tower_1 = pygame.transform.scale(self.sprite_tower_1, (scale_x, scale_y))
        self.surface.blit(self.sprite_tower_1, (self.x, self.y))
        # To do

    def turn_tower(self, angle):
        """
        Method for turn the tower on angle
        :param surface:
        :param angle:
        """
        self.angle = angle
        self.sprite_tower_1 = pygame.transform.rotate(self.sprite_tower_1, self.angle)
        


