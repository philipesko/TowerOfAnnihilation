import pygame

from MainWindow import CreateMainWindow
from CheckPos import CheckMousePos

class MainLoop:

    def __init__(self):
        self._running = True
        self.FPS = pygame.time.Clock()
        # Initializing - no need to init() in main loop
        pygame.init()
        # Known bug - high CPU usage
        pygame.mixer.quit()
        # Loading cursor
        pygame.mouse.set_cursor(*pygame.cursors.tri_left)

    def on_cleanup(self):
        #Clear all. Need use before exit from game
        pygame.quit()
        quit()


    def run(self):
        """Main loop"""
        while self._running:

            # Create new Main Window
            CMW = CreateMainWindow()
            create_main_window = CMW.create()
            
            # Tracking mouse events
            click_event = CheckMousePos()

            if CMW._isrunning == False:
                self._running = False
            
            for event in pygame.event.get():
                """Quit from game if player pushes button ESC"""
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    self._running = False
                    self.on_cleanup()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    click_event.mouse_coordinates(pygame.mouse.get_pos())
  


            pygame.display.update()
            self.FPS.tick(60)


if __name__ == "__main__":
    APP = MainLoop()
    APP.run()



