import pygame
import time
import random

from main_window import CreateMainWindow
from check_pos import CheckMousePos
from scene_one import Scene1
from Tower import SpriteTower
from creep import Creep
from config import GRID


class MainLoop:

    def __init__(self):
        # Initializing - no need to init() in main loop
        pygame.init()
        # Known bug - high CPU usage
        pygame.mixer.quit()
        self._running = True
        self._switch_scene = False
        # Initial health
        self.health_left = 20
        self.wave = True
        self.FPS = pygame.time.Clock()
        self.CMW = CreateMainWindow()
        self.scene_one_call = Scene1()
        self.creep_types = [Creep()]  # Сюда поместить список всех крипов и каждую волну подменять тип
        self.timer_creep = time.time()
        self.timer_wave = time.time()
        # Tracking mouse events
        self.click_event = CheckMousePos()
        self.tower_group = []
        self.creep_pack = []
        self.creep_group = [self.creep_pack]

    def run(self):
        """Main loop"""
        while self._running:
            # Start a new level
            if self._switch_scene:
                # Create a new level
                self.scene_one_call.create()
                self.scene_one_call.show_mouse_position_with_px(self.health_left)

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
                if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
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

            for creepy in self.creep_group:
                center = creepy.creep_center

            list(map(lambda x: x.update(center), self.tower_group))
            list(map(lambda x: x.draw(), self.tower_group))
            pygame.display.flip()
            self.FPS.tick(30)

        pygame.quit()
        quit()

    def release_the_craken(self):

        if not self.creep_group and time.time() - self.timer_creep >= 30:
            self.wave = True

        if len(self.creep_group) == 10:
            self.wave = False
            self.timer_wave = time.time()

        elif self.wave:
            if time.time() - self.timer_creep >= 0.5 and len(self.creep_group[0]) < 10:
                self.timer_creep = time.time()
                self.creep_pack.append(Creep())
                self.creep_group.append(self.creep_pack)
        for self.creep in self.creep_group[0]:
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
