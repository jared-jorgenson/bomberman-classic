import pygame
from classes import *


screen_width = 480
screen_height = 352

pygame.init()

screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Classic Bomberman")
background_file = "Images/2player_bomberman_map.png"
bg = pygame.image.load(background_file)
all_sprite_list = pygame.sprite.Group()
wall_list = pygame.sprite.Group()


all_sprite_list = pygame.sprite.Group()
wall_list = pygame.sprite.Group()

# generate walls
wall = Wall(0, 0, 28, 352)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(0, 0, 480, 32)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(448, 0, 449, 352)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(32, 320, 480, 321)
wall_list.add(wall)
all_sprite_list.add(wall)

for i in range(1, 7):
    for j in range(1, 5):
        wall_list.add(Wall(64 * i, 64 * j,28,32))
        all_sprite_list.add(Wall(64 * i, 64 * j,28,32))

# generate players
player1 = Player(34, 34,1)
player2 = Player(419,289,2)
player1.walls = wall_list
player2.walls = wall_list


all_sprite_list.add(player1)
all_sprite_list.add(player2)
bombs1 = []
bombs2 = []

def redrawGameWindow():
    screen.blit(bg, (0, 0))
    for bomb in bombs1:
        bomb.walls = wall_list
        bomb.draw(screen)
        for expcheck in bomb.expboxlist:
            if player1.rect.colliderect(expcheck):
                player1.rect.x = 1000
    for bomb in bombs2:
        bomb.walls = wall_list
        bomb.draw(screen)
        for expcheck in bomb.expboxlist:
            if player2.rect.colliderect(expcheck):
                player2.rect.x = 1000
    placeholder_x1, placeholder_y1 = player1.rect.x, player1.rect.y
    placeholder_x2, placeholder_y2 = player2.rect.x, player2.rect.y
    all_sprite_list.update()
    if player1.rect.colliderect(player2.rect):
        player1.rect.x, player1.rect.y = placeholder_x1, placeholder_y1
    if player2.rect.colliderect(player1.rect):
        player2.rect.x, player2.rect.y = placeholder_x2, placeholder_y2
    player1.draw(screen)
    player2.draw(screen)

def main():
    clock = pygame.time.Clock()

    run = True
    #Main Loop
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player1.changespeed(-3, 0)
                    player1.left = True
                    player1.front = False
                    player1.back = False
                    player1.right = False
                elif event.key == pygame.K_d:
                    player1.changespeed(3, 0)
                    player1.left = False
                    player1.front = False
                    player1.back = False
                    player1.right = True
                elif event.key == pygame.K_w:
                    player1.changespeed(0, -3)
                    player1.left = False
                    player1.front = False
                    player1.back = True
                    player1.right = False
                elif event.key == pygame.K_s:
                    player1.changespeed(0, 3)
                    player1.left = False
                    player1.front = True
                    player1.back = False
                    player1.right = False
                elif event.key == pygame.K_LEFT:
                    player2.changespeed(-3, 0)
                    player2.left = True
                    player2.front = False
                    player2.back = False
                    player2.right = False
                elif event.key == pygame.K_RIGHT:
                    player2.changespeed(3, 0)
                    player2.left = False
                    player2.front = False
                    player2.back = False
                    player2.right = True
                elif event.key == pygame.K_UP:
                    player2.changespeed(0, -3)
                    player2.left = False
                    player2.front = False
                    player2.back = True
                    player2.right = False
                elif event.key == pygame.K_DOWN:
                    player2.changespeed(0, 3)
                    player2.left = False
                    player2.front = True
                    player2.back = False
                    player2.right = False

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    player1.changespeed(3, 0)
                elif event.key == pygame.K_d:
                    player1.changespeed(-3, 0)
                elif event.key == pygame.K_w:
                    player1.changespeed(0, 3)
                elif event.key == pygame.K_s:
                    player1.changespeed(0, -3)
                elif event.key == pygame.K_LEFT:
                    player2.changespeed(3, 0)
                elif event.key == pygame.K_RIGHT:
                    player2.changespeed(-3, 0)
                elif event.key == pygame.K_UP:
                    player2.changespeed(0, 3)
                elif event.key == pygame.K_DOWN:
                    player2.changespeed(0, -3)

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
                # player is left and up
                if player1.rect.x % 32 < 16 and player1.rect.y % 32 < 16:
                    bombs1.append(bomb((player1.rect.x - player1.rect.x % 32+3),
                                    (player1.rect.y - player1.rect.y % 32+1), 32, 32, 0))
                # player is left and down
                elif player1.rect.x % 32 < 16 and player1.rect.y % 32 >= 16:
                    bombs1.append(bomb((player1.rect.x - player1.rect.x % 32+3),
                                    (player1.rect.y - player1.rect.y % 32+33), 32, 32, 0))
                # player is right and up
                elif player1.rect.x % 32 >= 16 and player1.rect.y % 32 < 16:
                    bombs1.append(bomb((player1.rect.x - player1.rect.x % 32+35),
                                    (player1.rect.y - player1.rect.y % 32+1), 32, 32, 0))
                # player is right and down
                else:
                    bombs1.append(bomb((player1.rect.x - player1.rect.x % 32+35),
                                    (player1.rect.y - player1.rect.y % 32+33), 32, 32, 0))
        # player2
        if keys[pygame.K_SLASH]:
            if len(bombs2) < 1:
                # player is left and up
                if player2.rect.x % 32 < 16 and player2.rect.y % 32 < 16:
                    bombs2.append(bomb((player2.rect.x - player2.rect.x % 32+3),
                                    (player2.rect.y - player2.rect.y % 32+1), 32, 32, 0))
                # player is left and down
                elif player2.rect.x % 32 < 16 and player2.rect.y % 32 >= 16:
                    bombs2.append(bomb((player2.rect.x - player2.rect.x % 32+3),
                                    (player2.rect.y - player2.rect.y % 32+33), 32, 32, 0))
                # player is right and up
                elif player2.rect.x % 32 >= 16 and player2.rect.y % 32 < 16:
                    bombs2.append(bomb((player2.rect.x - player2.rect.x % 32+35),
                                    (player2.rect.y - player2.rect.y % 32+1), 32, 32, 0))
                # player is right and down
                else:
                    bombs2.append(bomb((player2.rect.x - player2.rect.x % 32+35),
                                    (player2.rect.y - player2.rect.y % 32+33), 32, 32, 0))
        redrawGameWindow()
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()