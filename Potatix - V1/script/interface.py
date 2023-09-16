import pygame


class Distance(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.distance = 0
        self.deltatime_distance = 0


        self.font = pygame.font.SysFont('Arial Black', 35)
        self.image = self.font.render(f'{self.distance}', True, (255, 0, 0))
        self.rect = self.image.get_rect(center=(360, 680))



    def update_distance(self, dt):
        self.deltatime_distance += 3 * dt
        self.distance = round(self.deltatime_distance)
        self.image = self.font.render(f'{self.distance}', True, (255, 0, 0))

    def update(self, dt):
        self.update_distance(dt)


class Remaining_bullets(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.font = pygame.font.SysFont('Arial Black', 50)
        self.number = 0
        self.image = self.font.render(f'{self.number}', True, (255, 0, 0))
        self.rect = self.image.get_rect(center=(1280, 680))
