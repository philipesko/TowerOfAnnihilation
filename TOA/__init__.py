import pygame
import time

from main_window import CreateMainWindow
from check_pos import CheckMousePos
from scene_one import Scene1
from Tower import SpriteTower
from creep_all import Creep_blue_1, Creep_green_1, Creep_red_1, Creep_blue_2, Creep_green_2, Creep_red_2, Creep_blue_3, Creep_green_3, Creep_red_3, Boss
from config import GRID


class MainLoop:

    def __init__(self):
        # Initializing - no need to init() in main loop
        pygame.init()
        # Known bug - high CPU usage
        pygame.mixer.quit()
        self._running = True
        self._switch_scene = False
        self.health_left = 20  # Initial health
        self.wave = True  # Activate first wave
        self.creep_current = 0  # Current enemy type
        self.FPS = pygame.time.Clock()
        self.CMW = CreateMainWindow()
        self.scene_one_call = Scene1()
        self.timer_creep = time.time()
        # Tracking mouse events
        self.click_event = CheckMousePos()
        self.tower_group = []
        self.creep_group = []

    def run(self):
        """Main loop"""
        while self._running:
            # Start a new level
            if self._switch_scene:
                # Create a new level
                self.scene_one_call.create()
                self.scene_one_call.show_mouse_position_with_px(f'Health left: {self.health_left}', (10, 10), 10)
                self.scene_one_call.show_mouse_position_with_px(f'Current wave: {self.creep_current + 1}', (10, 30), 10)

                # Release the craken!
                self.release_the_craken()

            else:
                self.CMW.create()

                if not self.CMW.isrunning:
                    self._running = False
                if self.CMW.switch_scene:
                    self._switch_scene = True

            for event in pygame.event.get():
                """Quit from game if player pushes button ESC"""
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    self._running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_1 and not self.creep_group:
                    self.scene_one_call.show_mouse_position_with_px(f'next wave', (500, 20), 20)
                    if self.creep_current < 9:
                        self.creep_current += 1
                    else:
                        self.creep_current = 0
                    self.wave = True

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and \
                        self.click_event.get_cell_coordinate(pygame.mouse.get_pos()):
                    try:
                        coord = self.click_event.get_cell_coordinate(
                            self.click_event.get_cell_coordinate(pygame.mouse.get_pos()))
                        spite_tower = SpriteTower(x=coord[0], y=coord[1])
                        cell_name = self.click_event.get_cell_name(pygame.mouse.get_pos())
                        GRID[cell_name]['is_active'] = False
                        self.tower_group.append(spite_tower)
                        print('Tower added to group')
                        # if not self.creep_group:
                        list(map(lambda x: x.add_enemy_to_list(self.creep_group), self.tower_group))
                    except:
                        print('Not complete added tower to group')

            for x in self.creep_group:
                a = x.creep_center

            for creepy in self.creep_group:
                center = creepy.creep_center

            list(map(lambda x: x.update(center), self.tower_group))
            list(map(lambda x: x.draw(), self.tower_group))
            pygame.display.flip()
            self.FPS.tick(30)

        pygame.quit()
        quit()

    def release_the_craken(self):

        creep_types = [Creep_blue_1(), Creep_green_1(), Creep_red_1(),
                       Creep_blue_2(), Creep_green_2(), Creep_red_2(),
                       Creep_blue_3(), Creep_green_3(), Creep_red_3(),
                       Boss()]

        if not self.creep_group and time.time() - self.timer_creep >= 20:

            if self.creep_current < 9:
                self.creep_current += 1
                print(f'step{self.creep_current}')
            else:
                self.creep_current = 0
            self.wave = True

        if len(self.creep_group) == 10:
            self.wave = False
            self.timer_wave = time.time()

        if self.wave:
            if self.creep_current == 9:
                self.pack_size = 1 # Размер волны для босса
            else:
                self.pack_size = 10 # Стандартный азмер волны
            if time.time() - self.timer_creep >= 0.5 and len(self.creep_group) < self.pack_size:
                self.timer_creep = time.time()
                print(f'in wave {self.creep_current}')
                self.creep_group.append(creep_types[self.creep_current])

        for self.creep in self.creep_group:
            if self.creep.creep_health <= 0:
                self.creep_group.remove(self.creep)
            self.creep.move()
            if self.creep.damage_player:
                self.health_left -= 1
                self.creep_group.remove(self.creep)
                if self.health_left <= 0:
                    print('        Bad luck, fist fuck...')
                    self._running = False


if __name__ == "__main__":
    APP = MainLoop()
    APP.run()
