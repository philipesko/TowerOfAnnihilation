import pygame

import TOA.MainWindow as MW


class MainLoop:

    def __init__(self):
        self._running = True
        self.FPS = pygame.time.Clock()
    def on_cleanup(self):
        #Clear all. Need use before exit from game
        pygame.quit()

    def run(self):
        """"Main loop"""
        while self._running:

            pygame.init()
            #Create new Main Window
            create_main_window = MW.CreateMainWindow()
            cmw = create_main_window.create()

            for event in pygame.event.get():
                """"Quit from game if player push button ESC"""
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    self._running = False
                    self.on_cleanup()

                self.FPS.tick(60)
                pygame.display.update()



if __name__ == "__main__":
    APP = MainLoop()
    APP.run()



