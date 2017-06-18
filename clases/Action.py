import time

import pygame


class Action:
    _speed = 0
    _colors = None

    def __init__(self, speed):
        self._speed = speed

    def move_left(self):
        return -self._speed

    def move_right(self):
        return self._speed

    @staticmethod
    def pause(game_display, positions, colors, clock, others):
        paused = True
        print('paused')
        while paused:
            largeText = pygame.font.Font('fonts/arial.ttf', 115)
            TextSurf, TextRect = others.text_objects('PAUSED', largeText, colors.get_blue())
            TextRect.center = (positions.get_game_width() / 2, positions.get_game_height() / 2)
            game_display.blit(TextSurf, TextRect)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        paused = False
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            pygame.display.update()
            clock.tick(15)

    @staticmethod
    def crash(game_display, positions, others, colors, bt, bsc, blw, bsbt):
        largeText = pygame.font.Font('fonts/arial.ttf', 115)
        TextSurf, TextRect = others.text_objects('You Crashed', largeText, colors.get_red())
        TextRect.center = (positions.get_game_width() / 2, positions.get_game_height() / 2)
        game_display.blit(TextSurf, TextRect)
        pygame.display.update()
        time.sleep(2)
        game_display.fill(colors.get_white())
        score = bt.get_dodged() * (bsc.get_points() + blw.get_points() + bsbt.get_points())
        largeText = pygame.font.Font('fonts/arial.ttf', 60)
        TextSurf, TextRect = others.text_objects('Yours score:' + str(score), largeText, colors.get_red())
        TextRect.center = (positions.get_game_width() / 2, positions.get_game_height() / 2)
        game_display.blit(TextSurf, TextRect)
        pygame.display.update()
        time.sleep(2)

    def get_speed(self):
        return self._speed

    def set_speed(self, speed):
        self._speed = speed
