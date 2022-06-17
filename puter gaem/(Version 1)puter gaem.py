import pygame
import sys
pygame.init()

game_active = False

# Declaring a bunch of variable
screen_width = 960
screen_height = 540
FPS = 30
title_screen = pygame.image.load('1x/title_screen.png')
yes_game_screen = pygame.image.load('1x/game_active.png')
BLACK = (0,0,0)
GREEN = (0,255,0)

# Defining screen
screen = pygame.display.set_mode((960,540))
pygame.display.set_caption('puter gaem')

# Defining button
play_button = pygame.image.load('1x/test_button.png').convert()
play_button_rect = play_button.get_rect(topleft = (430,220))
quit_button = pygame.image.load('1x/quit_button.png').convert()
quit_button_rect = quit_button.get_rect(topright = (915,45))
controls_button = pygame.image.load('1x/controls_button.png').convert()
controls_button_rect = controls_button.get_rect(bottomleft = (45,495))
controls_screen = pygame.image.load('1x/controls_screen.png').convert()

# Controls screen
def controls_screen_func():
    while game_active == False:
        screen.blit(controls_screen,(0,0))
        screen.blit(quit_button,quit_button_rect)

        for event in pygame.event.get():
            if quit_button_rect.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                sys.exit()

# Game loop
def game_loop():
    game_active = False
    while game_active == False:

        pygame.display.flip()
        screen.blit(title_screen,(0,0))
        screen.blit(play_button,play_button_rect)
        screen.blit(quit_button,quit_button_rect)
        screen.blit(controls_button,controls_button_rect)

        for event in pygame.event.get():
            if play_button_rect.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN:
                game_active = True
            if controls_button_rect.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN:
                controls_screen_func()
            
            if quit_button_rect.collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                sys.exit()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()



    while game_active:
        pygame.display.flip()
        screen.blit(yes_game_screen,(0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        


game_loop()
