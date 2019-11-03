import os.path
import pygame
from config import PATH_TO_RESOURCE, SURFACE, GRID, MAIN_SIZE_FOR_WINDOW


class Creep(pygame.sprite.Sprite):

    def __init__(self):

        self.surface = SURFACE
        self.route = [[GRID['7:0']['coord'][0], -53], GRID['7:4']['coord'],
                      GRID['12:4']['coord'], GRID['12:8']['coord'],
                      GRID['10:8']['coord'], GRID['10:9']['coord'],
                      GRID['3:9']['coord'], GRID['3:11']['coord'],
                      GRID['10:8']['coord'], GRID['10:11']['coord'],
                      [GRID['10:11']['coord'][0], 800]]
        self.route_passed = []
        self.offset()  # Need to handle grid change in future
        self.creep_x = self.route[0][0]
        self.creep_y = self.route[0][1]
        self.speed = 5
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
        self.blue_creep1_origin = self.blue_creep3[self.animation_count]

    def move(self):
        '''
        Moving enemy
        '''
        self.damage = False  # Resetting damage flag
        self.animation_count += 1  # Switching animation in turns
        if self.animation_count >= len(self.blue_creep1):
            self.animation_count = 0
        self.blue_creep1_origin = self.blue_creep1[self.animation_count]
        self.blue_creep1_origin = pygame.transform.rotate(self.blue_creep1_origin, -90)

        self.creep_y += self.speed
        self.surface.blit(self.blue_creep1_origin, (self.creep_x, self.creep_y))

        # print(self.creep_x, self.creep_y)

        # If creep left screenm reset coordinates, switch damage flag to True
        if self.creep_y >= 808:
            self.creep_x = self.route[0][0]
            self.creep_y = self.route[0][1]
            self.damage = True

    def offset(self):
        for i in self.route:
            if i == 0:
                continue
            i[0] += 6
            i[1] += 6
        return self.route

    def load_image(self, img):
        '''
        Load image from file path
        img: The name of the image to load
        '''
        self.path_to_creep = os.path.join(PATH_TO_RESOURCE, 'creep/' + img)
        return pygame.image.load(self.path_to_creep)
