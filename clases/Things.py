import pygame


class Things:
    def __init__(self, x, y, w, h, c, s):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.c = c
        self.s = s

    def set_position_x(self, x):
        self.x = x

    def get_position_x(self):
        return self.x

    def set_position_y(self, y):
        self.y = y

    def get_position_y(self):
        return self.y

    def set_width(self, w):
        self.w = w

    def get_width(self):
        return self.w

    def set_height(self, h):
        self.h = h

    def get_height(self):
        return self.h

    def set_color(self, c):
        self.c = c

    def get_color(self):
        return self.c

    def set_speed(self, s):
        self.s = s

    def get_speed(self):
        return self.s

    def increase_y(self):
        self.y += self.s

    def increase_speed(self, increase):
        self.s += increase

    def make_thing(self, game_display, c=None):
        if c is not None:
            pygame.draw.rect(game_display, c, [self.x, self.y - self.s, self.w, self.h])
        else:
            pygame.draw.rect(game_display, self.c, [self.x, self.y, self.w, self.h])
