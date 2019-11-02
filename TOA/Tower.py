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
        self.surface = SURFACE
        self.level = None
        self.selected = True  # need change this value for show radius damage
        # temporary values:
        self.range = 100
        self.range_center = self.range
        self.x = x + 25
        self.y = y + 25
        self.pos = (self.x, self.y)
        self.level = level_tower
        # variable "flag_level_tower" the amount depends on the number of tower levels drawn in a
        # folder with "resources". Default = 0 => 1 Level
        self.image = pygame.image.load(os.path.join(self._path_to_sprite,
                                                    self._image_tower1[self.level]))
        self.orig_image = self.image
        self.rect = self.image.get_rect(center=self.pos)
        self.enemy_position = 0, 0
        self.turn_tower()
        # self.image = pygame.transform.scale(self.image, (scale_x, scale_y))

    def update(self, enemy_pos):
        """
        Method update for tower sprites.
        """
        self.enemy_position = enemy_pos

        self.turn_tower()
        # self.surface.blit(self.orig_image, self.rect)
        # SpriteTower.draw_radius(self)

    def draw(self):
        self.surface.blit(self.image, self.rect)
        self.draw_radius()

    def draw_radius(self):
        if self.selected:
            # draw range circle
            surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
            pygame.draw.circle(surface, (128, 128, 128, 100), (self.range, self.range), self.range, 0)

            self.surface.blit(surface, (self.x - self.range_center, self.y - self.range_center))

    def turn_tower(self):
        """
        Method for turn the tower on angle
        :param enemy_position:
        """
        center = pygame.math.Vector2(self.rect.center)
        mouse_position = pygame.math.Vector2(self.enemy_position)

        r, self.angle = (mouse_position - center).as_polar()
        if self.angle >= 359:
            self.angle = 0
        # r - radius  damage
        if r <= 100:
            self.image = pygame.transform.rotate(self.orig_image, -self.angle - 90)
            self.rect = self.image.get_rect(center=self.rect.center)
            # self.image = self.rect
