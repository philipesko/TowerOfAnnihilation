import pygame, os.path
pygame.init()

# Size of a window in px
size = width, height = 1024, 768
surface = pygame.display.set_mode(size)

# Loading and formatting windows icon to 32x32
icon = pygame.image.load(os.path.join('resources', 'tower-defense-levels-ship.png'))
icon = pygame.transform.scale(icon, (32, 32))

# Loading background for main menu, was scaled previously, but may be scaled in case of size changing
main_menu_background = pygame.image.load(os.path.join('resources', 'main.png'))
# main_menu_background = pygame.transform.scale(main_menu_background, size)

# Load font and position the text
main_menu_greets = pygame.font.Font(os.path.join('resources', 'font_forever.ttf'), 28)
main_menu_greets = main_menu_greets.render('Welcome to the Tower of Annihilation', 1, (207,204,127))
text_pos = main_menu_greets.get_rect()
text_pos.center = main_menu_background.get_rect().center

# Setting a window caption and an icon
pygame.display.set_caption('Tower of Annihilation')
pygame.display.set_icon(icon)

# Main loop
while True:
    for event in pygame.event.get():
        # print(event)
        surface.blit(main_menu_background, (0, 0))
        surface.blit(main_menu_greets, text_pos)
    if event.type == pygame.QUIT: 
        break
    pygame.display.update()
    




pygame.quit()
quit()