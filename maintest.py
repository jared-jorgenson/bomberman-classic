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
    player1.update()
    player1.draw(screen)
    player2.draw(screen)
    player2.update()

    for bomb in bombs1:
        bomb.draw(screen)

    for bomb in bombs2:
        bomb.draw(screen)

    pygame.display.flip()


#####################
# define characters #
#####################
player1 = player(34, 34, 28, 28, 1)
player2 = player(419, 289, 28, 28, 2)
bombs1 = []
bombs2 = []
hitboxes = pygame.sprite.Group()
for i in range(1, 7):
    for j in range(1, 5):
        hitboxes.add(blockHitbox(64 * i, 64 * j))
player1.walls = hitboxes
player2.walls = hitboxes
#############
# main loop #
#############
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player1.changespeed(-2, 0)
                player1.left = True
                player1.front = False
                player1.back = False
                player1.right = False
            elif event.key == pygame.K_d:
                player1.changespeed(2, 0)
                player1.left = False
                player1.front = False
                player1.back = False
                player1.right = True
            elif event.key == pygame.K_w:
                player1.changespeed(0, -2)
                player1.left = False
                player1.front = False
                player1.back = True
                player1.right = False
            elif event.key == pygame.K_s:
                player1.changespeed(0, 2)
                player1.left = False
                player1.front = True
                player1.back = False
                player1.right = False
            elif event.key == pygame.K_LEFT:
                player2.changespeed(-2, 0)
                player2.left = True
                player2.front = False
                player2.back = False
                player2.right = False
            elif event.key == pygame.K_RIGHT:
                player2.changespeed(2, 0)
                player2.left = False
                player2.front = False
                player2.back = False
                player2.right = True
            elif event.key == pygame.K_UP:
                player2.changespeed(0, -2)
                player2.left = False
                player2.front = False
                player2.back = True
                player2.right = False
            elif event.key == pygame.K_DOWN:
                player2.changespeed(0, 2)
                player2.left = False
                player2.front = True
                player2.back = False
                player2.right = False

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player1.changespeed(2, 0)
            elif event.key == pygame.K_d:
                player1.changespeed(-2, 0)
            elif event.key == pygame.K_w:
                player1.changespeed(0, 2)
            elif event.key == pygame.K_s:
                player1.changespeed(0, -2)
            elif event.key == pygame.K_LEFT:
                player2.changespeed(2, 0)
            elif event.key == pygame.K_RIGHT:
                player2.changespeed(-2, 0)
            elif event.key == pygame.K_UP:
                player2.changespeed(0, 2)
            elif event.key == pygame.K_DOWN:
                player2.changespeed(0, -2)

    for weapon in bombs1:
        if weapon.bomb_count > 120:
            bombs1.pop(bombs1.index(weapon))
            weapon.bomb_count = 0
        else:
            weapon.bomb_count += 1

    for weapon in bombs2:
        if weapon.bomb_count > 120:
            bombs2.pop(bombs2.index(weapon))
            weapon.bomb_count = 0
        else:
            weapon.bomb_count += 1

    keys = pygame.key.get_pressed()


    # bomb mechanics
    # player1
    if keys[pygame.K_SPACE]:
        if len(bombs1) < 1:
            bombs1.append(bomb((player1.x - player1.x % 32+3),
                               (player1.y - player1.y % 32+1), 32, 32, 0))
    # player2
    if keys[pygame.K_SLASH]:
        if len(bombs2) < 1:
            bombs2.append(bomb((player2.x - player2.x % 32+2),
                               (player2.y - player2.y % 32+1), 32, 32, 0))

    redrawGameWindow()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()