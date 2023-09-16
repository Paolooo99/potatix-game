import pygame, sys, time
from constants import *
from game import Game
from debug import debug_text


class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(screen_resolution)
        pygame.display.set_caption('Objectif: monnaie')
        self.game = Game()
        self.clock = pygame.time.Clock()
        self.previous_time = time.time()
        self.FPS = 0

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            dt = time.time() - self.previous_time
            self.previous_time = time.time()

            """Toi, codeur, tu veux par exemple 7 pixels de mouvement par image. Ainsi chaque boucle principale, ton personnage avancera
            7 fois. Or, tu as une cadence de boucle de 60 images par secondes. Donc tu va faire 7 * 60 = 420 pixels par secondes
            mais toi tu veux trouver un nombre pour lequel peu importe le nombre d'images par seconde (7 * 30 != 7 * 60) il y a 
            le même nombre de pixels par secondes. Pour cela, tu cherche le nombre de millisecondes (converties en secondes)
            qu'une image prend. Tu multiplie le nombre de pixels par secondes par celui de la longueur d'une image. Et la boucle
            te le répètera 60 fois. Ainsi, 420 * 1/60 (le temps pour une frame = 1 /60 ou 'dt' comme plus haut) sera fait 60 fois.
            A conceptualiser comme 420 * 1/60 = 420/60 donc (420 * 60)/ 60 = 420 et ceux pour toutes les performances d'ordinateur"""

            self.game.run(dt)

            if dt != 0:
                self.FPS = round((1 / dt) * (10 ** -1)) / 10 ** -1
            debug_text(f'{self.FPS} FPS')

            if pygame.mouse.get_pressed() == (0, 0, 1):
                print(pygame.mouse.get_pos())

            pygame.display.flip()


if __name__ == '__main__':
    main = Main()
    main.run()
