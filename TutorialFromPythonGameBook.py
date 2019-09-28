import pygame


class PyGView (object):


    def __init__(self, wight=640, height=400, fps=30):
        """Initialize pygame, window, background, font,..."""
        pygame.init()
        pygame.display.set_caption("Press ESC for quit")
        self.wight = wight
        self.height = height
        self.screen = pygame.display.set_mode((self.wight, self.height), pygame.DOUBLEBUF)
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.playtime = 0.0
        self.font = pygame.font.SysFont('mono', 20, bold=True)

    def paint(self):
        """painting on the surface"""
        #------- try out some pygame draw functions --------
        # pygame.draw.line(Surface, color, start, end, width)
        pygame.draw.line(self.background, (0,255,0), (10,10), (50,100))
        # pygame.draw.rect(Surface, color, Rect, width=0): return Rect
        pygame.draw.rect(self.background, (0,255,0), (50,50,100,25)) # rect: (x1, y1, width, height)
        # pygame.draw.circle(Surface, color, pos, radius, width=0): return Rect
        pygame.draw.circle(self.background, (0,200,0), (200,50), 35)
        # pygame.draw.polygon(Surface, color, pointlist, width=0): return Rect
        pygame.draw.polygon(self.background, (0,180,0), ((250,100),(300,0),(350,50)))
        # pygame.draw.arc(Surface, color, Rect, start_angle, stop_angle, width=1): return Rect
        pygame.draw.arc(self.background, (0,150,0),(400,10,150,100), 0, 3.14) # radiant instead of grad
        # ------------------- blitting a Ball --------------
        myball = Ball() # creating the Ball object
        myball.blit(self.background) # blitting it

    def run(self):
        """main loop"""
        self.paint()
        running_flag = True
        while running_flag:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running_flag = False
                elif event.type == pygame.KEYDOWN:
                    if event.type == pygame.K_ESCAPE:
                        running_flag = False

            milliseconds = self.clock.tick(self.fps)
            self.playtime +=milliseconds / 1000.0
            self.draw_text(f"FPS: {self.clock.get_fps()}     {self.playtime}")

            pygame.display.flip()
            self.screen.blit(self.background, (0, 0))

        pygame.quit()

    def draw_text (self, text):
        """Center text in window"""
        fw, fh = self.font.size(text)
        surface = self.font.render(text, True, (0, 255, 0))
        self.screen.blit(surface, ((self.wight - fw) // 2, (self.height - fh) // 2))

class Ball(object):
    """this is not a native pygame sprite but instead a pygame surface"""
    def __init__(self, radius = 50, color=(0,0,255), x=320, y=240):
        """create a (black) surface and paint a blue ball on it"""
        self.radius = radius
        self.color = color
        self.x = x
        self.y = y
        # create a rectangular surface for the ball 50x50
        self.surface = pygame.Surface((2*self.radius,2*self.radius))
        # pygame.draw.circle(Surface, color, pos, radius, width=0) # from pygame documentation
        pygame.draw.circle(self.surface, color, (radius, radius), radius) # draw blue filled circle on ball surface
        self.surface = self.surface.convert() # for faster blitting.
        # to avoid the black background, make black the transparent color:
        # self.surface.set_colorkey((0,0,0))
        # self.surface = self.surface.convert_alpha() # faster blitting with transparent color

    def blit(self, background):
        """blit the Ball on the background"""
        background.blit(self.surface, ( self.x, self.y))

if __name__ == '__main__':
    PyGView(640, 400).run()