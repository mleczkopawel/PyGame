import pygame
from clases.Things import Things

class GoodThing(Things):

    _bonus_type = 0
    _count_b0 = 0
    _count_b1 = 0
    _count_b2 = 0

    def __init__(self, x, y, w, h, c, s, b):
        super().__init__(x, y, w, h, c, s)
        self._bonus_type = b

    def make_bonus(self, gameDisplay, screen_width, car = None, bad_thing = None):
        if self._bonus_type == 0:
            car.set_speed(50)
            self._count_b0 += 1
        elif self._bonus_type == 1:
            bad_thing.set_width(100)
            self._count_b1 += 1
        elif self._bonus_type == 2:
            bad_thing.set_speed(7)
            self._count_b2 += 1


    def make_text(self, text_param, gameDisplay, position):
        font = pygame.font.SysFont(None, 25)
        if self._bonus_type == 0:
            text = font.render(text_param + str(self._count_b0), True, self.c)
        elif self._bonus_type == 1:
            text = font.render(text_param + str(self._count_b1), True, self.c)
        elif self._bonus_type == 2:
            text = font.render(text_param + str(self._count_b2), True, self.c)
        gameDisplay.blit(text, position)

    def get_points(self):
        if self._bonus_type == 0:
            return self._count_b0
        elif self._bonus_type == 1:
            return self._count_b1
        elif self._bonus_type == 2:
            return self._count_b2