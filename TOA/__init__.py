import pygame

import TOA.MainWindow as MW


class MainLoop:

    def __init__(self):
        self._running = True

    def on_cleanup(self):
        #Clear all. Need use before exit from game
        pygame.quit()

    def run(self):
        """"Main loop"""
        while self._running:

            pygame.init()
            create_main_window = MW.CreateMainWindows()
            create_main_window.create()
            for event in pygame.event.get():
                """"Quit from game if player push button ESC"""
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    self._running = False
                    self.on_cleanup()

                pygame.display.update()


if __name__ == "__main__":
    APP = MainLoop()
    APP.run()



