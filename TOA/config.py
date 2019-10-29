import pygame
import os.path
"""Configuration file"""

# config for project
MAIN_SIZE_FOR_WINDOW = 1024, 768
CELL_SIZE = 58, 58
SURFACE = pygame.display.set_mode(MAIN_SIZE_FOR_WINDOW)
PATH_TO_RESOURCE = os.path.join(os.path.dirname(__file__), 'resources')
NAME_PROJECT = 'Tower of Annihilation'
BUTTON_NAME_FOR_MAIN_MENU = ['start.png', 'exit.png', 'start_pressed.png', 'exit_pressed.png', 'start_light.png',
                             'exit_light.png']
# config for button
MAIN_MENU_BUTTON = {'button_start': {'title': 'Start', 'y': 0.45, 'image': 'start.png'},
                    'button_exit': {'title': 'Exit', 'y': 0.55, 'image': 'exit.png'}}
GRID = {}