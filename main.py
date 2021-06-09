import pygame
from character import *

pygame.init()

screen_width = 480
screen_height = 352

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Classic Bomberman")
background_file = "Images/2player_bomberman_map.png"
bg = pygame.image.load(background_file)

clock = pygame.time.Clock()


def redrawGameWindow():
    screen.blit(bg, (0, 0))
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
player1 = player(34, 34, 28, 28, 5, 1)
player2 = player(418, 288, 28, 28, 5, 2)
bombs1 = []
bombs2 = []
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
        if weapon.bomb_count > 30:
            bombs1.pop(bombs1.index(weapon))
            weapon.bomb_count = 0
        else:
            weapon.bomb_count += 1

    for weapon in bombs2:
        if weapon.bomb_count > 30:
            bombs2.pop(bombs2.index(weapon))
            weapon.bomb_count = 0
        else:
            weapon.bomb_count += 1

    keys = pygame.key.get_pressed()

    # Key Strokes for Player 1
    if keys[pygame.K_a]:
        player1.x -= player1.vel
        player1.left = True
        player1.front = False
        player1.back = False
        player1.right = False

    if keys[pygame.K_d]:
        player1.x += player1.vel
        player1.left = False
        player1.front = False
        player1.back = False
        player1.right = True

    if keys[pygame.K_w]:
        player1.y -= player1.vel
        player1.left = False
        player1.front = False
        player1.back = True
        player1.right = False

    if keys[pygame.K_s]:
        player1.y += player1.vel
        player1.left = False
        player1.front = True
        player1.back = False
        player1.right = False

    # Key Strokes for Player 2
    if keys[pygame.K_LEFT]:
        player2.x -= player2.vel
        player2.left = True
        player2.front = False
        player2.back = False
        player2.right = False

    if keys[pygame.K_RIGHT]:
        player2.x += player2.vel
        player2.left = False
        player2.front = False
        player2.back = False
        player2.right = True

    if keys[pygame.K_UP]:
        player2.y -= player2.vel
        player2.left = False
        player2.front = False
        player2.back = True
        player2.right = False

    if keys[pygame.K_DOWN]:
        player2.y += player2.vel
        player2.left = False
        player2.front = True
        player2.back = False
        player2.right = False

    # bomb mechanics
    # player1
    if keys[pygame.K_SPACE]:
        if len(bombs1) < 1:
            explosioncoords1 = (player1.x - player1.x % 32,
                               player1.y - player1.y % 32)
            bombs1.append(bomb((player1.x - player1.x % 32),
                               (player1.y - player1.y % 32), 32, 32, 0))
    # player2
    if keys[pygame.K_SLASH]:
        if len(bombs2) < 1:
            explosioncoords2 = (player2.x - player2.x % 32),
            (player2.y - player2.y % 32)
            bombs2.append(bomb((player2.x - player2.x % 32),
                               (player2.y - player2.y % 32), 32, 32, 0))

    redrawGameWindow()

pygame.quit()