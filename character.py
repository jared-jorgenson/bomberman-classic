import pygame

class player(object):
	def __init__(self,x,y,width,height,vel,number):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.vel = vel
		self.number = number
		self.front = True
		self.back = False
		self.left = False
		self.right = False

	def draw(self, screen):
		if self.number == 1:
			if self.front:
				screen.blit(pygame.image.load('p1front.png'), (self.x, self.y))
			elif self.back:
				screen.blit(pygame.image.load('p1back.png'), (self.x, self.y))
			elif self.left:
				screen.blit(pygame.image.load('p1left.png'), (self.x, self.y))
			else:
				screen.blit(pygame.image.load('p1right.png'), (self.x, self.y))
		elif self.number == 2:
			if self.front:
				screen.blit(pygame.image.load('p2front.png'), (self.x, self.y))
			elif self.back:
				screen.blit(pygame.image.load('p2back.png'), (self.x, self.y))
			elif self.left:
				screen.blit(pygame.image.load('p2left.png'), (self.x, self.y))
			else:
				screen.blit(pygame.image.load('p2right.png'), (self.x, self.y))


class bomb(object):
	def __init__(self,x,y,width,height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height

	def draw(self, screen):
		screen.blit(pygame.image.load('bomb.png'), (self.x, self.y))