import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('../images/player_1.png').convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (80, 80))
        self.rect = self.image.get_rect(center=(64, 167))

        self.images_list = []
        for a in range(0, 5):
            self.images_list.append(pygame.image.load(f'../images/player_{a + 1}.png').convert_alpha())
            self.images_list[a] = pygame.transform.smoothscale(self.images_list[a], (80, 80))
        self.frame = 0

        self.last_y_pos = self.rect.y
        self.position = pygame.math.Vector2(self.rect.center)
        self.game_jump_speed = 27
        self.key_pressed = False
        self.is_moving = ''

        self.gravity = 0
        self.vertical_velocity = 0
        self.horizontal_boost = 0
        self.fall_ended = False
        self.potato_falling = False

        self.starting_image = self.image
        self.angle = 0
        self.size_percentage = 100

    def movements(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if not self.key_pressed and self.is_moving == '':
                if self.rect.y >= 220:
                    self.key_pressed = True
                    self.last_y_pos = self.rect.y
                    self.is_moving = '+'
        elif keys[pygame.K_DOWN]:
            if not self.key_pressed and self.is_moving == '':
                if self.rect.y <= 510:
                    self.key_pressed = True
                    self.last_y_pos = self.rect.y
                    self.is_moving = '-'
        else:
            self.key_pressed = False

        if self.is_moving == '+':
            self.rect.y -= self.game_jump_speed
            if self.last_y_pos - 106 > self.rect.y:
                self.is_moving = ''
        elif self.is_moving == '-':
            self.rect.y += self.game_jump_speed
            if self.last_y_pos + 106 < self.rect.y:
                self.is_moving = ''
        self.position = pygame.math.Vector2(self.rect.center)

    def animate(self, dt):
        self.image = self.images_list[int(self.frame)]
        self.frame += 11.5 * dt
        if self.frame >= 5:
            self.frame = 0

    def jump(self):
        if not self.potato_falling:
            self.vertical_velocity = -4
            self.horizontal_boost = self.rect.x
            self.potato_falling = True

    def falling(self, dt):
        self.gravity = 15 * dt
        self.vertical_velocity += self.gravity
        self.horizontal_boost += 360 * dt
        self.rect.y += round(self.vertical_velocity)
        self.rect.x = round(self.horizontal_boost)
        self.position = pygame.math.Vector2(self.rect.center)
        if self.rect.y > 1000:
            self.fall_ended = True
            self.potato_falling = False

    def rotate(self, dt):
        self.image = pygame.transform.rotate(self.starting_image, self.angle)
        self.image = pygame.transform.smoothscale(self.image, (
        self.size_percentage / 100 * self.image.get_width(), self.size_percentage / 100 * self.image.get_height()))
        self.rect = self.image.get_rect(center=self.position)
        self.angle += 1000 * dt
        if self.size_percentage > 0:
            self.size_percentage -= 30 * dt

    def update(self, dt):
        self.movements(dt)
        self.animate(dt)
