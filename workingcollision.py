import pygame

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 352

class Player(pygame.sprite.Sprite):
    # Constructor function
    def __init__(self, x, y, number):
        super().__init__()
        self.image = pygame.Surface([22, 28], pygame.SRCALPHA, 32)
        image = self.image.convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.front = True
        self.back = False
        self.left = False
        self.right = False
        self.number = number

        self.change_x = 0
        self.change_y = 0
        self.walls = None

    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y

    def update(self):
        self.rect.x += self.change_x
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right

        self.rect.y += self.change_y
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

    def draw(self, screen):
        if self.number == 1:
            if self.front:
                screen.blit(pygame.image.load('Images/p1front.png'),
                            (self.rect.x, self.rect.y))
            elif self.back:
                screen.blit(pygame.image.load('Images/p1back.png'),
                            (self.rect.x, self.rect.y))
            elif self.left:
                screen.blit(pygame.image.load('Images/p1left.png'),
                            (self.rect.x, self.rect.y))
            else:
                screen.blit(pygame.image.load('Images/p1right.png'),
                            (self.rect.x, self.rect.y))
        elif self.number == 2:
            if self.front:
                screen.blit(pygame.image.load('Images/p2front.png'),
                            (self.rect.x, self.rect.y))
            elif self.back:
                screen.blit(pygame.image.load('Images/p2back.png'),
                            (self.rect.x, self.rect.y))
            elif self.left:
                screen.blit(pygame.image.load('Images/p2left.png'),
                            (self.rect.x, self.rect.y))
            else:
                screen.blit(pygame.image.load('Images/p2right.png'),
                            (self.rect.x, self.rect.y))
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface([width,height], pygame.SRCALPHA, 32)
        image = self.image.convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
class bomb(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, bomb_count):
        super().__init__()
        self.image = pygame.Surface([22, 28], pygame.SRCALPHA, 32)
        image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.width = width
        self.height = height
        self.bomb_count = bomb_count

    def draw(self, screen):
        if self.bomb_count < 30:
            screen.blit(pygame.image.load('Images/bomb3.png'), (self.rect.x, self.rect.y))
        elif self.bomb_count < 60:
            screen.blit(pygame.image.load('Images/bomb2.png'), (self.rect.x, self.rect.y))
        elif self.bomb_count < 90:
            screen.blit(pygame.image.load('Images/bomb1.png'), (self.rect.x, self.rect.y))
        else:
            screen.blit(pygame.image.load('Images/explosion.png'), (self.rect.x, self.rect.y))

pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Classic Bomberman")
background_file = "Images/2player_bomberman_map.png"
bg = pygame.image.load(background_file)
all_sprite_list = pygame.sprite.Group()
wall_list = pygame.sprite.Group()

wall = Wall(0, 0, 32, 352)
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
        wall_list.add(Wall(64 * i, 64 * j,32,32))
        all_sprite_list.add(Wall(64 * i, 64 * j,32,32))

player1 = Player(34, 34,1)
player2 = Player(419,289,2)
player1.walls = wall_list
player2.walls = wall_list

all_sprite_list.add(player1)
all_sprite_list.add(player2)
bombs1 = []
bombs2 = []

def redrawGameWindow():
    all_sprite_list.update()
    screen.blit(bg, (0, 0))
    player1.draw(screen)
    player2.draw(screen)
    for bomb in bombs1:
        bomb.draw(screen)
    for bomb in bombs2:
        bomb.draw(screen)

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
            bombs1.append(bomb((player1.rect.x - player1.rect.x % 32+3),
                               (player1.rect.y - player1.rect.y % 32+1), 32, 32, 0))
    # player2
    if keys[pygame.K_SLASH]:
        if len(bombs2) < 1:
            bombs2.append(bomb((player2.rect.x - player2.rect.x % 32+3),
                               (player2.rect.y - player2.rect.y % 32+1), 32, 32, 0))

    redrawGameWindow()
    pygame.display.flip()

    clock.tick(60)

pygame.quit()

