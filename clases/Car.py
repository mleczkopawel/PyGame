import pygame
from clases.Action import Action


class Car(Action):

    _car_img = None

    def __init__(self, img_name, start_speed):
        super().__init__(start_speed)
        self._img_name = img_name
        self._start_speed = start_speed
        self._car_img = pygame.image.load(self._img_name)

    def set_img_name(self, img_name):
        self._img_name = img_name

    def get_img_name(self):
        return self._img_name

    def set_start_speed(self, start_speed):
        self._start_speed = start_speed

    def get_start_speed(self):
        return self._start_speed

    def increase_speed(self, increase):
        self._speed += increase

    def show_car(self, game_display, x):
        game_display.blit(self._car_img, x)
