import pygame

pygame.init()
font = pygame.font.SysFont('Arial black', 25)


def debug_text(text, x=10, y=10):
    display_surface = pygame.display.get_surface()
    surface = font.render(str(text), True, (0, 0, 0))
    surface_rect = surface.get_rect(topleft=(x, y))
    display_surface.blit(surface, surface_rect)
