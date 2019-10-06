import pygame, os.path

class CheckMousePos:

    def mouse_coordinates(self, coordinates):

        self.mouse_coordinates = coordinates
        print(coordinates)



# if 427+170 > self.mouse[0] > 427 and 345+56 > self.mouse[1] > 345:
#     self.draw_button(self._button_name[4], 0.45)
#     self.draw_button(self._button_name[1], 0.55)
# elif 427+170 > self.mouse[0] > 427 and 422+56 > self.mouse[1] > 422:
#     self.draw_button(self._button_name[0], 0.45)
#     self.draw_button(self._button_name[5], 0.55)
#     for self.click in pygame.event.get():
#         if self.click.type == pygame.MOUSEBUTTONDOWN and self.click.button == 1:
#             self._isrunning = False