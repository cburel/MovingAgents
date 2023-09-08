import pygame
from pygame.locals import *
import Constants

class Enemy:
	def __init__(self, pos, size, spd):

		self.pos = pos
		self.size = size
		self.spd = spd
		self.vel = pygame.Vector2(0,0)
		self.color = Constants.ENEMY_COLOR
		self.center = self.calcCenter()

	def __str__(self):
		return ("Size: " +  str(self.size) + ", " + "Pos: " + str(self.pos) + ", " + "Vel: " + str(self.vel) + ", " + "Center: " + str(self.center))

	def draw(self, screen):

		#draw the rectangle
		pygame.draw.rect(screen, (Constants.ENEMY_COLOR), pygame.Rect(self.pos.x, self.pos.y, self.size, self.size))

	def update(self, player):
		pass

	def calcCenter(self):
		return pygame.Vector2(self.pos.x + self.size / 2, self.pos.y + self.size / 2)