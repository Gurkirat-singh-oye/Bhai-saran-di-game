'''Name - Sarandeep Singh
Roll no - 2018364
Sction - B
Group - 5
'''
import os
import pygame
from pygame.locals import *
from numpy import loadtxt
import time
from random import randint as rint
import sys

#Constants for the game
#gamedisplay = pygame.display.set_mode((1080,720))
font = "forte"
WIDTH, HEIGHT = (28, 28)
CHARACTERS_WIDTH,CHARACTERS_HEIGHT = (20, 20)
COIN_WIDTH, COIN_HEIGHT = (12, 12)
WALL_COLOR = pygame.Color(24, 11, 200) # RED
PACMAN_COLOR = pygame.Color(255, 255, 0) # GREEN
COIN_COLOR = pygame.Color(255, 255, 255) # YELLOW
ENEMY_1_COLOR = pygame.Color(255, 255, 0) # CYAN
ENEMY_2_COLOR = pygame.Color(242, 17, 227) # PURPLE
ENEMY_3_COLOR = pygame.Color(242, 17, 115) # BLUISH1
ENEMY_4_COLOR = pygame.Color(255, 17, 17) # BLUISH2
DOWN = (0,1)
RIGHT = (1,0)
TOP = (0,-1)
LEFT = (-1,0)
enemy_random = {1: TOP, 2: DOWN, 3: RIGHT, 4: LEFT}

#Draws a rectangle for the wall
def draw_wall(screen, pos):
    pixels = pixels_from_points(pos)
    pygame.draw.rect(screen, WALL_COLOR, [pixels, (WIDTH, HEIGHT)])
    pygame.draw.rect(screen, (0,0,0), [(pixels[0]+4,pixels[1]+4), (20, 20)])

#Draws a rectangle for the player
def draw_pacman(screen, pos):
    pixels = pixels_characters(pos)
    pygame.draw.circle(screen, PACMAN_COLOR, (pixels[0] + 10, pixels[1] + 10), 10)

#Draws a rectangle for the coin
def draw_coin(screen, pos):
    pixels = pixels_coins(pos)
    pygame.draw.circle(screen, COIN_COLOR, pixels, 5)

#Draws a rectangle for the enemy
def draw_enemy_1(screen, pos):
    pixels = pixels_characters(pos)
    pygame.draw.rect(screen, ENEMY_1_COLOR, [pixels, (CHARACTERS_WIDTH, CHARACTERS_HEIGHT)])

#Draws a rectangle for the enemy
def draw_enemy_2(screen, pos):
    pixels = pixels_characters(pos)
    pygame.draw.rect(screen, ENEMY_2_COLOR, [pixels, (CHARACTERS_WIDTH, CHARACTERS_HEIGHT)])

#Draws a rectangle for the enemy
def draw_enemy_3(screen, pos):
    pixels = pixels_characters(pos)
    pygame.draw.rect(screen, ENEMY_3_COLOR, [pixels, (CHARACTERS_WIDTH, CHARACTERS_HEIGHT)])

#Draws a rectangle for the enemy
def draw_enemy_4(screen, pos):
    pixels = pixels_characters(pos)
    pygame.draw.rect(screen, ENEMY_4_COLOR, [pixels, (CHARACTERS_WIDTH, CHARACTERS_HEIGHT)])

#Uitlity functions
def add_to_pos(pos, pos2):
    return (pos[0]+pos2[0], pos[1]+pos2[1])

def pixels_from_points(pos):
    return (pos[0]*WIDTH, pos[1]*HEIGHT)

def pixels_characters(pos):
    return (pos[0]*WIDTH + 4, pos[1]*HEIGHT + 4)

def pixels_coins(pos):
    return (pos[0]*WIDTH + 14, pos[1]*HEIGHT + 14)



#Initializing pygame
pygame.init()
screen = pygame.display.set_mode((1080, 400), 0, 32)
screen.fill([35,200,170])
#background = pygame.Surface.fill(0)

#Initializing variables
lives = 3
clock = pygame.time.Clock()
highest_score = 0
b = 150
c = 75
#loop to display the select menu and then let the person enter what he wants
x = os.system("CLS")
selected_color = (255, 255, 255)
unselected_color = (90, 90, 90)
title = pygame.font.SysFont('chiller',105).render('PACMAN', 1, (255,255,0))
screen.blit(title,(45,20))
count = 0
t = 0
while t == 0:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_DOWN or event.key == K_RIGHT:
                count+=1
            if event.key == K_UP or event.key == K_LEFT:
                count-=1
            if event.key == K_RETURN:
                t=1
        if count%3 == 0:
            x
            Start=pygame.font.SysFont(font,50).render('Start', 1, selected_color)
            Help=pygame.font.SysFont(font,50).render('Help', 1, unselected_color)
            Exit=pygame.font.SysFont(font,50).render('Exit', 1, unselected_color)
            screen.blit(Start, (100, b))
            screen.blit(Help, (100, b+c))
            screen.blit(Exit, (100, b+2*c))
            pygame.display.update()
        elif count%3 == 1:
            x
            Start=pygame.font.SysFont(font,50).render('Start', 1, unselected_color)
            Help=pygame.font.SysFont(font,50).render('Help', 1, selected_color)
            Exit=pygame.font.SysFont(font,50).render('Exit', 1, unselected_color)
            screen.blit(Start, (100, b))
            screen.blit(Help, (100, b+c))
            screen.blit(Exit, (100, b+2*c))
            pygame.display.update()
        else:
            x
            Start=pygame.font.SysFont(font,50).render('Start', 1, unselected_color)
            Help=pygame.font.SysFont(font,50).render('Help', 1, unselected_color)
            Exit=pygame.font.SysFont(font,50).render('Exit', 1, selected_color)
            screen.blit(Start, (100, b))
            screen.blit(Help, (100, b+c))
            screen.blit(Exit, (100, b+2*c))
            pygame.display.update()

if count%3 == 2:        #quit
    pygame.display.quit()
    sys.exit()
if count%3 == 1:        #display help
    screen.fill((0, 0, 0))
    background.fill((0, 0, 0))
    help_text_1="Instructions :"
    help_text_2="1) You can move using arrow keys."
    help_text_3="2) You can't cross the walls."
    help_text_4="3) If you and enemy get to the same point,"
    help_text_5="then you lose a life."
    help_text_6="4) You can Pause using spacebar "
    help_text_7="5) You can cross an enemy without losing a life."
    help_text_8="6) You can press backspace anytime to exit."
    help_display_1 = pygame.font.SysFont('bahnschrift',20).render(help_text_1, 1, (255, 255, 255))
    screen.blit(help_display_1,(50,20))
    help_display_2 = pygame.font.SysFont('bahnschrift',20).render(help_text_2, 1, (255, 255, 255))
    screen.blit(help_display_2,(50,50))
    help_display_3 = pygame.font.SysFont('bahnschrift',20).render(help_text_3, 1, (255, 255, 255))
    screen.blit(help_display_3,(50,80))
    help_display_4 = pygame.font.SysFont('bahnschrift',20).render(help_text_4, 1, (255, 255, 255))
    screen.blit(help_display_4,(50,110))
    help_display_5 = pygame.font.SysFont('bahnschrift',20).render(help_text_5, 1, (255, 255, 255))
    screen.blit(help_display_5,(50,140))
    help_display_6 = pygame.font.SysFont('bahnschrift',20).render(help_text_6, 1, (255, 255, 255))
    screen.blit(help_display_6,(50,170))
    help_display_7 = pygame.font.SysFont('bahnschrift',20).render(help_text_7, 1, (255, 255, 255))
    screen.blit(help_display_7,(50,200))
    help_display_8 = pygame.font.SysFont('bahnschrift',20).render(help_text_8, 1, (255, 255, 255))
    screen.blit(help_display_8,(50,230))
    help_display_9 = pygame.font.SysFont('bahnschrift',20).render("Press Enter to start, Backspace to exit", 1, (255, 255, 255))
    screen.blit(help_display_9,(50,260))
    pygame.display.update()
    t = 0
    while t == 0:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_RETURN:          #start the game
                    t=1
                    count = 0
                elif event.key == K_BACKSPACE:      #exit
                    t=1
                    pygame.display.quit()
                    sys.exit()
if count%3 == 0:        #start the game
    level=1
    pygame.quit()
    pygame.display.quit()
    pygame.init()
    start = time.time()
    #initializiing variables other in while loop
    # Main game loop
    while lives >0:
        var_to_decide_breaking = 0
        if level == 1 and lives == 3:
            layout = loadtxt('LAYOUT_2018364_level-1.txt', dtype=str)
        elif level == 2  and lives == lives2:
            layout = loadtxt('LAYOUT_2018364_level-2.txt', dtype=str)
        rows, cols = layout.shape
        screen = pygame.display.set_mode((WIDTH*cols, HEIGHT*rows), 0, 32)
        background = pygame.surface.Surface((WIDTH*cols, HEIGHT*rows)).convert()
        pacman_position = (1, 1)
        background.fill((0, 0, 0))
        move_direction = DOWN
        last_move = DOWN
        enemy_1_position = (8, 5)
        enemy_2_position = (9, 5)
        enemy_3_position = (10, 5)
        enemy_4_position = (11, 5)
        score = 0
        TF = 0
        coin_count=0
        while var_to_decide_breaking == 0:
            if score == coin_count and TF != 0:
                #display YOU WON when all the coins are finished
                pygame.quit()
                pygame.display.quit()
                pygame.init()
                screen = pygame.display.set_mode((560, 308), 0, 32)
                background = pygame.surface.Surface((560, 308)).convert()
                screen.fill((0, 0, 0))
                background.fill((0, 0, 0))
                you_won = pygame.font.SysFont('bahnschrift',70).render('YOU WON', 1, (0, 255, 255))
                screen.blit(you_won,(120,100))
                THANK_YOU = pygame.font.SysFont('bahnschrift',20).render('THANK YOU FOR PLAYING', 1, (0, 255, 255))
                screen.blit(THANK_YOU,(160,170))
                pygame.display.update()
                if level == 2:
                    time.sleep(2)
                    pygame.display.quit()
                    sys.exit()
                else:
                    pygame.display.quit()
                    pygame.quit()
                    pygame.init()
                    level+=1
                    highest_score = 0
                    lives2 = lives
                    break

            else:

                try:
                    move_direction = last_move
                except:
                    move_direction = DOWN
                for event in pygame.event.get():        #this for loop gets inputs and do the following - 1. move up 2. move down 3. move right 4. move left . and pauses when spacebar is pressed (till another tie spacebar is pressed)
                    if event.type == QUIT:
                        exit()
                    elif event.type == KEYDOWN:
                        if event.key == K_UP:
                            move_direction = TOP
                        elif event.key == K_DOWN:
                            move_direction = DOWN
                        elif event.key == K_LEFT:
                            move_direction = LEFT
                        elif event.key == K_RIGHT:
                            move_direction = RIGHT
                        elif event.key == K_SPACE:
                            TA=1
                            while TA==1:
                                for event2 in pygame.event.get():
                                    if event2.type == QUIT:
                                        exit()
                                    elif event2.type == KEYDOWN:
                                        if event2.key == K_SPACE:
                                            TA = 2
                                        else:
                                            TA = 1
                        elif event.key == K_BACKSPACE:
                            lives=0
                            var_to_decide_breaking = 1

                screen.blit(background, (0,0))

              #Draw board from the 2d layout array.
              #In the board, '.' denote the empty space, 'w' are the walls, 'c' are the coins
                for col in range(cols):
                    for row in range(rows):
                        value = layout[row][col]
                        pos = (col, row)
                        if value == 'w':
                            draw_wall(screen, pos)
                        elif value == 'c':
                            draw_coin(screen, pos)
                            if TF == 0:
                                coin_count+=10
                        if col == 8 and row == 5 and TF == 0:
                            draw_enemy_1(screen, pos)
                        if col == 9 and row == 5 and TF == 0:
                            draw_enemy_2(screen, pos)
                        if col == 10 and row == 5 and TF == 0:
                            draw_enemy_3(screen, pos)
                        if col == 11 and row == 5 and TF == 0:
                            draw_enemy_4(screen, pos)


                if TF == 1:
                    draw_enemy_1(screen, enemy_1_position)
                    draw_enemy_2(screen, enemy_2_position)
                    draw_enemy_3(screen, enemy_3_position)
                    draw_enemy_4(screen, enemy_4_position)


                #Draw the player
                draw_pacman(screen, pacman_position)

                #Update player position based on movement.
                score_text = pygame.font.SysFont('bahnschrift',14).render('Score - ' + str(score), 1, (255, 255, 255))
                screen.blit(score_text, (28,0))
                lives_text = pygame.font.SysFont('bahnschrift',14).render('Lives - ' + str(lives), 1, (255, 255, 255))
                screen.blit(lives_text, (28,13))
                if highest_score < score:
                    highest_score = score
                highest_text = pygame.font.SysFont('bahnschrift',14).render('Highest Score - ' + str(highest_score), 1, (255, 255, 255))
                screen.blit(highest_text, (168,0))
                level_text = pygame.font.SysFont('bahnschrift',14).render('Level - ' + str(level), 1, (255, 255, 255))
                screen.blit(level_text, (168,13))


                game_time = time.time() - start
                game_time = int(game_time*100)/100
                time_text = pygame.font.SysFont('bahnschrift',14).render('Time - ' + str(game_time), 1, (255, 255, 255))
                screen.blit(time_text, (336,00))
                if layout[add_to_pos(pacman_position, move_direction)[1],add_to_pos(pacman_position, move_direction)[0]] != 'w': #if the input move is valid, then add to position of pacman
                    pacman_position = add_to_pos(pacman_position, move_direction)
                    dummy = 1
                elif layout[add_to_pos(pacman_position, last_move)[1],add_to_pos(pacman_position, last_move)[0]] != 'w':  #if the input move is invalid check if continuing last move is valid
                    pacman_position = add_to_pos(pacman_position, last_move)
                    dummy = 0
                else:
                    pacman_position = add_to_pos(pacman_position, (0,0))    #if both the moves are invalid, then stop the pacman at that point untill a valid move is entered
                    dummy = 0
                if layout[pacman_position[1],pacman_position[0]] == 'c':    #if the player crosses a coin score incremented by 10 and that point is made a path
                    layout[pacman_position[1],pacman_position[0]] = '.'
                    score+=10
                pygame.display.update()



                move_1 = rint(1,4)      #randomly decide where to go for enemy no 1
                move_2 = rint(1,4)      #randomly decide where to go for enemy no 2
                move_3 = rint(1,4)      #randomly decide where to go for enemy no 3
                move_4 = rint(1,4)      #randomly decide where to go for enemy no 4


                #for enemies moving
                if TF == 0:
                    enemy_1_position = add_to_pos(enemy_1_position, (1,0))      #if its just the starting, then all the enemies are made out
                    enemy_1_position = add_to_pos(enemy_1_position, (0,-1))
                    enemy_2_position = add_to_pos(enemy_2_position, (0,-1))
                    enemy_3_position = add_to_pos(enemy_3_position, (0,-1))
                    enemy_4_position = add_to_pos(enemy_4_position, (-1,0))
                    enemy_4_position = add_to_pos(enemy_4_position, (0,-1))
                    dummy_1 = 1
                    dummy_2 = 1
                    dummy_3 = 1
                    dummy_4 = 1


                else:
                    if layout[add_to_pos(enemy_1_position, enemy_random[move_1])[1],add_to_pos(enemy_1_position, enemy_random[move_1])[0]] != 'w':  #if the input move is valid, then add to position of enemy- 1
                        enemy_1_position = add_to_pos(enemy_1_position, enemy_random[move_1])
                        dummy_1 = 1
                    elif layout[add_to_pos(enemy_1_position, last_move_1)[1],add_to_pos(enemy_1_position, last_move_1)[0]] != 'w':  #if the input move is invalid check if continuing last move is valid
                        enemy_1_position = add_to_pos(enemy_1_position, last_move_1)
                        dummy_1 = 0
                    else:           #if both the moves are invalid, then stop the enemy at that point untill a valid move is entered
                        enemy_1_position = add_to_pos(enemy_1_position, (0,0))
                        dummy_1 = 0



                    if layout[add_to_pos(enemy_2_position, enemy_random[move_2])[1],add_to_pos(enemy_2_position, enemy_random[move_2])[0]] != 'w':  #if the input move is valid, then add to position of enemy- 2
                        enemy_2_position = add_to_pos(enemy_2_position, enemy_random[move_2])
                        dummy_2 = 1
                    elif layout[add_to_pos(enemy_2_position, last_move_2)[1],add_to_pos(enemy_2_position, last_move_2)[0]] != 'w':  #if the input move is invalid check if continuing last move is valid
                        enemy_2_position = add_to_pos(enemy_2_position, last_move_2)
                        dummy_2 = 0
                    else:           #if both the moves are invalid, then stop the enemy at that point untill a valid move is entered
                        enemy_2_position = add_to_pos(enemy_2_position, (0,0))
                        dummy_2 = 0



                    if layout[add_to_pos(enemy_3_position, enemy_random[move_3])[1],add_to_pos(enemy_3_position, enemy_random[move_3])[0]] != 'w':  #if the input move is valid, then add to position of enemy- 3
                        enemy_3_position = add_to_pos(enemy_3_position, enemy_random[move_3])
                        dummy_3 = 1
                    elif layout[add_to_pos(enemy_3_position, last_move_3)[1],add_to_pos(enemy_3_position, last_move_3)[0]] != 'w':  #if the input move is invalid check if continuing last move is valid
                        enemy_3_position = add_to_pos(enemy_3_position, last_move_3)
                        dummy_3 = 0
                    else:           #if both the moves are invalid, then stop the enemy at that point untill a valid move is entered
                        enemy_3_position = add_to_pos(enemy_3_position, (0,0))
                        dummy_3 = 0



                    if layout[add_to_pos(enemy_4_position, enemy_random[move_4])[1],add_to_pos(enemy_4_position, enemy_random[move_4])[0]] != 'w':  #if the input move is valid, then add to position of enemy- 4
                        enemy_4_position = add_to_pos(enemy_4_position, enemy_random[move_4])
                        dummy_4 = 1
                    elif layout[add_to_pos(enemy_4_position, last_move_4)[1],add_to_pos(enemy_4_position, last_move_4)[0]] != 'w':  #if the input move is invalid check if continuing last move is valid
                        enemy_4_position = add_to_pos(enemy_4_position, last_move_4)
                        dummy_4 = 0
                    else:           #if both the moves are invalid, then stop the enemy at that point untill a valid move is entered
                        enemy_4_position = add_to_pos(enemy_4_position, (0,0))
                        dummy_4 = 0




                TF = 1
                #TODO: Check if player ate any coin, or collided with the wall by using the layout array.
                # player should stop when colliding with a wall
                # coin should dissapear when eating, i.e update the layout array


                if dummy == 1:      #assigning the right value to last_move, if invalid current move, then last ove remains the same as previous
                    last_move = move_direction
                elif dummy == 0:
                    last_move = last_move


                if dummy_1 == 1:      #assigning the right value to last_move, if invalid current move, then last ove remains the same as previous
                    last_move_1 = enemy_random[move_1]
                elif dummy_1 == 0:
                    last_move_1 = last_move_1


                if dummy_2 == 1:      #assigning the right value to last_move, if invalid current move, then last ove remains the same as previous
                    last_move_2 = enemy_random[move_2]
                elif dummy_2 == 0:
                    last_move_2 = last_move_2


                if dummy_3 == 1:      #assigning the right value to last_move, if invalid current move, then last ove remains the same as previous
                    last_move_3 = enemy_random[move_1]
                elif dummy_3 == 0:
                    last_move_3 = last_move_3


                if dummy_4 == 1:      #assigning the right value to last_move, if invalid current move, then last ove remains the same as previous
                    last_move_4 = enemy_random[move_1]
                elif dummy_4 == 0:
                    last_move_4 = last_move_4


                #Show score, lives and highest score

                if enemy_1_position == pacman_position or enemy_2_position == pacman_position or enemy_3_position == pacman_position or enemy_4_position == pacman_position :   #check if the player collides with enemy
                    var_to_decide_breaking = 1
                    lives-=1
                #Update the display
                pygame.display.update()
                clock.tick(2)       #frames per second = 2

    #if the lives are over, display GAME OVER
    pygame.quit()
    pygame.display.quit()
    pygame.init()
    screen = pygame.display.set_mode((560, 308), 0, 32)
    background = pygame.surface.Surface((560, 308)).convert()
    screen.fill((0, 0, 0))
    background.fill((0, 0, 0))
    game_over = pygame.font.SysFont('bahnschrift',70).render('GAME OVER', 1, (0, 255, 255))
    screen.blit(game_over,(100,100))
    THANK_YOU = pygame.font.SysFont('bahnschrift',20).render('THANK YOU FOR PLAYING', 1, (0, 255, 255))
    screen.blit(THANK_YOU,(170,170))
    pygame.display.update()
    time.sleep(2)
    pygame.display.quit()
