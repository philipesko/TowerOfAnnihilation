import os.path
import pygame
from config import PATH_TO_RESOURCE, SURFACE, GRID


class Creep(pygame.sprite.Sprite):

    def __init__(self):

        self.surface = SURFACE
        self.route = [[GRID['7:0']['coord'][0], -50], GRID['7:4']['coord'],
                      GRID['12:4']['coord'], GRID['12:8']['coord'],
                      GRID['10:8']['coord'], GRID['10:9']['coord'],
                      GRID['3:9']['coord'], GRID['3:11']['coord'],
                      GRID['10:8']['coord'], GRID['10:11']['coord'],
                      [GRID['10:11']['coord'][0], 800]]
        self.offset()
        print(GRID['10:11']['coord'])
        print(self.route[9])
        self.position = self.route[0]
        self._FLAG = True

        self.animation_count = 0
        self.speed = 5

        # Creep level 1
        self.blue_creep1 = [self.load_image('creep-1-blue/1.png'),
                            self.load_image('creep-1-blue/2.png'),
                            self.load_image('creep-1-blue/3.png'),
                            self.load_image('creep-1-blue/4.png'),
                            self.load_image('creep-1-blue/5.png'),
                            self.load_image('creep-1-blue/6.png')]
        self.blue_creep_origin = self.blue_creep1[0]
        # Creep level 2
        self.blue_creep2 = [self.load_image('creep-2-blue/1.png'),
                            self.load_image('creep-2-blue/2.png'),
                            self.load_image('creep-2-blue/3.png'),
                            self.load_image('creep-2-blue/4.png')]
        # Creep level 3
        self.blue_creep3 = [self.load_image('creep-3-blue/1.png'),
                            self.load_image('creep-3-blue/2.png'),
                            self.load_image('creep-3-blue/3.png'),
                            self.load_image('creep-3-blue/4.png')]

    def offset(self):
        for i in self.route:
            if i == 0:
                continue
            i[0] += 6
            i[1] += 6
        return self.route

    def move(self):
        '''
        Moving enemy
        '''
        if self.position <= self.route[1] and self._FLAG:
            self.moving_down()
            self.surface.blit(self.blue_creep1[0], self.position)
        elif self.position <= self.route[2] and self._FLAG:
            self.moving_right()
            self.surface.blit(self.blue_creep1[0], self.position)
        elif self.position <= self.route[3]:
            self.moving_down()
            self.surface.blit(self.blue_creep1[0], self.position)
            self._FLAG = False
        elif self.position >= self.route[4]:
            self.moving_left()
            self.surface.blit(self.blue_creep1[0], self.position)
        print(self.position)

    def moving_down(self):

        self.blue_creep1[0] = pygame.transform.rotate(self.blue_creep_origin, -90)
        self.route[0][1] += self.speed
        self.position = [self.route[0][0], self.route[0][1]]
        return self.blue_creep1[0], self.position

    def moving_right(self):

        self.blue_creep1[0] = pygame.transform.rotate(self.blue_creep_origin, 0)
        self.route[0][0] += self.speed
        self.position = [self.route[0][0], self.route[0][1]]
        return self.blue_creep1[0], self.position

    def moving_left(self):

        self.blue_creep1[0] = pygame.transform.rotate(self.blue_creep_origin, 180)
        self.route[0][0] -= self.speed
        self.position = [self.route[0][0], self.route[0][1]]
        return self.blue_creep1[0], self.position

    def load_image(self, img):
        '''
        Load image from file path
        img: The name of the image to load
        '''
        self.path_to_creep = os.path.join(PATH_TO_RESOURCE, 'creep/' + img)
        return pygame.image.load(self.path_to_creep)
