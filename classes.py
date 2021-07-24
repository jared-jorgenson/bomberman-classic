import pygame


class Player(pygame.sprite.Sprite):
    death = [pygame.image.load('Images/death1.png'), pygame.image.load('Images/death2.png'),
             pygame.image.load('Images/death3.png'),
             pygame.image.load('Images/death4.png'), pygame.image.load('Images/death5.png'),
             pygame.image.load('Images/death6.png'),
             pygame.image.load('Images/death7.png'), pygame.image.load('Images/death8.png'),
             pygame.image.load('Images/death9.png'),
             pygame.image.load('Images/death10.png'), pygame.image.load('Images/death11.png'),
             pygame.image.load('Images/death12.png'),
             pygame.image.load('Images/death13.png'), pygame.image.load('Images/death14.png'),
             pygame.image.load('Images/death15.png'),
             pygame.image.load('Images/death16.png'), pygame.image.load('Images/death17.png'),
             pygame.image.load('Images/death18.png'),pygame.image.load('Images/death19.png'),
             pygame.image.load('Images/death20.png')]
    p1walkLeft = [pygame.image.load('Images/p1left.png'), pygame.image.load('Images/p1left1.png'),
             pygame.image.load('Images/p1left2.png'),
             pygame.image.load('Images/p1left3.png'), pygame.image.load('Images/p1left2.png'),
             pygame.image.load('Images/p1left1.png'), pygame.image.load('Images/p1left.png')]
    p1walkRight = [pygame.image.load('Images/p1right.png'), pygame.image.load('Images/p1right1.png'),
                  pygame.image.load('Images/p1right2.png'),
                  pygame.image.load('Images/p1right3.png'), pygame.image.load('Images/p1right2.png'),
                  pygame.image.load('Images/p1right1.png'), pygame.image.load('Images/p1right.png')]
    p1walkFront = [pygame.image.load('Images/p1front.png'), pygame.image.load('Images/p1front1.png'),
                   pygame.image.load('Images/p1front2.png'),
                   pygame.image.load('Images/p1front3.png'), pygame.image.load('Images/p1front2.png'),
                   pygame.image.load('Images/p1front1.png'), pygame.image.load('Images/p1front.png')]
    p1walkBack = [pygame.image.load('Images/p1back.png'), pygame.image.load('Images/p1back1.png'),
                   pygame.image.load('Images/p1back2.png'),
                   pygame.image.load('Images/p1back3.png'), pygame.image.load('Images/p1back2.png'),
                   pygame.image.load('Images/p1back1.png'), pygame.image.load('Images/p1back.png')]
    p2walkLeft = [pygame.image.load('Images/p2left.png'), pygame.image.load('Images/p2left1.png'),
                  pygame.image.load('Images/p2left2.png'),
                  pygame.image.load('Images/p2left3.png'), pygame.image.load('Images/p2left2.png'),
                  pygame.image.load('Images/p2left1.png'), pygame.image.load('Images/p2left.png')]
    p2walkRight = [pygame.image.load('Images/p2right.png'), pygame.image.load('Images/p2right1.png'),
                   pygame.image.load('Images/p2right2.png'),
                   pygame.image.load('Images/p2right3.png'), pygame.image.load('Images/p2right2.png'),
                   pygame.image.load('Images/p2right1.png'), pygame.image.load('Images/p2right.png')]
    p2walkFront = [pygame.image.load('Images/p2front.png'), pygame.image.load('Images/p2front1.png'),
                   pygame.image.load('Images/p2front2.png'),
                   pygame.image.load('Images/p2front3.png'), pygame.image.load('Images/p2front2.png'),
                   pygame.image.load('Images/p2front1.png'), pygame.image.load('Images/p2front.png')]
    p2walkBack = [pygame.image.load('Images/p2back.png'), pygame.image.load('Images/p2back1.png'),
                  pygame.image.load('Images/p2back2.png'),
                  pygame.image.load('Images/p2back3.png'), pygame.image.load('Images/p2back2.png'),
                  pygame.image.load('Images/p2back1.png'), pygame.image.load('Images/p2back.png')]
    # Constructor function
    def __init__(self, x, y, number):
        super().__init__()
        self.image = pygame.Surface([24, 28])
        self.image.fill((0,0,0))

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
        self.walkCount = 0
        self.walls = None

        self.alive = True
        self.canmove = True
        self.deathCount = 0
        self.gotomenu=False

    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y

    def update(self):
        if self.canmove:
            self.rect.x += self.change_x
            if self.change_x <0:
                self.left=True
                self.right=False
                self.front=False
                self.back=False
            elif self.change_x >0:
                self.left=False
                self.right=True
                self.front=False
                self.back=False
            block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
            for block in block_hit_list:
                if self.change_x > 0:
                    self.rect.right = block.rect.left
                else:
                    self.rect.left = block.rect.right
            self.rect.y += self.change_y
            if self.change_y <0:
                self.left=False
                self.right=False
                self.front=False
                self.back=True
            elif self.change_y >0:
                self.left=False
                self.right=False
                self.front=True
                self.back=False
            block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
            for block in block_hit_list:
                if self.change_y > 0:
                    self.rect.bottom = block.rect.top
                else:
                    self.rect.top = block.rect.bottom

    def draw(self, screen):
        if self.number == 1 and self.alive:
            if self.front:
                if self.change_y == 0:
                    screen.blit(pygame.image.load('Images/p1front.png'),
                                (self.rect.x, self.rect.y))
                else:
                    if self.walkCount + 1 >= 21:
                        self.walkCount = 0
                    screen.blit(self.p1walkFront[self.walkCount // 3], (self.rect.x, self.rect.y))
                    self.walkCount += 1
            elif self.back:
                if self.change_y == 0:
                    screen.blit(pygame.image.load('Images/p1back.png'),
                                (self.rect.x, self.rect.y))
                else:
                    if self.walkCount + 1 >= 21:
                        self.walkCount = 0
                    screen.blit(self.p1walkBack[self.walkCount // 3], (self.rect.x, self.rect.y))
                    self.walkCount += 1
            elif self.left:
                if self.change_x == 0:
                    screen.blit(pygame.image.load('Images/p1left.png'),
                                (self.rect.x, self.rect.y))
                else:
                    if self.walkCount + 1 >= 21:
                        self.walkCount = 0
                    screen.blit(self.p1walkLeft[self.walkCount // 3], (self.rect.x, self.rect.y))
                    self.walkCount += 1
            elif self.right:
                if self.change_x == 0:
                    screen.blit(pygame.image.load('Images/p1right.png'),
                                (self.rect.x, self.rect.y))
                else:
                    if self.walkCount + 1 >= 21:
                        self.walkCount = 0
                    screen.blit(self.p1walkRight[self.walkCount // 3], (self.rect.x, self.rect.y))
                    self.walkCount += 1
        elif self.number == 2 and self.alive:
            if self.front:
                if self.change_y == 0:
                    screen.blit(pygame.image.load('Images/p2front.png'),
                                (self.rect.x, self.rect.y))
                else:
                    if self.walkCount + 1 >= 21:
                        self.walkCount = 0
                    screen.blit(self.p2walkFront[self.walkCount // 3], (self.rect.x, self.rect.y))
                    self.walkCount += 1
            elif self.back:
                if self.change_y == 0:
                    screen.blit(pygame.image.load('Images/p2back.png'),
                                (self.rect.x, self.rect.y))
                else:
                    if self.walkCount + 1 >= 21:
                        self.walkCount = 0
                    screen.blit(self.p2walkBack[self.walkCount // 3], (self.rect.x, self.rect.y))
                    self.walkCount += 1
            elif self.left:
                if self.change_x == 0:
                    screen.blit(pygame.image.load('Images/p2left.png'),
                                (self.rect.x, self.rect.y))
                else:
                    if self.walkCount + 1 >= 21:
                        self.walkCount = 0
                    screen.blit(self.p2walkLeft[self.walkCount // 3], (self.rect.x, self.rect.y))
                    self.walkCount += 1
            elif self.right:
                if self.change_x == 0:
                    screen.blit(pygame.image.load('Images/p2right.png'),
                                (self.rect.x, self.rect.y))
                else:
                    if self.walkCount + 1 >= 21:
                        self.walkCount = 0
                    screen.blit(self.p2walkRight[self.walkCount // 3], (self.rect.x, self.rect.y))
                    self.walkCount += 1
        if self.alive == False and self.deathCount < 200:
            screen.blit(self.death[self.deathCount // 10], (self.rect.x, self.rect.y))
            self.deathCount += 1
        if self.deathCount >= 200:
            self.rect.x = 1000
            self.gotomenu=True
    def reset(self,x,y):
        self.gotomenu = False
        self.alive = True
        self.deathCount = 0
        self.rect.x = x
        self.rect.y = y
        self.canmove = True
        self.front = True


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

        self.walls = None
        self.leftcheck = self.rect.x - 32
        self.rightcheck = self.rect.x + self.width
        self.upcheck = self.rect.y - 32
        self.downcheck = self.rect.y + self.height
        self.expleft = True
        self.expright = True
        self.expup = True
        self.expdown = True
        self.expboxlist = []

    def draw(self, screen):
        if self.bomb_count < 30:
            screen.blit(pygame.image.load('Images/bomb3.png'), (self.rect.x, self.rect.y))
        elif self.bomb_count < 60:
            screen.blit(pygame.image.load('Images/bomb2.png'), (self.rect.x, self.rect.y))
        elif self.bomb_count < 90:
            screen.blit(pygame.image.load('Images/bomb1.png'), (self.rect.x, self.rect.y))
        elif self.bomb_count < 120:
            for i in self.walls:
                if i.rect.collidepoint(self.leftcheck,self.rect.y):
                    self.expleft = False
                if i.rect.collidepoint(self.rightcheck,self.rect.y):
                    self.expright = False
                if i.rect.collidepoint(self.rect.x,self.upcheck):
                    self.expup = False
                if i.rect.collidepoint(self.rect.x,self.downcheck):
                    self.expdown = False
            screen.blit(pygame.image.load('Images/explosion.png'), (self.rect.x, self.rect.y))
            self.expboxlist.append(pygame.Rect(self.rect.x, self.rect.y, 32, 32))
            if self.expleft:
                screen.blit(pygame.image.load('Images/explosion.png'), (self.leftcheck, self.rect.y))
                self.expboxlist.append(pygame.Rect(self.leftcheck, self.rect.y, 32, 32))
                screen.blit(pygame.image.load('Images/explosion.png'), (self.leftcheck+16, self.rect.y))
                self.expboxlist.append(pygame.Rect(self.leftcheck+16, self.rect.y, 32, 32))
            if self.expright:
                screen.blit(pygame.image.load('Images/explosion.png'), (self.rightcheck, self.rect.y))
                self.expboxlist.append(pygame.Rect(self.rightcheck, self.rect.y, 32, 32))
                screen.blit(pygame.image.load('Images/explosion.png'), (self.rightcheck-16, self.rect.y))
                self.expboxlist.append(pygame.Rect(self.rightcheck-16, self.rect.y, 32, 32))
            if self.expup:
                screen.blit(pygame.image.load('Images/explosion.png'), (self.rect.x, self.upcheck))
                self.expboxlist.append(pygame.Rect(self.rect.x, self.upcheck, 32, 32))
                screen.blit(pygame.image.load('Images/explosion.png'), (self.rect.x, self.upcheck+16))
                self.expboxlist.append(pygame.Rect(self.rect.x, self.upcheck+16, 32, 32))
            if self.expdown:
                screen.blit(pygame.image.load('Images/explosion.png'), (self.rect.x, self.downcheck))
                self.expboxlist.append(pygame.Rect(self.rect.x, self.downcheck, 32, 32))
                screen.blit(pygame.image.load('Images/explosion.png'), (self.rect.x, self.downcheck-16))
                self.expboxlist.append(pygame.Rect(self.rect.x, self.downcheck-16, 32, 32))