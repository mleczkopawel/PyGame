import pygame
import time

class Action:

    _speed = 0
    _colors = None

    def __init__(self, speed):
        self._speed = speed

    def move_left(self):
        return -self._speed

    def move_right(self):
        return self._speed

    def pause(self, gameDisplay, positions, colors, clock, others):
        paused = True
        print('paused')
        while paused:
            largeText = pygame.font.Font('fonts/arial.ttf', 115)
            TextSurf, TextRect = others.text_objects('PAUSED', largeText, colors.get_blue())
            TextRect.center = ((positions.get_game_width() / 2, positions.get_game_height() / 2))
            gameDisplay.blit(TextSurf, TextRect)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        paused = False
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            pygame.display.update()
            clock.tick(15)

    def crash(self, gameDisplay, positions, others, colors):
        largeText = pygame.font.Font('fonts/arial.ttf', 115)
        TextSurf, TextRect = others.text_objects('You Crashed', largeText, colors.get_red())
        TextRect.center = ((positions.get_game_width() / 2, positions.get_game_height() / 2))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        time.sleep(2)