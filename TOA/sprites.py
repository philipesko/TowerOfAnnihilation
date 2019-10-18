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

    def create_tower_1(self, surface, flag_level_tower=0):
        """"Create tower 1 (draw, load image, check level up for tower, x and y start coordinates)"""
        # variable "flag_level_tower" the amount depends on the number of tower levels drawn in a
        # folder with "resources". Default = 0 => 1 Level
        sprite_tower_1 = pygame.image.load(os.path.join(self._path_to_sprite, self._image_tower1[flag_level_tower]))
        sprite_tower_1 = pygame.transform.scale(sprite_tower_1, (58, 58))
        return sprite_tower_1


class SpriteEnemy(pygame.sprite.Sprite):
    """ Class for enemy sprite"""

    def __init__(self):
        super(pygame.sprite.Sprite, self).__init__()
        self._path_to_sprite_enemy = os.path.join(PATH_TO_RESOURCE, 'creep\creep-1-blue')
        self._images_enemy1 = ['1.png', '2.png', '3.png', '4.png', '5.png', '6.png']
        self.index = 0
        self.image = pygame.image.load(os.path.join(self._path_to_sprite_enemy, self._images_enemy1[self.index]))
        self.rect = pygame.Rect(2, 2, 50, 50)
        # self.image = self._images_enemy1[self.index]

    def update(self):
        self.index += 1
        if self.index >= len(self.image):
            self.index = 0
        self.image = self._images_enemy1[self.index]
        # return self.image
