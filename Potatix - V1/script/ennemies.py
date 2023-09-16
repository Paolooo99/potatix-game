import pygame
import random
from constants import *


class Ennemy(pygame.sprite.Sprite):
    def __init__(self, image, hp=100, pos=(0, 0), size=(100, 100)):
        super().__init__()
        self.hp = hp
        self.size = size
        self.image = pygame.image.load('../images/' + str(image) + '.png').convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, self.size)
        self.rect = self.image.get_rect(center=pos)


class Rule(Ennemy):
    def __init__(self):
        self.position = pygame.math.Vector2(1408, random.choice(rule_y_pos))
        super().__init__('Rule', pos=self.position, size=(100, 32))
        self.angle = 0
        self.rotated_image = None
        self.starting_image = self.image

    def move(self, dt):
        if self.position.x <= -162:
            self.kill()
        else:
            self.position.x -= 840 * dt
        self.rect.x = round(self.position.x)

    def rotate(self, dt):
        self.rotated_image = pygame.transform.rotate(self.starting_image, self.angle)
        self.image = self.rotated_image
        self.rect = self.image.get_rect(center=self.position)
        self.angle += 660 * dt

    def update(self, dt):
        self.move(dt)
        self.rotate(dt)


class Table(Ennemy):
    def __init__(self, yposition):
        self.position = pygame.math.Vector2(1428, yposition)
        super().__init__(random.choice(['Table_1', 'Table_2']), pos=self.position, size=(150,100))

    def move(self, dt):
        if self.position.x <= -182:
            self.kill()
        else:
            self.position.x -= 420 * dt
        self.rect.x = round(self.position.x)

    def update(self, dt):
        self.move(dt)

