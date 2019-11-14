import pygame
import time


from main_window import CreateMainWindow
from check_pos import CheckMousePos
from scene_one import Scene1
from Tower import SpriteTower
from creep_all import *
from config import GRID



class MainLoop:

    def __init__(self):

        pygame.init()
        self._running = True
        self._switch_scene = False
        self.player_health_left = 20  # Initial health
        self.wave = True  # Activate first wave
        self.wave_trigger = 0
        self.creep_wave_current = 0  # Current enemy type
        self.FPS = pygame.time.Clock()
        self.CMW = CreateMainWindow()
        self.scene_one_call = Scene1()
        self.timer_creep = time.time()
        self.mouse_position = CheckMousePos()
        self.tower_group = []
        self.creep_group = []

    def run(self):
        """Main loop"""
        while self._running:

            # Start a new level
            if self._switch_scene:
                # Create a new level
                self.scene_one_call.create()
                self.draw_text()
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
                # Change cursor type with interactive object
                if self._switch_scene:
                    self.mouse_position.cursor_type(pygame.mouse.get_pos())
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    self._running = False
                # Force next wave
                if event.type == pygame.KEYDOWN and event.key == pygame.K_1 and not self.wave_trigger and self._switch_scene:
                    self.scene_one_call.show_mouse_position_with_px(f'next wave', (500, 20), 20)
                    self.check_conditions()
                    self.generate_new_wave()
                # Build new tower
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and \
                        self.mouse_position.mouse_coordinates(pygame.mouse.get_pos(), False) \
                        and self._switch_scene:
                    self.build_tower()

            # Fire!
            for creepy in self.creep_group:
                center = creepy.creep_center
            list(map(lambda x: x.update(center), self.tower_group))
            list(map(lambda x: x.draw(), self.tower_group))

            pygame.display.flip()
            self.FPS.tick(60)

        pygame.quit()
        quit()

    def draw_text(self):

        self.scene_one_call.show_mouse_position_with_px(f'Health left: {self.player_health_left}', (10, 10), 10)
        self.scene_one_call.show_mouse_position_with_px(f'Current wave: {self.creep_wave_current + 1}/10', (10, 30), 10)

    def build_tower(self):

        coord = self.mouse_position.mouse_coordinates(pygame.mouse.get_pos(), False)
        spite_tower = SpriteTower(x=coord[0], y=coord[1])
        cell_name = self.mouse_position.mouse_coordinates(pygame.mouse.get_pos(), True)
        GRID[cell_name]['towerlevel'] = 1
        self.tower_group.append(spite_tower)
        print('added')
        list(map(lambda x: x.add_enemy_to_list(self.creep_group), self.tower_group))

    def check_conditions(self):

        if self.creep_wave_current < 9:
            self.creep_wave_current += 1
            print(f'step{self.creep_wave_current}')
        else:
            self.creep_wave_current = 0
        self.wave = True

    def release_the_craken(self):

        # Launching new wave
        if not self.creep_group and time.time() - self.timer_creep >= 20:
            self.check_conditions()
        if self.wave:
            if self.creep_wave_current == 9:
                self.pack_size = 1  # Boss wave size
            else:
                self.pack_size = 10  # Standard wave size
            # Generating wave out of 10
            self.generate_new_wave()

        for self.creep in self.creep_group:
            # Check if dead, move if alive
            if self.creep.creep_health <= 0:
                self.creep_group.remove(self.creep)
            else:
                self.creep.move()
            # Damaging player by creep
            if self.creep.damage_player:
                self.player_health_left -= 1
                self.creep_group.remove(self.creep)
                # if player
                if self.player_health_left <= 0:
                    print('        Bad luck, fist fuck...')
                    self._running = False

    def generate_new_wave(self):

        creep_types = [Creep_blue_1(), Creep_green_1(), Creep_red_1(),
                       Creep_blue_2(), Creep_green_2(), Creep_red_2(),
                       Creep_blue_3(), Creep_green_3(), Creep_red_3(),
                       Boss()]

        if time.time() - self.timer_creep >= 0.7:
            self.wave_trigger += 1
            self.timer_creep = time.time()
            print(f'in wave {self.creep_wave_current}')
            self.creep_group.append(creep_types[self.creep_wave_current])
        if self.wave_trigger == self.pack_size:
            self.wave_trigger = 0
            self.wave = False
            self.timer_wave = time.time()


if __name__ == "__main__":
    APP = MainLoop()
    APP.run()
