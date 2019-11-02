import pygame

from main_window import CreateMainWindow
from check_pos import CheckMousePos
from scene_one import Scene1
from Tower import SpriteTower
from config import SURFACE


class MainLoop:

    def __init__(self):
        # Initializing - no need to init() in main loop
        pygame.init()
        # Known bug - high CPU usage
        pygame.mixer.quit()
        self._running = True
        self._switch_scene = False
        self.FPS = pygame.time.Clock()
        self.CMW = CreateMainWindow()
        self.scene_one_call = Scene1()
        # self.sprite = SpriteTower()
        # Tracking mouse events
        self.click_event = CheckMousePos()
        self.tower_group = []

    def on_cleanup(self):
        # Clear all. Need use before exit from game
        pygame.quit()
        quit()

    def run(self):
        """Main loop"""
        while self._running:
            # switch between windows if flag _switch_scene is true:
            if self._switch_scene:
                create_scene_one_call = self.scene_one_call.create()
                # TMP create sprite.
                # self.sprite.create_tower_1()
            else:
                create_main_window = self.CMW.create()

                if not self.CMW.isrunning:
                    self._running = False
                if self.CMW.switch_scene:
                    self._switch_scene = True

            for event in pygame.event.get():
                """Quit from game if player pushes button ESC"""
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    self._running = False
                    self.on_cleanup()
                # if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # self.click_event.mouse_coordinates(pygame.mouse.get_pos())

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and \
                        self.click_event.get_cell_coordinate(pygame.mouse.get_pos()):
                    try:
                        coord = self.click_event.get_cell_coordinate(
                            self.click_event.get_cell_coordinate(pygame.mouse.get_pos()))
                        spite_tower = SpriteTower(x=coord[0], y=coord[1])
                        self.tower_group.append(spite_tower)
                        print('True')
                    except:
                        print('Not True')

            mouse = pygame.mouse.get_pos()
            for x in self.tower_group:
                x.update(mouse)
            # list(map(lambda x:x.update(mouse), self.tower_group))
            # self.tower_group.update(self, mouse[0], mouse[1])
            # self.tower_group.draw(self)
            list(map(lambda x:x.draw(), self.tower_group))
            pygame.display.flip()
            self.FPS.tick(30)



if __name__ == "__main__":
    APP = MainLoop()
    APP.run()
