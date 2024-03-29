import pygame
import os.path

from config import PATH_TO_RESOURCE, SURFACE


class SpriteTower(pygame.sprite.Sprite):
    """Abstract Class for Towers """

    def __init__(self, level_tower=0, x=0, y=0):

        self._path_to_sprite = os.path.join(PATH_TO_RESOURCE, 'tower-defense-turrets')
        self._image_tower1 = ['turret-1-1.png', 'turret-1-2.png', 'turret-1-3.png']
        self.angle = 0
        self.surface = SURFACE
        self.level = None
        self.level = level_tower
        self.selected = False  # need change this value for show radius damage
        # temporary values:
        self.range = 150
        self.range_center = self.range
        self.x = x + 28
        self.y = y + 28
        self.pos = (self.x, self.y)
        # variable "flag_level_tower" the amount depends on the number of tower levels drawn in a
        # folder with "resources". Default = 0 => 1 Level
        self.image = pygame.image.load(os.path.join(self._path_to_sprite,
                                                    self._image_tower1[self.level]))
        self.orig_image = self.image
        self.rect = self.image.get_rect(center=self.pos)
        self.enemy_position = None
        self.enemy_position_vec = 0, 0
        self.in_range = False
        self.enemy_position_list = []
        self.radius_to_enemy_list = []
        self.enemy_obj_list = []
        self.creep_count = 0
        self.radius = None
        self.center = None

    def update(self, enemy_pos: object = None) -> object:
        """
        Method update for tower sprites.
        :param enemy_pos:
        """
        if self.enemy_obj_list and self.creep_count < len(self.enemy_obj_list):
            self.turn_tower()
        else:
            self.creep_count = 0

    def add_enemy_to_list(self, enemy_obj):
        """
        Set enemy objects from enemy obj list.
        Identify near the enemy object to Tower.
        :rtype: object
        """
        self.enemy_obj_list = enemy_obj

    def draw(self):
        self.surface.blit(self.image, self.rect)
        self.draw_radius()

    def draw_radius(self):
        """
        Draw radius for Tower.
        """
        if self.selected:
            surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
            pygame.draw.circle(surface, (128, 128, 128, 100), (self.range, self.range), self.range, 0)

            self.surface.blit(surface, (self.x - self.range_center, self.y - self.range_center))

    def calculate_radius_and_angle(self):
        self.center = pygame.math.Vector2(self.rect.center)
        self.enemy_position_vec = pygame.math.Vector2(self.enemy_obj_list[self.creep_count].creep_center)

        self.radius, self.angle = (self.enemy_position_vec - self.center).as_polar()
        if self.angle >= 359:
            self.angle = 0

        if self.range:
            # self.radius_to_enemy_list.append(self.radius)
            self.enemy_position_list.append(self.enemy_obj_list[self.creep_count].creep_center)
        else:
            self.enemy_position_list.remove(self.enemy_obj_list[self.creep_count].creep_center)
            # self.radius_to_enemy_list.remove(self.radius)

    def turn_tower(self):
        """
        Method for turn the tower on angle
        :param enemy_position:
        """
        self.calculate_radius_and_angle()
        if self.radius <= self.range:
            self.in_range = True

            self.image = pygame.transform.rotate(self.orig_image, -self.angle - 90)
            self.rect = self.image.get_rect(center=self.rect.center)
            pygame.draw.aaline(SURFACE, pygame.Color(150, 250, 100), self.center, self.enemy_position_vec, 3)
            self.enemy_obj_list[self.creep_count].creep_health -= 0.5

        if self.radius > self.range and self.in_range:
            self.creep_count += 1
            self.in_range = False
            if self.creep_count >= len(self.enemy_obj_list):
                self.creep_count = 0
