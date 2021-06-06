import pygame
from character import *

pygame.init()

screen_width = 800
screen_height = 672

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Classic Bomberman")
background_file = "test_map.png"
bg = pygame.image.load(background_file)

clock = pygame.time.Clock()

def redrawGameWindow():
    screen.blit(bg, (0,0))
    player1.draw(screen)
    player2.draw(screen)

    for bomb in bombs1:
    	bomb.draw(screen)

    for bomb in bombs2:
    	bomb.draw(screen)
    
    pygame.display.update()

#####################
# define characters #
#####################
player1 = player(60,60,32,32,5)
player2 = player(710,550,32,32,5)
#bomb1 = bomb(player1.x, player1.y, 32, 32)
bombs1 = []
bombs2 = []
is_placed1 = False
is_placed2 = False
bomb_count1 = 0
bomb_count2 = 0
#############
# main loop #
#############
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False      

    for weapon in bombs1:
    	if bomb_count1 > 30:
    		bombs1.pop(bombs1.index(weapon))
    		is_placed1 == False
    		bomb_count1 = 0
    	else:
    		bomb_count1 += 1

    for weapon in bombs2:
    	if bomb_count2 > 30:
    		bombs2.pop(bombs2.index(weapon))
    		is_placed2 == False
    		bomb_count2 = 0
    	else:
    		bomb_count2 += 1

    keys = pygame.key.get_pressed()
    
    # Key Strokes for Player 1
    if keys[pygame.K_a]:
        player1.x -= player1.vel

    if keys[pygame.K_d]:
        player1.x += player1.vel

    if keys[pygame.K_w]:
        player1.y -= player1.vel

    if keys[pygame.K_s]:
        player1.y += player1.vel

    # Key Strokes for Player 2
    if keys[pygame.K_LEFT]:
        player2.x -= player2.vel

    if keys[pygame.K_RIGHT]:
        player2.x += player2.vel

    if keys[pygame.K_UP]:
        player2.y -= player2.vel

    if keys[pygame.K_DOWN]:
        player2.y += player2.vel

    # bomb mechanics
    # player1
    if keys[pygame.K_SPACE]:
    	if len(bombs1) < 1:
    		bombs1.append(bomb((player1.x - player1.x % 32),
    				(player1.y - player1.y % 32),32,32))
    		is_placed1 == True
    # player2
    if keys[pygame.K_SLASH]:
    	if len(bombs2) < 1:
    		bombs2.append(bomb((player2.x - player2.x % 32),
    		(player2.y - player2.y % 32),32,32))
    		is_placed2 == True
    	
    
    redrawGameWindow()
    
pygame.quit()