import pygame
from clases.Things import Things


class BadThing(Things):
    _dodged = 0

    def __init__(self, x, y, w, h, c, s):
        super().__init__(x, y, w, h, c, s)

    def things_dodged(self, colors, game_display):
        font = pygame.font.SysFont(None, 25)
        text = font.render("Dodged: " + str(self._dodged), True, colors.get_black())
        game_display.blit(text, (0, 0))

    def increase_width(self, increase):
        self.w += self._dodged * increase

    def increase_dodged(self):
        self._dodged += 1

    def get_dodged(self):
        return self._dodged
