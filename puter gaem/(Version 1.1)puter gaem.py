import pygame
import sys
pygame.init()

# screen / overall game definitions
screen_width = 960
screen_height = 540
screen = pygame.display.set_mode((960,540))
pygame.display.set_caption('puter gaem')
clock = pygame.time.Clock()

# Defining static image's (mainly bakgrounds)
title_screen_png = pygame.image.load('1x/title_screen.png').convert()
yes_game_screen = pygame.image.load('1x/game_active.png').convert()
control_screen = pygame.image.load('1x/controls_screen.png').convert()

# Defining images that will have interactions and need rectangles 
play_button = pygame.image.load('1x/test_button.png').convert()
play_button_rect = play_button.get_rect(topleft = (430,300))
quit_button = pygame.image.load('1x/quit_button.png').convert()
quit_button_rect = quit_button.get_rect(topright = (915,45))
controls_button = pygame.image.load('1x/controls_button.png').convert()
controls_button_rect = controls_button.get_rect(bottomleft = (45,495))
back_arrow = pygame.image.load('1x/back_arrow.png').convert()
back_arrow_rect = back_arrow.get_rect(topleft = (50,50))
player = pygame.image.load('1x/player.png').convert()
player_rect = player.get_rect(bottom = (405))
floor = pygame.image.load('1x/floor.png')
floor_rect = floor.get_rect(bottom = (540))

# Game screen, general game loop will go in here (biggest func)
def game_active():
    while True:

        mouse_pos = pygame.mouse.get_pos()

        screen.blit(yes_game_screen,(0,0))
        screen.blit(quit_button,quit_button_rect)
        screen.blit(back_arrow,back_arrow_rect)
        screen.blit(floor,floor_rect)
        screen.blit(player,player_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if quit_button_rect.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                sys.exit()
            if back_arrow_rect.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
                status = 1
                return status
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                   print('left')
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    print('right')
                if event.key == pygame.K_UP or event.key == ord('w'):
                    print('jump')
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    print('left stop')
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    print('right stop')

# Screen to show player the controls
def controls_screen_active():
    while True:

        # Get mouse position
        mouse_pos = pygame.mouse.get_pos()

        # Blit a bunch of stuff
        screen.blit(control_screen,(0,0))
        screen.blit(quit_button,quit_button_rect)
        screen.blit(back_arrow,back_arrow_rect)

        pygame.display.flip()

        # For loop to check events and act accordingly
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if quit_button_rect.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                sys.exit()
            if back_arrow_rect.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
                status = 1
                return status

# Game menu screen
def start_game():
    while True:

        # Get mouse position
        mouse_pos = pygame.mouse.get_pos()

        # Blit a bunch of stuff
        screen.blit(title_screen_png,(0,0))
        screen.blit(play_button,play_button_rect)
        screen.blit(quit_button,quit_button_rect)
        screen.blit(controls_button,controls_button_rect)
        
        pygame.display.flip()

        # For loop to check events and act accordingly
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if quit_button_rect.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                sys.exit()
            if controls_button_rect.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
                status = 2
                return status
            if play_button_rect.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
                status = 3
                return status

            
# Game loop aka controller that will call functions depending on the status
# 1 = title screen
# 2 = control screen
# 3 = game mode
def game_loop(status):
    while True:
        if status == 1:
          status = start_game()
        elif status == 2:
            status = controls_screen_active()
        elif status == 3:
            status = game_active()

game_loop(1)
