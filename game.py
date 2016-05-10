import random
import pygame
import time

pygame.init()

FPS = 20
# defining colours
green = (0, 155, 0)
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)
# specs of car
car_width = 100
car_height = 180

disp_height = 720
disp_width = 220

gameDisplay = pygame.display.set_mode((disp_width, disp_height))
pygame.display.set_caption("Car Dodge")
# defining player and computer cars
player_car = pygame.image.load('Car_Green_Front.png').convert()  # converting to surface
player_car.set_colorkey(white)
player_car = player_car.convert_alpha()  # making background transparent

computer_car = pygame.image.load('Car_Red_Front.png').convert()  # same as above
computer_car.set_colorkey(white)
computer_car = computer_car.convert_alpha()

clock = pygame.time.Clock()  # clock for the game

font = pygame.font.SysFont(None, 20)  # font of text's


def message_to_screen(msg, color, y=0, x=0):  # function to display text to screen
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [x, y])


def gameloop():  # most important function, , game runs inside this

    player_speed = 20
    computer_speed = 30

    road = pygame.image.load('road.png').convert()
    # road had to be defined inside gameloop since we are flipping it vertically to give effect of road changing
    player_x = disp_width - car_width  # starting x and y coordinates of player car
    player_y = disp_height - car_height

    computer_x = random.choice([0, disp_width - car_width])
    # randomly choosing if computer car starts from left or right lane
    computer_y = -car_height # computer car starts above the display and comes driving inside

    player_x_change = 0

    score = 0
    start = False
    gameExit = False
    gameOver = False  #gameExit to exit the whole game
    left_or_right = 0 #if left key was pressed or right key was pressed

    while not gameExit:

        while gameOver:  #if game gets over do this
            message_to_screen("Score : {0}".format(score), green, disp_height // 2 - 10, disp_width // 2)
            message_to_screen("Game over, play again or quit? p/q ", red, disp_height // 25)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q or event.key == pygame.QUIT:
                        gameOver = False
                        gameExit = True
                    elif event.key == pygame.K_p:
                        gameloop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                start = True

                if event.key == pygame.K_LEFT:
                    left_or_right = -1
                    player_x_change = -player_speed
                elif event.key == pygame.K_RIGHT:
                    left_or_right = 1
                    player_x_change = player_speed
                elif event.key == pygame.K_ESCAPE:
                    start = False

        if score % 5 == 0 and score != 0:
            computer_speed += 0.5
            player_speed += 0.5
        if player_x <= 0 and left_or_right == -1:
            player_x = 0
            player_x_change = 0
        if player_x + car_width >= disp_width and left_or_right == 1:
            player_x = disp_width - car_width
            player_x_change = 0
        if computer_y > disp_height:
            score += 1
            computer_y = -car_height
            computer_x = random.choice([0, disp_width - car_width])
        if computer_x <= player_x <= computer_x + car_width and computer_y <= player_y <= computer_y + car_height - computer_speed:
            # print("hit")
            gameOver = True
        player_x += player_x_change

        if start:
            computer_y += computer_speed
            road = pygame.transform.flip(road, False, True)

        gameDisplay.blit(road, (0, 0))
        gameDisplay.blit(player_car, (player_x, player_y))
        gameDisplay.blit(computer_car, (computer_x, computer_y))
        message_to_screen("Score : " + str(score), white)
        if not start:
            message_to_screen("Paused, press any key", white, disp_height // 2)
        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()
    quit()


gameloop()
