import pygame
import os.path

from config import PATH_TO_RESOURCE, SURFACE


class SpriteTower(pygame.sprite.Sprite):
    """Abstract Class for Towers """
    def __init__(self):
        super(pygame.sprite.Sprite, self).__init__()
        self._path_to_sprite = os.path.join(PATH_TO_RESOURCE, 'tower-defense-turrets')
        self._image_tower1 = ['turret-1-1.png', 'turret-1-2.png', 'turret-1-3.png']
        self.angle = None
        self.sprite_tower_1 = None
        self.x = None
        self.y = None
        self.surface = SURFACE
        self.level = None
        self.selected = False
        # temporary values:
        self.range = 100
        self.range_center = self.range - 24

    def set_param_tower(self, level_tower=2, x=500, y=500, scale_x=50, scale_y=50):
        """"Create tower 1 (draw, load image, check level up for tower, x and y start coordinates)
        :param scale_x:
        :param scale_y:
        :param level_tower: load image with compare with level tower.
        :param x: Position X on window
        :param y: Position Y on window
        """
        self.x = x + 4
        self.y = y + 4
        self.level = level_tower
        # variable "flag_level_tower" the amount depends on the number of tower levels drawn in a
        # folder with "resources". Default = 0 => 1 Level
        self.sprite_tower_1 = pygame.image.load(os.path.join(self._path_to_sprite,
                                                             self._image_tower1[self.level]))
        # tmp scale
        self.sprite_tower_1 = pygame.transform.scale(self.sprite_tower_1, (scale_x, scale_y))

        # To do

    def turn_tower(self, angle):
        """
        Method for turn the tower on angle
        :param angle:
        """
        self.angle = angle
        self.sprite_tower_1 = pygame.transform.rotate(self.sprite_tower_1, self.angle)

    def draw_tower(self):
        """
        Method draw for tower sprites.
        """
        self.surface.blit(self.sprite_tower_1, (self.x, self.y))

    def draw_radius(self):
        if self.selected:
            # draw range circle
            surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
            pygame.draw.circle(surface, (128, 128, 128, 100), (self.range, self.range), self.range, 0)

            self.surface.blit(surface, (self.x - self.range_center, self.y - self.range_center))




