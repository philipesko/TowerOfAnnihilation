import pygame


from main_window import CreateMainWindow
from check_pos import CheckMousePos
from scene_one import Scene1


class MainLoop:

    def __init__(self):
        self._running = True
        self.FPS = pygame.time.Clock()
        self._switch_scene = False
        # Initializing - no need to init() in main loop
        pygame.init()
        # Known bug - high CPU usage
        pygame.mixer.quit()
        self.CMW = CreateMainWindow()
        self.scene_one_call = Scene1()



    def on_cleanup(self):
        #Clear all. Need use before exit from game
        pygame.quit()
        quit()


    def run(self):
        """Main loop"""
        while self._running:

            # switch between windows if flag _switch_scene is true:
            if self._switch_scene:
                create_scene_one_call = self.scene_one_call.create()
            else:
                create_main_window = self.CMW.create()

                if not self.CMW.isrunning:
                    self._running = False

            # Tracking mouse events
            click_event = CheckMousePos()


            for event in pygame.event.get():
                """Quit from game if player pushes button ESC"""
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    self._running = False
                    self.on_cleanup()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                    # set flag for switch windows if key "1" is pushing
                    self._switch_scene = True

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    click_event.mouse_coordinates(pygame.mouse.get_pos())
  
            pygame.display.update()
            self.FPS.tick(60)


if __name__ == "__main__":
    APP = MainLoop()
    APP.run()



