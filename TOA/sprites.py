import pygame
import os.path

from config import PATH_TO_RESOURCE
from scene_one import Scene1


class SpriteTower(Scene1):
    """Class for Towers"""
    def __init__(self):
        Scene1.__init__(self)
        self._path_to_sprite = os.path.join(PATH_TO_RESOURCE, 'tower-defense-turrets')
        self._image_tower1 = ['turret-1-1.png', 'turret-1-2.png', 'turret-1-3.png']
        self.sprite_tower_1 = pygame.image.load(os.path.join(self._path_to_sprite, 'turret-1-1.png'))


    def create_tower_1(self, flag_level_tower=0, x=500, y=500):
        """"Create tower 1 (draw, load image, check level up for tower, x and y start coordinates)"""
        # variable "flag_level_tower" the amount depends on the number of tower levels drawn in a
        # folder with "resources". Default = 0 => 1 Level

        sprite_tower_1_x = self.surface.get_width() - self.sprite_tower_1.get_width()
        sprite_tower_1_y = self.surface.get_height() - self.sprite_tower_1.get_height()
        block = []
        block1 = self.surface((x, y))
        block1.set_alpha(80)
        block1.fill((255, 0, 0))
        block1_rect = pygame.Rect(0, 0, block1.get_width(), block1.get_height())
        block.append((block1, block1_rect))
        self.surface.blit(block[0])











