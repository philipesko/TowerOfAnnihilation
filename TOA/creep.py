import os.path
import pygame
from config import PATH_TO_RESOURCE, SURFACE, GRID


class Creep:

    def __init__(self):

        self.surface = SURFACE
        self.route = [[GRID['7:0']['coord'][0], -150], GRID['7:4']['coord'],
                      GRID['12:4']['coord'], GRID['12:8']['coord'],
                      GRID['10:8']['coord'], GRID['10:9']['coord'],
                      GRID['3:9']['coord'], GRID['3:11']['coord'],
                      GRID['10:11']['coord'], [GRID['10:11']['coord'][0], 799]]
        self.target_point = 1
        self.creep_x = self.route[0][0]
        self.creep_y = self.route[0][1]
        self.damage_player = False
        self.creep_center = self.creep_x + 23, self.creep_y + 23
        self.shoot = False
        self.creep_health = 0
        self.max_health = 0
        self.reward = 0
        self.speed = 0
        self.animation_count = 0
        # Creep level 1
        self.creep_imgs = [self.load_image('creep-1-blue/1.png'),
                           self.load_image('creep-1-blue/2.png'),
                           self.load_image('creep-1-blue/3.png'),
                           self.load_image('creep-1-blue/4.png'),
                           self.load_image('creep-1-blue/5.png'),
                           self.load_image('creep-1-blue/6.png')]
        self.creep_img_original = self.creep_imgs[self.animation_count]
        # self.hit = 0

    def move(self):
        '''
        Moving enemy
        '''
        self.damage_player = False  # Resetting damage flag
        self.animate()  # Animating creep

        # Let's move!
        self.target_x, self.target_y = self.route[self.target_point]
        # Moving down
        if self.target_x - self.creep_x == 0:
            self.creep_img_original = pygame.transform.rotate(self.creep_img_original, -90)
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
            self.creep_img_original = pygame.transform.rotate(self.creep_img_original, 180)
            self.creep_x -= self.speed
            if self.creep_x <= self.target_x:
                self.move_to_the_next()

        # Draw a creep
        self.surface.blit(self.creep_img_original, (self.creep_x + 6, self.creep_y + 6))
        self.draw_health_bar()

        # If creep left screen, switch damage flag to True
        if self.creep_y >= self.route[9][1]:
            self.damage_done()
        self.creep_center = self.creep_x + 29, self.creep_y + 29

    def move_to_the_next(self):

        self.creep_x, self.creep_y = self.target_x, self.target_y
        self.target_point += 1
        if self.target_point >= len(self.route):
            self.target_point = 1
        self.target_x, self.target_y = self.route[self.target_point]

    def animate(self):

        self.animation_count += 0.5  # Switching animation in turns
        if self.animation_count >= len(self.creep_imgs):
            self.animation_count = 0
        self.creep_img_original = self.creep_imgs[int(self.animation_count)]

    def damage_done(self):

        self.target_point = 1
        self.damage_player = True

    def draw_health_bar(self):

        length = self.creep_img_original.get_rect()[2] - 6
        move_by = length / self.max_health
        health_bar = round(move_by * self.creep_health)

        pygame.draw.rect(self.surface, (255,0,0), (self.creep_x + 7, self.creep_y, length, 3), 0)
        pygame.draw.rect(self.surface, (0, 255, 0), (self.creep_x + 7, self.creep_y, health_bar, 3), 0)

    def load_image(self, img):
        '''
        Load image from file path
        img: The name of the image to load
        '''
        self.path_to_creep = os.path.join(PATH_TO_RESOURCE, 'creep/' + img)
        return pygame.image.load(self.path_to_creep)
