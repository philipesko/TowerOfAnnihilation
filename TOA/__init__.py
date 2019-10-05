import pygame

from MainWindow import CreateMainWindow


class MainLoop:

    def __init__(self):
        self._running = True
        self.FPS = pygame.time.Clock()
        # Known bug - high CPU usage
        pygame.mixer.quit()
        

    def on_cleanup(self):
        #Clear all. Need use before exit from game
        pygame.quit()
        quit()


    def run(self):
        """Main loop"""
        while self._running:

            pygame.init()
            #Create new Main Window
            # create_main_window = MW.CreateMainWindow().create()
            CMW = CreateMainWindow()
            create_main_window = CMW.create()
            if CMW._isrunning == False:
                self._running = False
            
            for event in pygame.event.get():
                # print(event)
                """Quit from game if player pushes button ESC"""
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    self._running = False
                    self.on_cleanup()
                    
  
                # self.FPS.tick(60)

            pygame.display.update()
            


if __name__ == "__main__":
    APP = MainLoop()
    APP.run()



