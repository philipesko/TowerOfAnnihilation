import pygame

import MainWindow 
from CheckPos import CheckMousePos

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
            CMW = MainWindow.CreateMainWindow()
            create_main_window = CMW.create()
            click_event = CheckMousePos()

            if CMW._isrunning == False:
                self._running = False
            
            for event in pygame.event.get():
                """Quit from game if player pushes button ESC"""
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    self._running = False
                    self.on_cleanup()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    coord = pygame.mouse.get_pos()
                    # print(coord)
                    click_event.mouse_coordinates(coord)
  
                # self.FPS.tick(60)

            pygame.display.update()
            


if __name__ == "__main__":
    APP = MainLoop()
    APP.run()



