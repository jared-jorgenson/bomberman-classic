# Character classes
import pygame

class player(object):
	def __init__(self,x,y,width,height,vel):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.vel = vel

	def draw(self, screen):
		pygame.draw.rect(screen, (255,0,0), (
			self.x, self.y, self.width, self.height)
		)   

class bomb(object):
	def __init__(self,x,y,width,height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height

	def draw(self, screen):
		pygame.draw.rect(screen, (0,0,255), (
			self.x, self.y, self.width, self.height)
		)

