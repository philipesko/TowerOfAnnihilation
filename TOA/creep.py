import os.path
import pygame
from config import PATH_TO_RESOURCE, SURFACE, GRID


class Creep(pygame.sprite.Sprite):

    def __init__(self):

        self.surface = SURFACE
        self.route = []
        # Creep level 1
        self.blue_creep1 = [self.load_image('creep-1-blue/1.png'),
                            self.load_image('creep-1-blue/2.png'),
                            self.load_image('creep-1-blue/3.png'),
                            self.load_image('creep-1-blue/4.png'),
                            self.load_image('creep-1-blue/5.png'),
                            self.load_image('creep-1-blue/6.png')]
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
        self.draw_creep(self.blue_creep2[0], GRID['7:0']['coord'])

    def draw_creep(self, creep, coordinates):
        # Offset for coordinates
        offset = 6, 6
        coordinates = [sum(i) for i in zip(coordinates, offset)]
        self.surface.blit(creep, coordinates)

    # def update(self):


    def load_image(self, img):
        '''
        Load image from file path
        img: The name of the image to load
        '''
        self.path_to_creep = os.path.join(PATH_TO_RESOURCE, 'creep/' + img)
        return pygame.image.load(self.path_to_creep)


if __name__ == '__main__':
    Creep()
