import pygame
import secrets
from classes import *
from pygame import mixer

mixer.init()
mixer.music.load("sounds/menu_music.mp3")
mixer.music.set_volume(0.1)
mixer.music.play()

screen_width = 480
screen_height = 352

pygame.init()

screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Classic Bomberman")
background_file = "Images/2player_bomberman_map.png"
bg = pygame.image.load(background_file)
wall_list = pygame.sprite.Group()

# generate walls
wall = Wall(0, 0, 28, 352)
wall_list.add(wall)

wall = Wall(0, 0, 480, 32)
wall_list.add(wall)

wall = Wall(448, 0, 449, 352)
wall_list.add(wall)

wall = Wall(32, 320, 480, 321)
wall_list.add(wall)

for i in range(1, 7):
    for j in range(1, 5):
        wall_list.add(Wall(64 * i, 64 * j,28,32))
#Create list of all possible powerup coordinates
powerupcoords=[]
for i in range(1,14):
    for j in range(1,10):
        powerupcoords.append((i*32+2,j*32+2))
for i in range(1, 7):
    for j in range(1, 5):
        powerupcoords.remove((i*64+2,j*64+2))
#Defining these here because code crashes otherwise, they're just placeholders
randompowerupcoords = (0,0)
speedboost=powerup(randompowerupcoords[0],randompowerupcoords[1])

# generate players
player1 = Player(34, 34,1)
player2 = Player(419,289,2)
player1.walls = wall_list
player2.walls = wall_list

bombs1 = []
bombs2 = []

white=(255, 255, 255)
black=(0, 0, 0)
grey=(50, 50, 50)
red=(255, 0, 0)
green=(0, 255, 0)
blue=(0, 0, 255)
yellow=(255, 255, 0)
font = "Retro.ttf"
def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)

    return newText
def redrawGameWindow():
    screen.blit(bg, (0, 0))
    #Draw any bombs, detect collisions between players and explosions
    for bomb in bombs1:
        bomb.walls = wall_list
        bomb.draw(screen)
        for expcheck in bomb.expboxlist:
            if player1.rect.colliderect(expcheck):
                player1.alive = False
                player1.canmove = False
            elif player2.rect.colliderect(expcheck):
                player2.alive = False
                player2.canmove = False
    for bomb in bombs2:
        bomb.walls = wall_list
        bomb.draw(screen)
        for expcheck in bomb.expboxlist:
            if player2.rect.colliderect(expcheck):
                player2.alive = False
                player2.canmove = False
            elif player1.rect.colliderect(expcheck):
                player1.alive = False
                player1.canmove = False
    #Detect collisions between player and player
    placeholder_x1, placeholder_y1 = player1.rect.x, player1.rect.y
    placeholder_x2, placeholder_y2 = player2.rect.x, player2.rect.y
    player1.update()
    player2.update()
    if player1.rect.colliderect(player2.rect):
        player1.rect.x, player1.rect.y = placeholder_x1, placeholder_y1
    if player2.rect.colliderect(player1.rect):
        player2.rect.x, player2.rect.y = placeholder_x2, placeholder_y2
    #Draw players, increment time with superspeed
    player1.draw(screen)
    if player1.superspeed:
        player1.superspeedcount+=1
    player2.draw(screen)
    if player2.superspeed:
        player2.superspeedcount+=1
    #Powerups
    speedboost.spawntimer+=1
    if player1.rect.colliderect(speedboost.rect):
        speedboost.exists=False
        player1.superspeed=True
    if player2.rect.colliderect(speedboost.rect):
        speedboost.exists=False
        player2.superspeed = True
    if speedboost.exists==False:
        speedboost.respawntimer+=1
    if speedboost.respawntimer>200:
        speedboost.exists=True
        speedboost.respawntimer=0
        randompowerupcoords = secrets.choice(powerupcoords)
        while abs(randompowerupcoords[0] - player1.rect.x) < 16 or abs(randompowerupcoords[0] - player2.rect.x) < 16:
            randompowerupcoords = secrets.choice(powerupcoords)
        speedboost.rect.x = randompowerupcoords[0]
        speedboost.rect.y = randompowerupcoords[1]
    speedboost.draw(screen)
def main():
    clock = pygame.time.Clock()
    FPS = 30
    run = True
    bomb1quantity = 0
    bomb2quantity = 0
    menu = True
    p1_win = False
    p2_win = False
    game = False
    selected = "start"
    #Main Loop
    while run:
        if menu:
            #Resetting anything that changes during the game
            randompowerupcoords = secrets.choice(powerupcoords)
            while abs(randompowerupcoords[0]-player1.rect.x) < 16 or abs(randompowerupcoords[0]-player2.rect.x) < 16:
                randompowerupcoords = secrets.choice(powerupcoords)
            speedboost.rect.x = randompowerupcoords[0]
            speedboost.rect.y = randompowerupcoords[1]
            speedboost.reset()
            player1.reset(34,34)
            player2.reset(419,289)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        selected = "start"
                    elif event.key == pygame.K_DOWN:
                        selected = "quit"
                    if event.key == pygame.K_RETURN:
                        if selected == "start":
                            menu=False
                            game=True
                            p1_win=False
                            p2_win=False
                        if selected == "quit":
                            pygame.quit()
                            quit()
            # Main Menu UI
            screen.fill(grey)
            title = text_format("Bomberman", font, 90, yellow)
            if selected == "start":
                text_start = text_format("START", font, 75, white)
            else:
                text_start = text_format("START", font, 75, black)
            if selected == "quit":
                text_quit = text_format("QUIT", font, 75, white)
            else:
                text_quit = text_format("QUIT", font, 75, black)

            title_rect = title.get_rect()
            start_rect = text_start.get_rect()
            quit_rect = text_quit.get_rect()

            # Main Menu Text
            screen.blit(title, (screen_width / 2 - (title_rect[2] / 2), 50))
            screen.blit(text_start, (screen_width / 2 - (start_rect[2] / 2), 200))
            screen.blit(text_quit, (screen_width / 2 - (quit_rect[2] / 2), 260))
            pygame.display.update()
            clock.tick(FPS)
            pygame.display.set_caption("Bomberman Classic")

        elif p1_win:
            #Resetting anything that changes during the game
            randompowerupcoords = secrets.choice(powerupcoords)
            while abs(randompowerupcoords[0]-player1.rect.x) < 16 or abs(randompowerupcoords[0]-player2.rect.x) < 16:
                randompowerupcoords = secrets.choice(powerupcoords)
            speedboost.rect.x = randompowerupcoords[0]
            speedboost.rect.y = randompowerupcoords[1]
            speedboost.reset()
            player1.reset(34,34)
            player2.reset(419,289)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        selected = "Main Menu"
                    elif event.key == pygame.K_DOWN:
                        selected = "Play Again"
                    if event.key == pygame.K_RETURN:
                        if selected == "Main Menu":
                            menu=True
                            game=False
                            p1_win=False
                            p2_win=False
                        if selected == "Play Again":
                            menu=False
                            game=True
                            p1_win=False
                            p2_win=False

            # P1 Win UI
            screen.fill(red)
            title=text_format("Red Wins", font, 90, black)
            if selected=="Main Menu":
                text_start=text_format("Main Menu", font, 75, white)
            else:
                text_start = text_format("Main Menu", font, 75, black)
            if selected=="Play Again":
                text_quit=text_format("Play Again", font, 75, white)
            else:
                text_quit = text_format("Play Again", font, 75, black)

            title_rect=title.get_rect()
            start_rect=text_start.get_rect()
            quit_rect=text_quit.get_rect()

            # P1 Win Text
            screen.blit(title, (screen_width/2 - (title_rect[2]/2), 50))
            screen.blit(text_start, (screen_width/2 - (start_rect[2]/2), 200))
            screen.blit(text_quit, (screen_width/2 - (quit_rect[2]/2), 260))
            pygame.display.update()
            clock.tick(FPS)
            pygame.display.set_caption("Bomberman Classic")

        elif p2_win:
            #Resetting anything that changes during the game
            randompowerupcoords = secrets.choice(powerupcoords)
            while abs(randompowerupcoords[0]-player1.rect.x) < 16 or abs(randompowerupcoords[0]-player2.rect.x) < 16:
                randompowerupcoords = secrets.choice(powerupcoords)
            speedboost.rect.x = randompowerupcoords[0]
            speedboost.rect.y = randompowerupcoords[1]
            speedboost.reset()
            player1.reset(34,34)
            player2.reset(419,289)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        selected = "Main Menu"
                    elif event.key == pygame.K_DOWN:
                        selected = "Play Again"
                    if event.key == pygame.K_RETURN:
                        if selected == "Main Menu":
                            menu=True
                            game=False
                            p1_win=False
                            p2_win=False
                        if selected == "Play Again":
                            menu=False
                            game=True
                            p1_win=False
                            p2_win=False

            # P2 Win UI
            screen.fill(blue)
            title=text_format("Blue Wins", font, 90, black)
            if selected=="Main Menu":
                text_start=text_format("Main Menu", font, 75, white)
            else:
                text_start = text_format("Main Menu", font, 75, black)
            if selected=="Play Again":
                text_quit=text_format("Play Again", font, 75, white)
            else:
                text_quit = text_format("Play Again", font, 75, black)

            title_rect=title.get_rect()
            start_rect=text_start.get_rect()
            quit_rect=text_quit.get_rect()

            # P2 Win Text
            screen.blit(title, (screen_width/2 - (title_rect[2]/2), 50))
            screen.blit(text_start, (screen_width/2 - (start_rect[2]/2), 200))
            screen.blit(text_quit, (screen_width/2 - (quit_rect[2]/2), 260))
            pygame.display.update()
            clock.tick(FPS)
            pygame.display.set_caption("Bomberman Classic")

        elif game:
            if player1.gotomenu:
                game=False
                menu=False
                p1_win=False
                p2_win=True
            elif player2.gotomenu:
                game=False
                menu=False
                p1_win=True
                p2_win=False
            if bomb1quantity > 0:
                bomb1quantity += 1
            if bomb1quantity > 30:
                bomb1quantity = 0
            if bomb2quantity > 0:
                bomb2quantity += 1
            if bomb2quantity > 30:
                bomb2quantity = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        player1.changespeed(-player1.speed, 0)
                    elif event.key == pygame.K_d:
                        player1.changespeed(player1.speed, 0)
                    elif event.key == pygame.K_w:
                        player1.changespeed(0, -player1.speed)
                    elif event.key == pygame.K_s:
                        player1.changespeed(0, player1.speed)
                    elif event.key == pygame.K_LEFT:
                        player2.changespeed(-player2.speed, 0)
                    elif event.key == pygame.K_RIGHT:
                        player2.changespeed(player2.speed, 0)
                    elif event.key == pygame.K_UP:
                        player2.changespeed(0, -player2.speed)
                    elif event.key == pygame.K_DOWN:
                        player2.changespeed(0, player2.speed)

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        player1.changespeed(player1.speed, 0)
                    elif event.key == pygame.K_d:
                        player1.changespeed(-player1.speed, 0)
                    elif event.key == pygame.K_w:
                        player1.changespeed(0, player1.speed)
                    elif event.key == pygame.K_s:
                        player1.changespeed(0, -player1.speed)
                    elif event.key == pygame.K_LEFT:
                        player2.changespeed(player2.speed, 0)
                    elif event.key == pygame.K_RIGHT:
                        player2.changespeed(-player2.speed, 0)
                    elif event.key == pygame.K_UP:
                        player2.changespeed(0, player2.speed)
                    elif event.key == pygame.K_DOWN:
                        player2.changespeed(0, -player2.speed)

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
            if keys[pygame.K_SPACE] and bomb1quantity == 0:
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
                bomb1quantity = 1
            # player2
            if keys[pygame.K_SLASH] and bomb2quantity == 0:
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
                bomb2quantity = 1
            redrawGameWindow()
            pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()