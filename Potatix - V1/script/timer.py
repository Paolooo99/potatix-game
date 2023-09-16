import pygame


class Timer:
    def __init__(self, duration, function=None, function2=None):
        self.duration = duration
        self.start_time = 0
        self.function = function
        self.function2 = function2
        self.active = False

    def activate(self):
        self.active = True
        self.start_time = pygame.time.get_ticks()

    def deactivate(self):
        self.active = False
        self.start_time = 0

    def update(self):
        current_time = pygame.time.get_ticks()
        if self.active:
            if current_time - self.start_time >= self.duration:
                if self.function is not None:
                    self.function()
                if self.function2 is not None:
                    self.function2()

                self.deactivate()
