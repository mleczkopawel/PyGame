import random

import pygame

from clases.Action import Action
from clases.BadThing import BadThing
from clases.Car import Car
from clases.Colors import Colors
from clases.GoodThing import GoodThing
from clases.Others import Others
from clases.Positions import Positions
from clases.Things import Things

pygame.init()

crash_sound = pygame.mixer.Sound('sounds/Crash2.wav')
loop_sound = pygame.mixer.Sound('sounds/play2.wav')

colors = Colors()
positions = Positions(800, 800)
positions.set_car_width(73)
others = Others()
action = Action(0)

gameDisplay = pygame.display.set_mode((positions.get_game_width(), positions.get_game_height()))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

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


def make_road():
    l_t_c_l.make_thing(gameDisplay)
    l_t_c_r.make_thing(gameDisplay)
    l_t_l_w.make_thing(gameDisplay)
    l_t_r_w.make_thing(gameDisplay)
    l_t_l_g.make_thing(gameDisplay)
    l_t_r_g.make_thing(gameDisplay)


def button(text, start_x, start_y, width, height, color, color_dark, actionn=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if start_x + width > mouse[0] > start_x and start_y + height > mouse[1] > start_y:
        pygame.draw.rect(gameDisplay, color, (start_x, start_y, width, height))
        if click[0] == 1 and actionn is not None:
            if actionn == 1:
                game_loop()
            else:
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(gameDisplay, color_dark, (start_x, start_y, width, height))

    smallText = pygame.font.Font('fonts/arial.ttf', 20)
    textSurf, textRect = others.text_objects(text, smallText, colors.get_black())
    textRect.center = ((start_x + (width / 2)), (start_y + (height / 2)))
    gameDisplay.blit(textSurf, textRect)


def game_intro():
    pygame.mixer.Sound.play(loop_sound)
    file = open('scores.txt', 'r')
    score = file.readline()
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(colors.get_gray())
        make_road()
        largeText1 = pygame.font.Font('fonts/arial.ttf', 50)
        TextSurf1, TextRect1 = others.text_objects('Last score: ' + score, largeText1, colors.get_black())
        TextRect1.center = (positions.get_game_width() / 2, 50)
        gameDisplay.blit(TextSurf1, TextRect1)

        largeText = pygame.font.Font('fonts/arial.ttf', 115)
        TextSurf, TextRect = others.text_objects('A bit Racey', largeText, colors.get_black())
        TextRect.center = (positions.get_game_width() / 2, positions.get_game_height() / 2)
        gameDisplay.blit(TextSurf, TextRect)

        button('START', 150, 2 * positions.get_game_height() / 3, 100, 50, colors.get_green(), colors.get_dark_green(),
               1)
        button('EXIT', 550, 2 * positions.get_game_height() / 3, 100, 50, colors.get_red(), colors.get_dark_red(), 0)

        pygame.display.update()
        clock.tick(15)


def crash(bt, bsc, blw, bsbt):
    pygame.mixer.Sound.stop(loop_sound)
    pygame.mixer.Sound.play(crash_sound)
    action.crash(gameDisplay, positions, others, colors, bt, bsc, blw, bsbt)
    game_intro()


def game_loop():
    car = Car('images/SimpleDarkBlueCarTopView.png', 50)
    positions.set_car_position(positions.get_game_width() * 0.45, positions.get_game_height() - 110)
    bad_thing = BadThing(random.randrange(60, positions.get_game_width() - 160), -600, 50, 50, colors.get_black(), 7)
    bonus_slower_car = GoodThing(random.randrange(60, positions.get_game_width() - 160), -600, 100, 100,
                                 colors.get_green(),
                                 15, 0)
    bonus_less_width = GoodThing(random.randrange(60, positions.get_game_width() - 160), -600, 100, 100,
                                 colors.get_blue(), 15,
                                 1)
    bonus_slower_bad_thing = GoodThing(random.randrange(60, positions.get_game_width() - 160), -600, 100, 100,
                                       colors.get_gold(), 15, 2)
    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    positions.set_car_position_x(positions.get_car_position_x() + car.move_left())
                elif event.key == pygame.K_RIGHT:
                    positions.set_car_position_x(positions.get_car_position_x() + car.move_right())
                elif event.key == pygame.K_SPACE:
                    action.pause(gameDisplay, positions, colors, clock, others)
                elif event.key == pygame.K_s:
                    pygame.mixer.Sound.stop(loop_sound)
                elif event.key == pygame.K_d:
                    pygame.mixer.Sound.play(loop_sound)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    positions.set_car_position_x(positions.get_car_position_x())

        gameDisplay.fill(colors.get_gray())
        make_road()

        bonus_slower_bad_thing.make_text('Slower bad black box: ', gameDisplay, (positions.get_game_width() - 300, 5))
        if bad_thing.get_dodged() % 11 == 0 and bad_thing.get_dodged() != 0:
            bonus_slower_bad_thing.make_thing(gameDisplay, colors.get_gold(), 1)
            bonus_slower_bad_thing.increase_y()

        bonus_slower_car.make_text('Slower car bonus: ', gameDisplay, (positions.get_game_width() - 300, 25))
        if bad_thing.get_dodged() % 5 == 0 and bad_thing.get_dodged() != 0:
            bonus_slower_car.make_thing(gameDisplay, colors.get_green(), 1)
            bonus_slower_car.increase_y()

        bonus_less_width.make_text('Less width: ', gameDisplay, (positions.get_game_width() - 300, 45))
        if bad_thing.get_dodged() % 7 == 0 and bad_thing.get_dodged() != 0:
            bonus_less_width.make_thing(gameDisplay, colors.get_blue(), 1)
            bonus_less_width.increase_y()

        car.show_car(gameDisplay, positions.get_car_position())
        bad_thing.things_dodged(colors, gameDisplay)

        bad_thing.make_thing(gameDisplay)
        bad_thing.increase_y()

        if (
                    positions.get_car_position_x() > positions.get_game_width() - positions.get_car_width()) or positions.get_car_position_x() < 0:
            crash(bad_thing, bonus_slower_car, bonus_less_width, bonus_slower_bad_thing)

        if bad_thing.get_position_y() > positions.get_game_height():
            bad_thing.increase_speed(0.5)
            bad_thing.increase_width(1.2)
            bad_thing.set_position_y(0 - bad_thing.get_height())
            bad_thing.set_position_x(random.randrange(60, positions.get_game_width() - 160))
            bad_thing.increase_dodged()

            bonus_slower_car.set_position_y(0 - bonus_slower_car.get_height())
            bonus_slower_car.set_position_x(random.randrange(60, positions.get_game_width() - 160))

            bonus_less_width.set_position_y(0 - bonus_less_width.get_height())
            bonus_less_width.set_position_x(random.randrange(60, positions.get_game_width() - 160))

            bonus_slower_bad_thing.set_position_y(0 - bonus_slower_bad_thing.get_height())
            bonus_slower_bad_thing.set_position_x(random.randrange(60, positions.get_game_width() - 160))

            car.increase_speed(5)

        if positions.get_car_position_y() < bad_thing.get_position_y() + bad_thing.get_height():
            if bad_thing.get_position_x() < positions.get_car_position_x() < bad_thing.get_position_x() + bad_thing.get_width() or bad_thing.get_position_x() < positions.get_car_position_x() + positions.get_car_width() < bad_thing.get_position_x() + bad_thing.get_width():
                bad_thing.make_thing(gameDisplay, colors.get_dark_red())
                crash(bad_thing, bonus_slower_car, bonus_less_width, bonus_slower_bad_thing)

        if positions.get_car_position_y() < bonus_slower_car.get_position_y() + bonus_slower_car.get_height() and bad_thing.get_dodged():
            if bonus_slower_car.get_position_x() < positions.get_car_position_x() < bonus_slower_car.get_position_x() + bonus_slower_car.get_width() or bonus_slower_car.get_position_x() < positions.get_car_position_x() + positions.get_car_width() < bonus_slower_car.get_position_x() + bonus_slower_car.get_width():
                bonus_slower_car.make_bonus(car)

        if positions.get_car_position_y() < bonus_less_width.get_position_y() + bonus_less_width.get_height() and bad_thing.get_dodged():
            if bonus_less_width.get_position_x() < positions.get_car_position_x() < bonus_less_width.get_position_x() + bonus_less_width.get_width() or bonus_less_width.get_position_x() < positions.get_car_position_x() + positions.get_car_width() < bonus_less_width.get_position_x() + bonus_less_width.get_width():
                bonus_less_width.make_bonus(None, bad_thing)

        if positions.get_car_position_y() < bonus_slower_bad_thing.get_position_y() + bonus_slower_bad_thing.get_height() and bad_thing.get_dodged():
            if bonus_slower_bad_thing.get_position_x() < positions.get_car_position_x() < bonus_slower_bad_thing.get_position_x() + bonus_slower_bad_thing.get_width() or bonus_slower_bad_thing.get_position_x() < positions.get_car_position_x() + positions.get_car_width() < bonus_slower_bad_thing.get_position_x() + bonus_slower_bad_thing.get_width():
                bonus_slower_bad_thing.make_bonus(None, bad_thing)

        pygame.display.update()
        clock.tick(60)


game_intro()
game_loop()
pygame.quit()
quit()
