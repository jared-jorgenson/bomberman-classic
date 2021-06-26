import pygame

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
