import pygame
import sys
pygame.init()

# Constant variable's
screen_width, screen_height = 960, 540
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('puter gaem')
clock = pygame.time.Clock()

# Defining static image's (mainly bakgrounds)
title_screen_png = pygame.image.load('1x/title_screen.png').convert()
game_background = pygame.image.load('1x/game_active.png').convert()
control_screen = pygame.image.load('1x/controls_screen.png').convert()
win_screen = pygame.image.load('1x/win_screen.png').convert()

# Defining images that will have interactions and need rectangles 
play_button = pygame.image.load('1x/test_button.png').convert()
play_button_rect = play_button.get_rect(topleft = (430,300))
quit_button = pygame.image.load('1x/quit_button.png').convert()
quit_button_rect = quit_button.get_rect(topright = (915,45))
controls_button = pygame.image.load('1x/controls_button.png').convert()
controls_button_rect = controls_button.get_rect(bottomleft = (45,495))
back_arrow = pygame.image.load('1x/back_arrow.png').convert()
back_arrow_rect = back_arrow.get_rect(topleft = (50,50))
player = pygame.image.load('1x/mongoos.png').convert()
player_rect = player.get_rect(bottomleft = (0,405))
floor = pygame.image.load('1x/floor.png').convert()
floor_rect = floor.get_rect(bottom = (540))
return_button = pygame.image.load('1x/return_button.png').convert()
return_button_rect = return_button.get_rect(topleft =(294.7295,270))

# Main game function where the actual game goes
def game_active():
    
    # Rest player pos and grav everytime it's called so play always starts in same place
    player_grav = 0
    player_rect.x = 0
    player_rect.y = 330

    while True:

        # Blit everything the game needs (except play) and set mouse_pos
        mouse_pos = pygame.mouse.get_pos()
        screen.blit(game_background,(0,0))
        screen.blit(quit_button,quit_button_rect)
        screen.blit(back_arrow,back_arrow_rect)
        screen.blit(floor,floor_rect)

        # Gravity for the player and making sure the player doesn't fall through the floor
        player_grav += 1
        player_rect.y += player_grav
        if player_rect.bottom >= floor_rect.top:
            player_rect.bottom = floor_rect.top
        screen.blit(player,player_rect)

        # Win game borders, right side is win and player can't move left
        if player_rect.right >= 960:
            status = 4
            return status
        if player_rect.left <= 0:
            player_rect.left = 0

        # Event loop to check for inputs and act accordingly
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
                if player_rect.bottom == 405:
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        player_grav = -20
        
        # Player moevement (left / right)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player_rect.x += 3
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player_rect.x -= 3

        # Set fps and update display
        clock.tick(60)
        pygame.display.flip()

# Screen to show player the controls
def controls_screen_active():
    while True:

        mouse_pos = pygame.mouse.get_pos()
        screen.blit(control_screen,(0,0))
        screen.blit(quit_button,quit_button_rect)
        screen.blit(back_arrow,back_arrow_rect)

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

        # Menu screens don't need a high fps
        clock.tick(30)
        pygame.display.flip()

# Main menu screen
def start_game():
    while True:

        mouse_pos = pygame.mouse.get_pos()
        screen.blit(title_screen_png,(0,0))
        screen.blit(play_button,play_button_rect)
        screen.blit(quit_button,quit_button_rect)
        screen.blit(controls_button,controls_button_rect)

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

        clock.tick(30)        
        pygame.display.flip()

# Win screen of the game, appears after playr reaches goal
def game_win():
    while True:

        mouse_pos = pygame.mouse.get_pos()
        screen.blit(win_screen,(0,0))
        screen.blit(return_button,return_button_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if return_button_rect.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
                status = 1
                return status

        clock.tick(30)
        pygame.display.flip()
       
# Game loop aka controller that will call functions depending on the status
# 1 = title screen
# 2 = control screen
# 3 = game mode
# 4 = win screen
def game_loop(status):
    while True:
        if status == 1:
          status = start_game()
        elif status == 2:
            status = controls_screen_active()
        elif status == 3:
            status = game_active()
        elif status == 4:
            status = game_win()

# Call to the game loop to start the game
game_loop(1)
