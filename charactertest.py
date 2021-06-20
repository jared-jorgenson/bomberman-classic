import pygame


class blockHitbox(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, 32, 32)


class player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, number):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.xvel = 0
        self.yvel = 0
        self.walls = None
        self.number = number  # player number
        self.front = True
        self.back = False
        self.left = False
        self.right = False
        self.rect = pygame.Rect(self.x, self.y, 28, 28)

    def changespeed(self, x, y):
        self.xvel += x
        self.yvel += y

    def update(self):
        self.x += self.xvel
        if self.x < 32:
            self.x = 32
        elif self.x > 420:
            self.x = 420
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            if self.xvel > 0:
                self.x = block.rect.left - 28
            elif self.xvel < 0:
                self.x = block.rect.right

        self.y += self.yvel
        if self.y < 34:
            self.y = 34
        elif self.y > 289:
            self.y = 289
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            if self.yvel > 0:
                self.y = block.rect.top - 29
            elif self.yvel < 0:
                self.y = block.rect.bottom

    def draw(self, screen):
        self.rect = pygame.Rect(self.x + 3, self.y, 21, 28)
        if self.number == 1:
            if self.front:
                screen.blit(pygame.image.load('Images/p1front.png'),
                            (self.x, self.y))
            elif self.back:
                screen.blit(pygame.image.load('Images/p1back.png'),
                            (self.x, self.y))
            elif self.left:
                screen.blit(pygame.image.load('Images/p1left.png'),
                            (self.x, self.y))
            else:
                screen.blit(pygame.image.load('Images/p1right.png'),
                            (self.x, self.y))
        elif self.number == 2:
            if self.front:
                screen.blit(pygame.image.load('Images/p2front.png'),
                            (self.x, self.y))
            elif self.back:
                screen.blit(pygame.image.load('Images/p2back.png'),
                            (self.x, self.y))
            elif self.left:
                screen.blit(pygame.image.load('Images/p2left.png'),
                            (self.x, self.y))
            else:
                screen.blit(pygame.image.load('Images/p2right.png'),
                            (self.x, self.y))


class bomb(object):
    def __init__(self, x, y, width, height, bomb_count):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.bomb_count = bomb_count

    def draw(self, screen):
        if self.bomb_count < 30:
            screen.blit(pygame.image.load('Images/bomb3.png'), (self.x, self.y))
        elif self.bomb_count < 60:
            screen.blit(pygame.image.load('Images/bomb2.png'), (self.x, self.y))
        elif self.bomb_count < 90:
            screen.blit(pygame.image.load('Images/bomb1.png'), (self.x, self.y))
        else:
            screen.blit(pygame.image.load('Images/explosion.png'), (self.x, self.y))
