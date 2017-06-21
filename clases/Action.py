import time

import pygame

from clases.Things import Things


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
        l_t_c_l = Things(positions.get_game_width() / 2 - 10, 0, 10, positions.get_game_height(),
                         colors.get_white(), 0)
        l_t_c_r = Things(positions.get_game_width() / 2 + 10, 0, 10, positions.get_game_height(),
                         colors.get_white(), 0)
        l_t_l_w = Things(50, 0, 10, positions.get_game_height(), colors.get_white(), 0)
        l_t_r_w = Things(positions.get_game_width() - 60, 0, 10, positions.get_game_height(),
                         colors.get_white(), 0)
        l_t_l_g = Things(0, 0, 50, positions.get_game_height(), colors.get_darker_green(), 0)
        l_t_r_g = Things(positions.get_game_width() - 50, 0, 50, positions.get_game_height(),
                         colors.get_darker_green(), 0)
        largeText = pygame.font.Font('fonts/arial.ttf', 115)
        TextSurf, TextRect = others.text_objects('You Crashed', largeText, colors.get_red())
        TextRect.center = (positions.get_game_width() / 2, positions.get_game_height() / 2)
        game_display.blit(TextSurf, TextRect)
        pygame.display.update()
        time.sleep(2)
        game_display.fill(colors.get_gray())
        l_t_c_l.make_thing(game_display)
        l_t_c_r.make_thing(game_display)
        l_t_l_w.make_thing(game_display)
        l_t_r_w.make_thing(game_display)
        l_t_l_g.make_thing(game_display)
        l_t_r_g.make_thing(game_display)
        score = bt.get_dodged() * (bsc.get_points() + blw.get_points() + bsbt.get_points())
        file = open('scores.txt', 'w')
        file.write(str(score))
        file.close()
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
