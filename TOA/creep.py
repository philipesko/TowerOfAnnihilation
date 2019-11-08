import os.path
import pygame
from config import PATH_TO_RESOURCE, SURFACE, GRID


class Creep(pygame.sprite.Sprite):

    def __init__(self):

        self.surface = SURFACE
        self.route = [[GRID['7:0']['coord'][0], -106], GRID['7:4']['coord'],
                      GRID['12:4']['coord'], GRID['12:8']['coord'],
                      GRID['10:8']['coord'], GRID['10:9']['coord'],
                      GRID['3:9']['coord'], GRID['3:11']['coord'],
                      GRID['10:11']['coord'], [GRID['10:11']['coord'][0], 802]]
        self.target_point = 1
        # self.offset()  # Need to handle grid change in future
        self.creep_x = self.route[0][0]
        self.creep_y = self.route[0][1]
        self.creep_center = self.creep_x + 23, self.creep_y + 23
        self.creep_health = 30
        self.speed = 3
        self.animation_count = 0
        # Creep level 1
        self.blue_creep1 = [self.load_image('creep-1-blue/1.png'),
                            self.load_image('creep-1-blue/2.png'),
                            self.load_image('creep-1-blue/3.png'),
                            self.load_image('creep-1-blue/4.png'),
                            self.load_image('creep-1-blue/5.png'),
                            self.load_image('creep-1-blue/6.png')]
        self.blue_creep1_origin = self.blue_creep1[self.animation_count]
        # Creep level 2
        self.blue_creep2 = [self.load_image('creep-2-blue/1.png'),
                            self.load_image('creep-2-blue/2.png'),
                            self.load_image('creep-2-blue/3.png'),
                            self.load_image('creep-2-blue/4.png')]
        self.blue_creep2_origin = self.blue_creep2[self.animation_count]
        # Creep level 3
        self.blue_creep3 = [self.load_image('creep-3-blue/1.png'),
                            self.load_image('creep-3-blue/2.png'),
                            self.load_image('creep-3-blue/3.png'),
                            self.load_image('creep-3-blue/4.png')]
        self.blue_creep3_origin = self.blue_creep3[self.animation_count]

    def move(self):
        '''
        Moving enemy
        '''
        self.damage = False  # Resetting damage flag
        self.animate()  # Animating creep

        # Let's move!
        self.target_x, self.target_y = self.route[self.target_point]
        # Moving down
        if self.target_x - self.creep_x == 0:
            self.blue_creep1_origin = pygame.transform.rotate(self.blue_creep1_origin, -90)
            self.creep_y += self.speed
            if self.creep_y >= self.target_y:
                self.move_to_the_next()
        # Moving right
        if self.target_y - self.creep_y == 0 and self.creep_x - self.target_x <= 0:
            self.creep_x += self.speed
            if self.creep_x >= self.target_x:
                self.move_to_the_next()
        # Moving left
        if self.target_x - self.creep_x <= 0 and self.creep_y == self.target_y:
            self.blue_creep1_origin = pygame.transform.rotate(self.blue_creep1_origin, 180)
            self.creep_x -= self.speed
            if self.creep_x <= self.target_x:
                self.move_to_the_next()

        # print(self.creep_x, self.creep_y)
        self.surface.blit(self.blue_creep1_origin, (self.creep_x, self.creep_y))

        # If creep left screen reset coordinates, switch damage flag to True
        if self.creep_y >= self.route[9][1]:
            self.damage_done()
        self.creep_center = self.creep_x + 23, self.creep_y + 23

        # return self.creep_center

    def move_to_the_next(self):

        self.creep_x, self.creep_y = self.target_x, self.target_y
        self.target_point += 1
        if self.target_point >= len(self.route):
            self.target_point = 1
        self.target_x, self.target_y = self.route[self.target_point]

    def animate(self):
        self.animation_count += 0.5  # Switching animation in turns
        if self.animation_count >= len(self.blue_creep1):
            self.animation_count = 0
        self.blue_creep1_origin = self.blue_creep1[int(self.animation_count)]

    def damage_done(self):

        self.creep_x = self.route[0][0]
        self.creep_y = self.route[0][1]
        self.target_point = 1
        self.damage = True

    def load_image(self, img):
        '''
        Load image from file path
        img: The name of the image to load
        '''
        self.path_to_creep = os.path.join(PATH_TO_RESOURCE, 'creep/' + img)
        return pygame.image.load(self.path_to_creep)
