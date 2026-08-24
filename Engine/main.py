import pygame
import sys
from Engine.Assets.UI import *
import time as _time
import random as _random

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
        self.moving = False
        self.right = True
        self.can_move = True
        self.is_dead = False  # اضافه شد
        self.dead_image = None  # اضافه شد

        img_s1 = self.main.load_image("Assets/Image/Player/state1.png")
        img_s2 = self.main.load_image("Assets/Image/Player/state2.png")
        
        self.img_idle_right = self.main.transform_image(img_s1, (90, 220))
        self.img_idle_left = pygame.transform.flip(self.img_idle_right, True, False)

        self.img_walk_right = self.main.transform_image(img_s2, (90, 220))
        self.img_walk_left = pygame.transform.flip(self.img_walk_right, True, False)

        self.image = self.img_idle_right
        self.rect = self.image.get_rect()

        self.x = 0
        self.y = main.win.height - self.rect.height
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
        if self.is_dead and self.dead_image:
            self.image = self.dead_image
            self.rect = self.image.get_rect()
            self.rect.x = self.x
            self.rect.y = self.y
            return
            
        if self.moving:
            self.image = self.img_walk_right if self.right else self.img_walk_left
        else:
            self.image = self.img_idle_right if self.right else self.img_idle_left

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def move(self):
        if self.is_dead:
            return
            
        keys = pygame.key.get_pressed()
        self.moving = False
        if self.can_move:
            if keys[pygame.K_a]:
                self.x -= self.speed
                self.moving = True
                self.right = False

            if keys[pygame.K_d]:
                self.x += self.speed
                self.moving = True
                self.right = True

            if keys[pygame.K_w]:
                self.y -= self.speed
                self.moving = True

            if keys[pygame.K_s]:
                self.y += self.speed
                self.moving = True

        self.set_in_window()
        self.set_status()

    def kill(self):
        self.is_dead = True
        self.dead_image = self.main.transform_image(self.main.load_image("Assets/Image/Player/Dead/player-body-parts.png"), (450, 250))
        self.image = self.dead_image
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.can_move = False
        self.moving = False

    def update(self):
        self.move()
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

    def randint(self, a, b): return _random.randint(a, b)

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