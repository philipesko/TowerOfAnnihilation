import pygame
import os.path

from config import PATH_TO_RESOURCE, MAIN_SIZE_FOR_WINDOW


class SpriteTower(pygame.sprite.Sprite):
    """Class for Towers"""

    def __init__(self):
        # pygame.sprite.Sprite.__init__(self)
        super(pygame.sprite.Sprite, self).__init__()
        self._path_to_sprite = os.path.join(PATH_TO_RESOURCE, 'tower-defense-turrets')
        self._image_tower1 = ['turret-1-1.png', 'turret-1-2.png', 'turret-1-3.png']
        # self.sprite_tower_1 = pygame.image.load(os.path.join(self._path_to_sprite, self._image_tower1[0]))

    def create_tower_1(self, surface, flag_level_tower=2, x=500, y=500):
        """"Create tower 1 (draw, load image, check level up for tower, x and y start coordinates)"""
        # variable "flag_level_tower" the amount depends on the number of tower levels drawn in a
        # folder with "resources". Default = 0 => 1 Level
        self.sprite_tower_1 = pygame.image.load(os.path.join(self._path_to_sprite, self._image_tower1[flag_level_tower]))
        # tmp scale
        self.sprite_tower_1 = pygame.transform.scale(self.sprite_tower_1, (50, 50))
        #surface.blit(self.sprite_tower_1, (x, y))
        self.sprite_tower_1 = pygame.transform.rotate(self.sprite_tower_1, 270)
        return self.sprite_tower_1
        #To do
