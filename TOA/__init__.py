import pygame


from main_window import CreateMainWindow
# from check_pos import CheckMousePos
from scene_one import Scene1
# from sprites import SpriteTower


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
        # self.click_event = CheckMousePos()

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
                #     self.click_event.mouse_coordinates(pygame.mouse.get_pos())

            pygame.display.update()
            self.FPS.tick(60)


if __name__ == "__main__":
    APP = MainLoop()
    APP.run()
