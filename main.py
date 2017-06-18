import pygame
import random
from clases.Colors import Colors
from clases.Car import Car
from clases.Positions import Positions
from clases.Others import Others
from clases.Action import Action

pygame.init()
colors = Colors()
positions = Positions(800, 1000)
positions.set_car_width(73)
others = Others()
action = Action(others)

gameDisplay = pygame.display.set_mode((positions.get_game_width(), positions.get_game_height()))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, colors.get_black())
    gameDisplay.blit(text, (0, 0))

def things(thing_x, thing_y, thing_w, thing_h, color):
    pygame.draw.rect(gameDisplay, color, [thing_x, thing_y, thing_w, thing_h])


def button(text, start_x, start_y, width, height, color, color_dark, action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if start_x + width > mouse[0] > start_x and start_y + height > mouse[1] > start_y:
        pygame.draw.rect(gameDisplay, color, (start_x, start_y, width, height))
        if click[0] == 1 and action != None:
            if action == 1:
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
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(colors.get_white())
        largeText = pygame.font.Font('fonts/arial.ttf', 115)
        TextSurf, TextRect = others.text_objects('A bit Racey', largeText, colors.get_black())
        TextRect.center = ((positions.get_game_width() / 2, positions.get_game_height() / 2))
        gameDisplay.blit(TextSurf, TextRect)


        button('START', 150, 2*positions.get_game_height()/3, 100, 50, colors.get_green(), colors.get_dark_green(), 1)
        button('EXIT', 550, 2*positions.get_game_height()/3, 100, 50, colors.get_red(), colors.get_dark_red(), 0)

        pygame.display.update()
        clock.tick(15)

def crash():
    action.crash(gameDisplay, positions, others, colors)
    game_intro()

def game_loop():
    car = Car('images/SimpleDarkBlueCarTopView.png', 50)
    positions.set_car_position(positions.get_game_width() * 0.45, positions.get_game_height() * 0.88)

    thing_start_x = random.randrange(0, positions.get_game_width())
    thing_start_y = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100

    dodged = 0

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

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    positions.set_car_position_x(positions.get_car_position_x())

        gameDisplay.fill(colors.get_white())

        things(thing_start_x, thing_start_y, thing_width, thing_height, colors.get_black())
        thing_start_y += thing_speed

        car.show_car(gameDisplay, positions.get_car_position())
        things_dodged(dodged)

        if (positions.get_car_position_x() > positions.get_game_width() - positions.get_car_width()) or positions.get_car_position_x() < 0:
            crash()

        if thing_start_y > positions.get_game_height():
            thing_start_y = 0 - thing_height
            thing_start_x = random.randrange(0, positions.get_game_width())
            dodged += 1
            thing_speed += 0.5
            thing_width += (dodged * 1.2)
            car.increase_speed(5)

        if positions.get_car_position_y() < thing_start_y + thing_height:
            if positions.get_car_position_x() > thing_start_x and positions.get_car_position_x() < thing_start_x + thing_width or positions.get_car_position_x() + positions.get_car_width() > thing_start_x and positions.get_car_position_x() + positions.get_car_width() < thing_start_x + thing_width:
                things(thing_start_x, thing_start_y - thing_speed, thing_width, thing_height, colors.get_dark_red())
                crash()

        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()