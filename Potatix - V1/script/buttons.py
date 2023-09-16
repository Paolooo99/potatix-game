import pygame
from constants import *


class Welcome_button(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('../images/welcome_button.png')

        self.button = self.image
        self.bigger_button = pygame.transform.smoothscale(self.image, (
            self.image.get_width() * 1.25, self.image.get_height() * 1.25))

        self.rect = self.image.get_rect(center=(screen_width / 2 + 50, screen_height / 2 + 50))

    def mouse_hover(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.rect = self.bigger_button.get_rect(center=(screen_width / 2 +50, screen_height / 2+50))
            self.image = self.bigger_button
        else:
            self.rect = self.image.get_rect(center=(screen_width / 2+50, screen_height / 2+50))
            self.image = self.button

    def update(self):
        self.mouse_hover()
