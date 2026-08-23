import pygame
import sys

pygame.init()

class Engine:
    def __init__(self, title="Game", fullscreen=(False, (400, 400)), icon=""):
        self.win = None
        self.size = fullscreen[1]
        self.fullscreen = fullscreen
        self.icon = icon
        self.win = pygame.display.set_mode(self.size)
        if self.icon != "": pygame.display.set_icon(pygame.image.load(self.icon))

    def run(self, update_func = lambda: ..., event_func = lambda: ..., exit_func = lambda: ...):
        while True:
            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    exit_func()
                    sys.exit()
                event_func()


            update_func()
            pygame.display.update()