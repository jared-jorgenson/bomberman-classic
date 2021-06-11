import pygame

class player(object):
	def __init__(self,x,y,width,height,vel,number):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.vel = vel
		self.number = number # player number
		self.front = True
		self.back = False
		self.left = False
		self.right = False
		self.hitbox = (self.x+3, self.y, 21, 28)

	def draw(self, screen):
		self.hitbox = (self.x+3, self.y, 21, 28)
		pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)
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

class blockHitbox(object):
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.hitbox = (self.x, self.y, 32, 32)
	def draw(self,screen):
		self.hitbox = (self.x, self.y, 32, 32)
		pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)

class bomb(object):
	def __init__(self,x,y,width,height,bomb_count):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.bomb_count = bomb_count

	def draw(self, screen):
		if self.bomb_count < 15:
			screen.blit(pygame.image.load('Images/bomb3.png'), (self.x, self.y))
		elif self.bomb_count < 30:
			screen.blit(pygame.image.load('Images/bomb2.png'), (self.x, self.y))
		elif self.bomb_count < 45:
			screen.blit(pygame.image.load('Images/bomb1.png'), (self.x, self.y))
		else:
			screen.blit(pygame.image.load('Images/explosion.png'), (self.x, self.y))