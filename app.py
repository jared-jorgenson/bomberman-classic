import pygame
from character import *

pygame.init()

screen_width = 800
screen_height = 640

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Classic Bomberman")
background_file = "test_map.png"
bg = pygame.image.load(background_file)

clock = pygame.time.Clock()

def redrawGameWindow():
    screen.blit(bg, (0,0))
    player1.draw(screen)
    player2.draw(screen)
    
    pygame.display.update()

#####################
# define characters #
#####################
player1 = player(60,60,32,32,5)
player2 = player(710,550,32,32,5)

#############
# main loop #
#############
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

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
    
    redrawGameWindow()
    
pygame.quit()