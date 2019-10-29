import pygame
import os.path

from config import PATH_TO_RESOURCE, SURFACE


class SpriteTower(pygame.sprite.Sprite):
    """Abstract Class for Towers """

    def __init__(self, level_tower=2, x=500, y=500, scale_x=50, scale_y=50):
        super(pygame.sprite.Sprite, self).__init__()

        self._path_to_sprite = os.path.join(PATH_TO_RESOURCE, 'tower-defense-turrets')
        self._image_tower1 = ['turret-1-1.png', 'turret-1-2.png', 'turret-1-3.png']
        self.angle = 0
        self.sprite_tower_1 = None
        self.x = None
        self.y = None
        self.surface = SURFACE
        self.level = None
        self.selected = False  # need change this value for show radius damage
        # temporary values:
        self.range = 100
        self.range_center = self.range
        self.x = x + 28
        self.y = y + 28
        self.pos = (self.x, self.y)
        self.level = level_tower
        # variable "flag_level_tower" the amount depends on the number of tower levels drawn in a
        # folder with "resources". Default = 0 => 1 Level
        self.sprite_tower_1 = pygame.image.load(os.path.join(self._path_to_sprite,
                                                             self._image_tower1[self.level])).convert_alpha()
        self.orig_image = self.sprite_tower_1
        self.rect = self.sprite_tower_1.get_rect(center=self.pos)

        self.sprite_tower_1 = pygame.transform.scale(self.sprite_tower_1, (scale_x, scale_y))

    def turn_tower(self, enemy_position):
        """
        Method for turn the tower on angle
        :param enemy_position:
        """
        center = pygame.math.Vector2(self.rect.center)
        mouse_position = pygame.math.Vector2(enemy_position)

        r, self.angle = (mouse_position - center).as_polar()
        # r - radius  damage
        if r <= 100:
            self.orig_image = pygame.transform.rotate(self.orig_image, -self.angle - 90)
            self.rect = self.orig_image.get_rect(center=self.rect.center)

    def draw_tower(self):
        """
        Method draw for tower sprites.
        """
        self.surface.blit(self.orig_image, self.rect)

    def draw_radius(self):
        if self.selected:
            # draw range circle
            surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
            pygame.draw.circle(surface, (128, 128, 128, 100), (self.range, self.range), self.range, 0)

            self.surface.blit(surface, (self.x - self.range_center, self.y - self.range_center))
