import pygame
import sys
from Engine.Assets.UI import *

pygame.init()

class Engine:
    def __init__(self, title="Game", fullscreen=(False, (400, 400)), icon=""):
        self.win = None
        self.size = fullscreen[1]
        self.fullscreen = fullscreen
        self.icon = icon
        self.win = pygame.display.set_mode(self.size)
        pygame.display.set_caption(title)
        if self.icon != "": pygame.display.set_icon(pygame.image.load(self.icon))

    def set_color(self, color): self.win.fill(color)

    def transform_image(self, image, new_size=(0,0)): return pygame.transform.scale(image, new_size)

    def load_image(self, path): return pygame.image.load(path)

    def button(self, x, y, width, height, text = "", font = "", text_color = (255, 255, 255), button_color = (0, 0, 0), hover_color = (21, 21, 21), image = "", r = 15): return Button(x, y, width, height, text, font, text_color, button_color, hover_color, image, r)

    def load_font(self, path, size): return pygame.font.Font(path, size)

    def render_image(self, img, pos): self.win.blit(img, pos)

    def run(self, update_func = lambda: ..., event_func = lambda: ..., exit_func = lambda: ...):
        while True:
            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    exit_func()
                    sys.exit()
                event_func()


            update_func()
            pygame.display.update()