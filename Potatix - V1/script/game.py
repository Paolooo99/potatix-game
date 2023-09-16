import pygame

from player import *
from interface import *
from buttons import *
from constants import *
from ennemies import *
from timer import *


class Game:
    def __init__(self):
        # draw surface
        self.display_surface = pygame.display.get_surface()

        # welcome screen setup
        self.welcome_screen = True
        self.welcome_background = pygame.image.load('../images/intro_back.png').convert_alpha()
        self.welcome_background = pygame.transform.scale(self.welcome_background,
                                                         (screen_width, screen_height))

        self.setup()

    def setup(self):
        # game backgrounds setup
        self.general_background = pygame.image.load('../images/general_background_lvl1.png').convert_alpha()
        self.general_background = pygame.transform.scale(self.general_background,
                                                         (screen_width, screen_height))

        self.game_backgrounds = []
        for a in range(2):
            self.game_backgrounds.append([pygame.image.load('../images/game_background_lvl1.png').convert_alpha()])
            self.game_backgrounds[a][0] = pygame.transform.scale(self.game_backgrounds[a][0],
                                                                 (screen_width, 531))
            self.game_backgrounds[a].append(self.game_backgrounds[a][0].get_rect(topleft = (a * 1345, 116)))
            self.game_backgrounds[a].append(int(a * 1345))


        # sprites setup
        self.welcome_button = Welcome_button()

        self.player = Player()
        self.rule = Rule()
        self.table = Table(random.choice(table_y_pos))
        self.table_count = 0
        self.random_table_list = []
        self.distance = Distance()
        self.remaining_bullets = Remaining_bullets()

        self.welcome_screen_group = pygame.sprite.Group()
        self.welcome_screen_group.add(self.welcome_button)

        self.player_group = pygame.sprite.GroupSingle()
        self.player_group.add(self.player)

        self.global_group = pygame.sprite.Group()
        self.global_group.add(self.distance)
        self.global_group.add(self.remaining_bullets)

        self.rules_group = pygame.sprite.Group()
        self.tables_group = pygame.sprite.Group()

        # timers
        self.rules_timer = Timer(500, function=self.spawn_rules)
        self.table_timer = Timer(2000, function=self.spawn_tables)
        self.potato_end_delay = Timer(700, function=self.player.jump)


    def spawn_rules(self):
        self.rule = Rule()
        self.rules_group.add(self.rule)

    def spawn_tables(self):
        random_choice = random.choice(table_y_pos)
        self.random_table_list.append(random_choice)
        self.table = Table(random_choice)
        self.tables_group.add(self.table)

        table_y_pos.remove(random_choice)

        self.table_count += 1
        if self.table_count == 1:
            self.spawn_tables()
        else:
            self.table_count = 0
            table_y_pos.append(self.random_table_list[0])
            table_y_pos.append(self.random_table_list[1])
            self.random_table_list = []

    def back_moving(self,dt):
        if self.game_backgrounds[0][2] > -1345:
            self.game_backgrounds[0][2] -= 420 * dt
        else:
            self.game_backgrounds[0][2] = 1340
        if self.game_backgrounds[1][2] > -1345:
            self.game_backgrounds[1][2] -= 420 * dt
        else:
            self.game_backgrounds[1][2] = 1340

        self.game_backgrounds[0][1].x = round(self.game_backgrounds[0][2])
        self.game_backgrounds[1][1].x = round(self.game_backgrounds[1][2])

    def run(self,dt):
        if self.welcome_screen:

            self.display_surface.blit(self.welcome_background, (0, 0))

            self.welcome_screen_group.draw(self.display_surface)
            self.welcome_screen_group.update()

            if self.welcome_button.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed() == (1,0,0):
                self.welcome_screen = False
                self.setup()

        else:
            if not self.player.potato_falling and not self.potato_end_delay.active:
                self.back_moving(dt)
                if not self.rules_timer.active:
                    self.rules_timer.activate()
                self.rules_timer.update()

                if not self.table_timer.active:
                    self.table_timer.activate()
                self.table_timer.update()

                self.player_group.update(dt)


            self.display_surface.blit(self.general_background, (0, 0))
            self.display_surface.blit(self.game_backgrounds[0][0], (0,116))
            self.display_surface.blit(self.game_backgrounds[0][0], self.game_backgrounds[0][1])
            self.display_surface.blit(self.game_backgrounds[1][0], self.game_backgrounds[1][1])

            self.player_group.draw(self.display_surface)

            self.global_group.draw(self.display_surface)
            self.global_group.update(dt)

            self.tables_group.draw(self.display_surface)
            self.tables_group.update(dt)

            self.rules_group.draw(self.display_surface)
            self.rules_group.update(dt)


            rules_collisions = pygame.sprite.spritecollide(self.player, self.rules_group, False)
            tables_collisions = pygame.sprite.spritecollide(self.player, self.tables_group, False)

            if rules_collisions or tables_collisions:
                self.tables_group.empty()
                self.rules_group.empty()
                self.global_group.empty()
                self.rules_timer.deactivate()
                self.table_timer.deactivate()
                if not self.potato_end_delay.active:
                    self.potato_end_delay.activate()


            self.potato_end_delay.update()

            if self.player.potato_falling:
                self.player.falling(dt)
                self.player.rotate(dt)

            if self.player.fall_ended:
                self.welcome_screen = True
                self.global_group.empty()
