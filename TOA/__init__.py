import pygame

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
        self.FPS = pygame.time.Clock()
        self.CMW = CreateMainWindow()
        self.scene_one_call = Scene1()
        self.creep = Creep()
        self.creep1 = Creep(start_y=-150)
        self.creep2 = Creep(start_y=-200)
        self.creep3 = Creep(start_y=-250)
        self.creep4 = Creep(start_y=-300)
        self.creep5 = Creep(start_y=-350)
        # Tracking mouse events
        self.click_event = CheckMousePos()
        self.tower_group = []
        self.creep_group = [self.creep, self.creep1, self.creep2, self.creep3, self.creep4, self.creep5]
        self.target = None

    def run(self):
        """Main loop"""
        while self._running:
            # Start a new level
            if self._switch_scene:
                # Create a new level
                self.scene_one_call.create()
                self.scene_one_call.show_mouse_position_with_px(self.health_left)
                # Release the craken!


                # self.creep_group.append(Creep(start_y=y-30))
                # self.creep_group.append(Creep(start_y=y-60))
                # self.creep_group.append(Creep(start_y=y-90))
                # self.creep_group.append(Creep(start_y=y-120))

                for enemy in self.creep_group:
                    enemy.move()
                # self.target = self.creep_group[0].creep_center

                if self.creep.damage:
                    self.health_left -= 1
                    if self.health_left <= 0:
                        print('        Bad luck, fist fuck...')
                        self._running = False

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
                # if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # self.click_event.mouse_coordinates(pygame.mouse.get_pos())

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and \
                        self.click_event.get_cell_coordinate(pygame.mouse.get_pos()):
                    try:
                        coord = self.click_event.get_cell_coordinate(
                            self.click_event.get_cell_coordinate(pygame.mouse.get_pos()))
                        spite_tower = SpriteTower(x=coord[0], y=coord[1])
                        cell_name = self.click_event.get_cell_name(pygame.mouse.get_pos())
                        GRID[cell_name]['is_active'] = False  # <- Здесь косяк: откуда-то берётся ячейка 8:13, хотя в гриде её нет. Игра крашится
                        self.tower_group.append(spite_tower)
                        print('Tower added to group')
                    except:
                        print('Not complete added tower to group')



            for creepy in self.creep_group:
                center = creepy.creep_center
                list(map(lambda x: x.update(center), self.tower_group))
            # list(map(lambda x: x.update(self.target), self.tower_group))
            # list(map(lambda x: x.update(self.creep1.creep_center), self.tower_group))
            list(map(lambda x: x.draw(), self.tower_group))
            pygame.display.flip()
            self.FPS.tick(30)

        pygame.quit()
        quit()


if __name__ == "__main__":
    APP = MainLoop()
    APP.run()
