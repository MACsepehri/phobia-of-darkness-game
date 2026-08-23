import pygame

pygame.init()

class Button:
    def __init__(self, x, y, width, height, text="", font="", text_color=(255,255,255), button_color=(0,0,0), hover_color=(21,21,21), image="", r=15):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        if isinstance(font, str):
            self.font = pygame.font.SysFont(None, 32)
        else:
            self.font = font
        self.text_color = text_color
        self.button_color = button_color
        self.hover_color = hover_color
        self.clicked = False
        self.visible = True
        if image != "":
            self.image = image
        else:
            self.image = None

        self.border_radius = r

    def draw(self, screen):
        if not self.visible:
            return
        
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_x, mouse_y):
            pygame.draw.rect(screen, self.hover_color, self.rect, border_radius=self.border_radius)
        else:
            pygame.draw.rect(screen, self.button_color, self.rect, border_radius=self.border_radius)

        if self.image is not None:
            text_surface = self.image
        else:
            text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self):
        if not self.visible:
            return
        
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()[0]

        if self.rect.collidepoint(mouse_x, mouse_y) and mouse_click:
            if not self.clicked:
                self.clicked = True
                return True
        else:
            self.clicked = False
        return False
    
    def hide(self):
        self.visible = False

    def show(self):
        self.visible = True