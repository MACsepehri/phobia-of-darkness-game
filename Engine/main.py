import pygame
import sys
from Engine.Assets.UI import *
import time as _time

pygame.init()

BED_RECT = pygame.Rect(pygame.display.Info().current_w - 428, pygame.display.Info().current_h - 355, 540, 212)

def check_collision(rect1, rect2):
    if rect1.colliderect(rect2):
        return True
    else:
        return False


class Player:
    def __init__(self, main, speed=5):
        self.main = main
        self.speed = speed
        self.moveing = False

        self.image = self.main.transform_image(
            self.main.load_image("Assets/Image/Player/state1.png"),
            (90, 220)
        )

        self.rect = self.image.get_rect()

        self.x = 0
        self.y = main.win.height - self.rect.height

        # هماهنگ کردن موقعیت اولیه
        self.rect.x = self.x
        self.rect.y = self.y

    def set_position(self, x, y):
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
        self.update()

    def set_in_window(self):
        if self.x <= 0:
            self.x = 0
        elif self.x >= self.main.win.width - self.rect.width:
            self.x = self.main.win.width - self.rect.width

        if self.y <= 0:
            self.y = 0
        elif self.y >= self.main.win.height - self.rect.height:
            self.y = self.main.win.height - self.rect.height

    def set_status(self):
        if self.moveing:
            self.image = self.main.transform_image(
                self.main.load_image("Assets/Image/Player/state2.png"),
                (90, 220)
            )
        else:
            self.image = self.main.transform_image(
                self.main.load_image("Assets/Image/Player/state1.png"),
                (90, 220)
            )

        self.rect = self.image.get_rect()
        # بعد از تغییر تصویر، دوباره rect را با مختصات فعلی هماهنگ کن
        self.rect.x = self.x
        self.rect.y = self.y

    def move(self):
        keys = pygame.key.get_pressed()

        self.moveing = False

        if keys[pygame.K_a]:
            self.x -= self.speed
            self.moveing = True

        if keys[pygame.K_d]:
            self.x += self.speed
            self.moveing = True

        if keys[pygame.K_w]:
            self.y -= self.speed
            self.moveing = True

        if keys[pygame.K_s]:
            self.y += self.speed
            self.moveing = True

        self.set_status()
        self.set_in_window()

    def update(self):
        self.move()
        # هماهنگ سازی نهایی rect با x و y
        self.rect.x = self.x
        self.rect.y = self.y
        self.main.render_image(self.image, (self.x, self.y))

class Engine:
    def __init__(self, title="Game", fullscreen=(False, (400, 400)), icon="", fps=120):
        self.win = None
        self.size = fullscreen[1]
        self.fullscreen = fullscreen
        self.icon = icon
        self.win = pygame.display.set_mode(self.size)
        self.fps = fps
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(title)
        if self.icon != "": pygame.display.set_icon(pygame.image.load(self.icon))

    def set_color(self, color): self.win.fill(color)

    def transform_image(self, image, new_size=(0,0)): return pygame.transform.scale(image, new_size)

    def load_image(self, path): return pygame.image.load(path)

    def button(self, x, y, width, height, text = "", font = "", text_color = (255, 255, 255), button_color = (0, 0, 0), hover_color = (21, 21, 21), image = "", r = 15): return Button(x, y, width, height, text, font, text_color, button_color, hover_color, image, r)

    def load_font(self, path, size): return pygame.font.Font(path, size)

    def render_image(self, img, pos): self.win.blit(img, pos)

    def full_window_size(self): return (pygame.display.Info().current_w, pygame.display.Info().current_h)

    def draw_text(self, text, color, x, y, font, middle=False):
        if not middle: self.win.blit(font.render(text, True, color), (x, y))
        else:
            res = font.render(text, True, color)
            x = self.win.width / 2 - res.get_width() / 2
            y = self.win.height / 2 - res.get_height() / 2
            self.win.blit(res, (x, y))

    def load_music(self, path): return pygame.mixer.Sound(path)

    def delay(self, milliseconds): pygame.time.delay(milliseconds)

    def time(self): return _time.time()

    def is_clicked(self, key): return pygame.key.get_pressed()[key]

    def run(self, update_func = lambda: ..., event_func = lambda: ..., exit_func = lambda: ...):
        while True:
            self.clock.tick(self.fps)
            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    exit_func()
                    sys.exit()
                event_func()


            update_func()
            pygame.display.update()

def get_pg(): return pygame